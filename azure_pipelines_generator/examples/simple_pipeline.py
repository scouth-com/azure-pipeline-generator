import yaml
from azure_pipelines_generator.models.azure_pipelines_models import Pipeline, Stage, Job, Step

# Platform configurations
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