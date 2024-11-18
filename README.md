# Azure Pipelines Generator

Azure Pipelines Generator is a Python library for programmatically creating Azure DevOps Pipelines.

## Benefits
- Separate configuration from code
- Write testable and reusable pipelines
- Harness the power of Python

## Installation

Install the library with pip:

```bash
pip install azure-pipelines-generator
```

## Usage

Example of creating a pipeline:

```python
import yaml
from azure_pipelines_generator.models.azure_pipelines_models import Pipeline, Stage, Job, Step

# Pipeline configurations
platforms = {
    "Xbox": "echo Building, testing, and deploying for Xbox",
    "PS5": "echo Building, testing, and deploying for PS5",
    "PC": "echo Building, testing, and deploying for PC",
}

# Create jobs dynamically using platform configurations
jobs = [
    Job(
        name=f"{platform}Job",
        steps=[Step(script=script, name=f"{platform}_Step")]
    )
    for platform, script in platforms.items()
]

# Create a stage containing all jobs
stage = Stage(
    name="BuildAndDeployStage",
    jobs=jobs
)

# Create a pipeline
pipeline = Pipeline(
    name="GamingPlatformPipeline",
    trigger={"branches": {"include": ["main"]}},
    stages=[stage]
)

# Serialize pipeline to YAML
pipeline_yaml = yaml.dump(pipeline.to_dict(), sort_keys=False)

# Save to a YAML file
with open("azure-pipelines.yaml", "w") as f:
    f.write(pipeline_yaml)

print("Pipeline YAML generated and saved to 'azure-pipelines.yaml'")
```

## Development

To set up the project for development:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/azure-pipelines-generator.git
   cd azure-pipelines-generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Update schema and generate models:
   ```bash
   python update_schema_and_models.py
   ```

## License

This project is licensed under the MIT License.