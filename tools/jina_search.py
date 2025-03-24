#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Jina.ai Search Tool

This script provides functionality to perform web searches using the Jina.ai search API.
It can be used as a command-line tool or imported as a module into other Python scripts.
"""

import argparse
import json
import logging
import os
import sys
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
import requests
from urllib.parse import quote_plus
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
class JinaSearchResult:
    """Jina.ai Search Result Structure"""
    url: str
    title: str
    snippet: str
    position: int = 0
    content: Optional[str] = None
    site: Optional[str] = None

class JinaSearcher:
    """Jina.ai Search API Client"""
    
    BASE_URL = "https://s.jina.ai/"
    
    def __init__(self, api_token: Optional[str] = None, site: Optional[str] = None):
        """
        Initialize Jina.ai Search Client
        
        Args:
            api_token: Jina.ai API token. If None, attempts to read from environment variable
            site: Restrict search to a specific website domain
        """
        # Attempt to get API token from environment variable
        self.api_token = api_token or os.environ.get("JINA_API_TOKEN", DEFAULT_JINA_API_TOKEN)
        if not self.api_token:
            logger.warning("Jina.ai API token not set, search may be limited")
        
        self.site = site
        self.headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.api_token}',
            'X-No-Cache': 'true',
            'X-Respond-With': 'no-content',  # Do not return content (only return metadata)
        }
        
        # If a site is specified, add it to the request headers
        if self.site:
            self.headers['X-Site'] = self.site
    
    def search(self, query: str, num_results: int = 10, page: int = 1, site_search: bool = False) -> List[JinaSearchResult]:
        """
        Perform Jina.ai search
        
        Args:
            query: Search query
            num_results: Maximum number of results to return
            page: Pagination parameter, defaults to the first page
            site_search: Whether to limit the search to the specified site
            
        Returns:
            List of search results
        """
        try:
            # Construct query parameters
            params = {
                'q': query,
                'num': num_results
            }
            
            # If pagination is specified
            if page > 1:
                params['page'] = page
            
            # If site search is needed and a site is specified
            if site_search and self.site:
                # Already set X-Site in headers
                logger.info(f"Performing site search: {self.site}")
            
            # Send request
            logger.info(f"Searching Jina.ai: {query}")
            logger.debug(f"Request URL: {self.BASE_URL}")
            logger.debug(f"Parameters: {params}")
            logger.debug(f"Request Headers: {self.headers}")
            
            response = requests.get(
                self.BASE_URL, 
                params=params,
                headers=self.headers,
                timeout=30
            )
            
            # Check response status
            response.raise_for_status()
            
            # Log full response for debugging
            logger.debug(f"Jina.ai Response Status Code: {response.status_code}")
            logger.debug(f"Jina.ai Response Headers: {response.headers}")
            
            # For debugging: log full response content
            response_text = response.text
            logger.debug(f"Jina.ai Response Content: {response_text[:1000]}...")  # Log first 1000 characters
            
            # Parse JSON response
            try:
                data = response.json()
                # Log full JSON structure for debugging
                logger.debug(f"Jina.ai Response JSON Structure: {json.dumps(data, indent=2)[:1000]}...")
            except json.JSONDecodeError:
                logger.error("Unable to parse JSON data returned by Jina.ai")
                logger.error(f"Raw response content: {response_text[:500]}...")
                return []
            
            # Process search results
            results = []
            
            # Jina.ai API results are in the data field
            if isinstance(data, dict) and "data" in data and isinstance(data["data"], list):
                logger.info(f"Parsing data field from Jina.ai response, found {len(data['data'])} results")
                for i, item in enumerate(data["data"], 1):
                    if isinstance(item, dict):
                        result = JinaSearchResult(
                            url=item.get("url", ""),
                            title=item.get("title", item.get("name", "")),
                            snippet=item.get("description", item.get("snippet", "")),
                            position=i,
                            site=item.get("site", item.get("domain", ""))
                        )
                        results.append(result)
            # Try to find results field for backward compatibility
            elif "results" in data:
                logger.info("Using traditional format (results field) to parse Jina.ai response")
                for i, item in enumerate(data["results"], 1):
                    result = JinaSearchResult(
                        url=item.get("url", ""),
                        title=item.get("title", ""),
                        snippet=item.get("snippet", ""),
                        position=i,
                        site=item.get("site", "")
                    )
                    results.append(result)
            else:
                # Log full response structure for analysis
                logger.warning("Jina.ai returned data does not contain data or results fields")
                logger.warning(f"Response data structure: {list(data.keys()) if isinstance(data, dict) else 'not a dict'}")
                
            if results:
                logger.info(f"Successfully retrieved {len(results)} results from Jina.ai")
            else:
                logger.warning("Unable to extract valid search results from Jina.ai response")
            
            return results
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Jina.ai search request failed: {str(e)}")
            return []
        except Exception as e:
            logger.error(f"Error occurred during Jina.ai search: {str(e)}")
            return []
    
    def format_results(self, results: List[JinaSearchResult]) -> List[Dict[str, Any]]:
        """
        Format search results into a list of dictionaries
        
        Args:
            results: List of search results
            
        Returns:
            Formatted list of dictionaries
        """
        formatted_results = []
        for result in results:
            formatted_results.append({
                "url": result.url,
                "title": result.title,
                "snippet": result.snippet,
                "position": result.position,
                "site": result.site
            })
        return formatted_results

def search_jina(query: str, max_results: int = 10, api_token: Optional[str] = None, 
                site: Optional[str] = None, site_search: bool = False) -> List[Dict[str, Any]]:
    """
    Convenient function to perform search using Jina.ai
    
    Args:
        query: Search query
        max_results: Maximum number of results
        api_token: Jina.ai API token
        site: Specific website to search
        site_search: Whether to only search within the specified site
        
    Returns:
        List of dictionaries containing search results
    """
    searcher = JinaSearcher(api_token=api_token, site=site)
    results = searcher.search(query, num_results=max_results, site_search=site_search)
    return searcher.format_results(results)

def main():
    """Command line entry point"""
    # Create command line argument parser
    parser = argparse.ArgumentParser(description="Jina.ai Search Tool")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--max-results", "-n", type=int, default=10,
                      help="Maximum number of results (default: 10)")
    parser.add_argument("--token", "-t", type=str,
                      help="Jina.ai API token (optional, defaults to environment variable or built-in token)")
    parser.add_argument("--site", "-s", type=str,
                      help="Restrict search to a specific website domain (e.g., https://cursor.com)")
    parser.add_argument("--site-search", action="store_true",
                      help="Only search within the specified site")
    parser.add_argument("--json", "-j", action="store_true",
                      help="Output results in JSON format")
    parser.add_argument("--page", "-p", type=int, default=1,
                      help="Result page number (default: 1)")
    parser.add_argument("--debug", "-d", action="store_true",
                      help="Enable debug mode, output detailed logs")
    
    # Parse command line arguments
    args = parser.parse_args()
    
    # Set log level
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")
    
    try:
        # Initialize searcher
        searcher = JinaSearcher(api_token=args.token, site=args.site)
        
        # Perform search
        results = searcher.search(
            args.query, 
            num_results=args.max_results, 
            page=args.page,
            site_search=args.site_search
        )
        
        # Output results
        if args.json:
            # JSON output
            json_output = {
                "query": args.query,
                "results": searcher.format_results(results)
            }
            print(json.dumps(json_output, ensure_ascii=False, indent=2))
        else:
            # Human-readable output
            if not results:
                print("No search results found")
            else:
                for i, result in enumerate(results, 1):
                    print(f"\n--- Result {i} ---")
                    print(f"URL: {result.url}")
                    print(f"Title: {result.title}")
                    print(f"Snippet: {result.snippet}")
                    if result.site:
                        print(f"Site: {result.site}")
                
                print(f"\nTotal results: {len(results)}")
        
    except KeyboardInterrupt:
        print("\nSearch cancelled")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Search failed: {str(e)}")
        print(f"Search failed: {str(e)}")
        # Provide search link as a fallback
        print(f"\nYou can directly use the following link to search:")
        print(f"https://s.jina.ai/?q={quote_plus(args.query)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
    
    # Usage examples:
    # Basic search:
    # python tools/jina_search.py "search keyword"
    #
    # Specify maximum number of results:
    # python tools/jina_search.py "search keyword" --max-results 20
    #
    # Site search:
    # python tools/jina_search.py "search keyword" --site "https://cursor.com" --site-search
    #
    # JSON format output:
    # python tools/jina_search.py "search keyword" --json
    #
    # View second page of results:
    # python tools/jina_search.py "search keyword" --page 2 