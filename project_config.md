# project_config.md
_Last updated: 2025-07-13_

<!-- STATIC:GOAL:START -->
## Goal  
AI Model Development: [model_type] for [specific_task]
Target: [accuracy/latency/throughput] baseline
<!-- STATIC:GOAL:END -->

<!-- STATIC:TECH_STACK:START -->
## Tech Stack  
- Language: Python 3.11+ | TypeScript 5
- ML: PyTorch/TensorFlow | Hugging Face | scikit-learn
- Data: pandas | numpy | Jupyter notebooks
- Tooling: pytest | Docker | MLflow (optional)
- Deployment: FastAPI | Docker | cloud platform
<!-- STATIC:TECH_STACK:END -->

<!-- STATIC:PATTERNS:START -->
## Patterns  
- Functional core, imperative shell; snake_case .py files; camelCase .ts vars
- Data versioning: git-tracked datasets <1MB, external storage refs >1MB  
- Model versioning: checkpoint files + metadata JSON
- Experiment tracking: structured logging to files
- No `any` types; type hints required; secrets via env only
<!-- STATIC:PATTERNS:END -->

<!-- STATIC:CONSTRAINTS:START -->
## Constraints  
Model size≤100MB; inference<500ms; training dataset<10GB local; GPU memory<16GB
<!-- STATIC:CONSTRAINTS:END -->

<!-- STATIC:TOKENIZATION:START -->
## Tokenization  
3.5ch/token; 8K cap; summarize workflow_state.md>12K
<!-- STATIC:TOKENIZATION:END -->

<!-- STATIC:MODEL_CONFIG:START -->
## Model Config
Type: [classification|regression|generation|detection]
Architecture: [sklearn|pytorch|tensorflow|transformers]
Input: [shape|format|preprocessing]  
Output: [classes|range|format]
Baseline: [accuracy|loss|metric] target
<!-- STATIC:MODEL_CONFIG:END -->

<!-- STATIC:DATA_CONFIG:START -->
## Data Config  
Source: [local_files|API|database|web_scraping]
Size: [num_samples] samples, [size_MB]MB estimated
Split: train/val/test [70/15/15]
Features: [feature_count] features, [categorical|numerical|text|image]
<!-- STATIC:DATA_CONFIG:END -->

<!-- DYNAMIC:CHANGELOG:START -->
## Changelog
- 2025-07-13: Cleansed out.
<!-- DYNAMIC:CHANGELOG:END -->
