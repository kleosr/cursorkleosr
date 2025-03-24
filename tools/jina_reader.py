#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jina.ai Web Reading Tool

This script provides functionality to read web content using Jina.ai, allowing for the retrieval of clean web text and extraction of links from the page.
It can be used as a command-line tool or imported as a module into other Python scripts.
"""

import argparse
import logging
import os
import sys
from dataclasses import dataclass
from typing import List, Dict, Optional, Any, Tuple
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def load_environment():
    """Load environment variables from .env files in order of precedence"""
    # Order of precedence:
    # 1. System environment variables (already loaded)
    # 2. .env.local (user-specific overrides)
    # 3. .env (project defaults)
    # 4. .env.example (example configuration)
    
    env_files = ['.env.local', '.env', '.env.example']
    env_loaded = False
    
    logger.info("Current working directory: %s", Path('.').absolute())
    logger.info("Looking for environment files: %s", env_files)
    
    for env_file in env_files:
        env_path = Path('.') / env_file
        logger.debug("Checking %s", env_path.absolute())
        if env_path.exists():
            logger.info("Found %s, loading variables...", env_file)
            load_dotenv(dotenv_path=env_path)
            env_loaded = True
            logger.info("Loaded environment variables from %s", env_file)
            # Print loaded keys (but not values for security)
            with open(env_path) as f:
                keys = [line.split('=')[0].strip() for line in f if '=' in line and not line.startswith('#')]
                logger.debug("Keys loaded from %s: %s", env_file, keys)
    
    if not env_loaded:
        logger.warning("No .env files found. Using system environment variables only.")
        logger.debug("Available system environment variables: %s", list(os.environ.keys()))

# Load environment variables at module import
load_environment()

# Default API token - recommended to set via environment variable or configuration file
DEFAULT_JINA_API_TOKEN = "your_jina_api_token"

@dataclass
class WebPageContent:
    """Web page content structure"""
    url: str
    title: str
    content: str
    raw_response: Optional[str] = None

class JinaReader:
    """Jina.ai Web Reading API client"""
    
    BASE_URL = "https://r.jina.ai/"
    
    def __init__(self, api_token: Optional[str] = None):
        """
        Initialize Jina.ai Web Reading client
        
        Args:
            api_token: Jina.ai API token. If None, attempts to read from environment variable.
        """
        # Attempt to get API token from environment variable
        self.api_token = api_token or os.environ.get("JINA_API_TOKEN", DEFAULT_JINA_API_TOKEN)
        if not self.api_token:
            logger.warning("Jina.ai API token not set, functionality may be limited")
    
    def read_url(self, url: str, extract_links: bool = False, timeout: int = 30) -> Optional[WebPageContent]:
        """
        Read web content
        
        Args:
            url: The web URL to read
            extract_links: Whether to extract and return a summary of links on the page
            timeout: Request timeout in seconds
            
        Returns:
            Web content object, returns None if reading fails
        """
        # Construct request URL and headers
        request_url = f"{self.BASE_URL}{url}"
        headers = {
            'Authorization': f'Bearer {self.api_token}'
        }
        
        # If links need to be extracted, add the corresponding header
        if extract_links:
            headers['X-With-Links-Summary'] = 'true'
        
        try:
            logger.info(f"Reading web page through Jina.ai: {url}")
            logger.debug(f"Request URL: {request_url}")
            logger.debug(f"Request headers: {headers}")
            
            # Send request
            response = requests.get(
                request_url,
                headers=headers,
                timeout=timeout
            )
            
            # Check response status
            response.raise_for_status()
            
            # Get response content (Markdown text)
            content = response.text
            
            # Attempt to extract title from content (usually the first line)
            title = self._extract_title_from_content(content) or self._extract_title_from_url(url)
            
            return WebPageContent(
                url=url,
                title=title,
                content=content,
                raw_response=content
            )
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Error processing web content: {str(e)}")
            import traceback
            traceback.print_exc()
            return None
    
    def _extract_title_from_content(self, content: str) -> Optional[str]:
        """Extract title from Markdown content"""
        if not content:
            return None
            
        # Attempt to find the first title line
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            # Check Markdown title format (# Title)
            if line.startswith('# '):
                return line[2:].strip()
            # Check other possible title lines
            elif line and not line.startswith('---') and not line.startswith('==='):
                return line
        
        return None
    
    def _extract_title_from_url(self, url: str) -> str:
        """Extract title from URL"""
        try:
            parsed = urlparse(url)
            path = parsed.path.strip('/')
            if path:
                # Return the last part of the path as the title
                return path.split('/')[-1].replace('-', ' ').replace('_', ' ').title()
            else:
                # If no path, return the domain name
                return parsed.netloc
        except:
            return url

def read_webpage(url: str, api_token: Optional[str] = None, 
                extract_links: bool = False) -> Tuple[Optional[str], Optional[str]]:
    """
    Convenient function to read web content using Jina.ai
    
    Args:
        url: The web URL to read
        api_token: Jina.ai API token
        extract_links: Whether to include link summary in the content
        
    Returns:
        A tuple containing the title and content
    """
    reader = JinaReader(api_token=api_token)
    result = reader.read_url(url, extract_links=extract_links)
    
    if result:
        return result.title, result.content
    else:
        return None, None

def main():
    """Command line entry point"""
    # Create command line argument parser
    parser = argparse.ArgumentParser(description="Jina.ai Web Reading Tool")
    parser.add_argument("url", help="The web URL to read")
    parser.add_argument("--token", "-t", type=str,
                      help="Jina.ai API token (optional, defaults to environment variable or built-in token)")
    parser.add_argument("--extract-links", "-l", action="store_true",
                      help="Include page link summary")
    parser.add_argument("--output", "-o", type=str,
                      help="Save content to specified file")
    parser.add_argument("--timeout", type=int, default=30,
                      help="Request timeout in seconds, default is 30 seconds")
    parser.add_argument("--debug", "-d", action="store_true",
                      help="Enable debug mode, output detailed logs")
    
    # Parse command line arguments
    args = parser.parse_args()
    
    # Set log level
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")
    
    try:
        # Initialize reader
        reader = JinaReader(api_token=args.token)
        
        # Read web content
        result = reader.read_url(
            args.url, 
            extract_links=args.extract_links,
            timeout=args.timeout
        )
        
        if not result:
            logger.error(f"Unable to read web page: {args.url}")
            sys.exit(1)
        
        # Output result
        if args.output:
            # Save to file
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(result.content)
            logger.info(f"Content saved to file: {args.output}")
        else:
            # Directly output to console
            print(result.content)
                
    except KeyboardInterrupt:
        print("\nOperation cancelled")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # If --test argument is provided, perform a simple test
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("Starting test of Jina.ai API...")
        
        test_url = "https://modelcontextprotocol.io"
        print(f"Test URL: {test_url}")
        
        # Construct request URL and headers
        request_url = f"https://r.jina.ai/{test_url}"
        headers = {
            'Authorization': f'Bearer {DEFAULT_JINA_API_TOKEN}',
            'X-With-Links-Summary': 'true'
        }
        
        print(f"Request URL: {request_url}")
        print(f"Request headers: {headers}")
        
        try:
            # Send request
            response = requests.get(
                request_url,
                headers=headers,
                timeout=30
            )
            
            # Check response status
            print(f"Response status code: {response.status_code}")
            if response.status_code == 200:
                # Display response content summary
                content = response.text
                print(content)
            else:
                print(f"Request failed, status code: {response.status_code}")
                print(f"Response content: {response.text}")
                
        except Exception as e:
            print(f"Error occurred during request: {str(e)}")
            import traceback
            traceback.print_exc()
    else:
        main()
    
    # Usage examples:
    # Basic read:
    # python tools/jina_reader.py https://example.com
    #
    # Extract link summary:
    # python tools/jina_reader.py https://example.com --extract-links
    #
    # Save content to file:
    # python tools/jina_reader.py https://example.com --output example.txt 
    #
    # Test Jina API:
    # python tools/jina_reader.py --test 