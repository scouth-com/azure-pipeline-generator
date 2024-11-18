import os
import subprocess
import requests
import json
import jsonschema

SCHEMA_URL = "https://github.com/Microsoft/azure-pipelines-vscode/raw/main/service-schema.json"
SCHEMA_PATH = "azure_pipelines_generator/schema/azure_pipelines_schema.json"
MODELS_PATH = "azure_pipelines_generator/models/azure_pipelines_models.py"
INIT_FILE = "azure_pipelines_generator/__init__.py"

def download_schema():
    """Download the Azure DevOps schema and save it to the schema directory."""
    print(f"Downloading schema from {SCHEMA_URL}...")
    response = requests.get(SCHEMA_URL)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(SCHEMA_PATH), exist_ok=True)
        with open(SCHEMA_PATH, "w") as f:
            f.write(response.text)
        print(f"Schema downloaded to {SCHEMA_PATH}")
    else:
        print(f"Failed to download schema. HTTP Status: {response.status_code}")
        exit(1)

def validate_schema():
    """Validate the downloaded schema for correctness."""
    print(f"Validating schema at {SCHEMA_PATH}...")
    with open(SCHEMA_PATH, "r") as f:
        schema = json.load(f)

    try:
        jsonschema.Draft7Validator.check_schema(schema)
        print("Schema validation successful.")
    except jsonschema.exceptions.SchemaError as e:
        print(f"Schema validation failed: {e.message}")
        exit(1)

def extract_version_info():
    """Extract the schema version and update the library."""
    print(f"Extracting schema version from {SCHEMA_PATH}...")
    with open(SCHEMA_PATH, "r") as f:
        schema = json.load(f)
        version = schema.get("$comment", "Unknown version")
        print(f"Schema version: {version}")
        update_init_file(version)

def update_init_file(schema_version):
    """Update the __schema_version__ in the library's __init__.py file."""
    print(f"Updating schema version in {INIT_FILE}...")
    with open(INIT_FILE, "r") as f:
        lines = f.readlines()

    with open(INIT_FILE, "w") as f:
        for line in lines:
            if line.startswith("__schema_version__"):
                f.write(f'__schema_version__ = "{schema_version}"\n')
            else:
                f.write(line)
    print(f"Schema version updated in {INIT_FILE}")

def generate_models():
    """Generate Python models from the JSON schema using QuickType."""
    print("Generating Python models from schema using QuickType...")

    try:
        subprocess.run(
            [
                "quicktype",
                "--just-types",
                "--lang", "python",
                "--src", SCHEMA_PATH,
                "--out", MODELS_PATH,
            ],
            check=True,
        )
        print(f"Models generated and saved to {MODELS_PATH}")
    except FileNotFoundError:
        print("Error: QuickType CLI is not installed.")
        print("Install it with: npm install -g quicktype")
        exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error generating models: {e}")
        exit(1)

if __name__ == "__main__":
    download_schema()        # Download the latest schema
    validate_schema()        # Validate the schema
    extract_version_info()   # Extract and update the schema version
    generate_models()        # Generate Python models
