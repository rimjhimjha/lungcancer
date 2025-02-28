import os

# Define the project structure
project_structure = [
    "src",
    "src/components",
    "src/pipeline",
    "src/utils",
    "src/config",
    "artifacts",
    "data",
    "notebook",
    "app",
]

# Define files to be created (excluding README.md, setup.py, and requirements.txt)
files = [
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/model_training.py",
    "src/components/model_evaluation.py",
    "src/components/prediction.py",
    "src/pipeline/__init__.py",
    "src/pipeline/train_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/logger.py",
    "src/utils/common.py",
    "src/config/__init__.py",
    "src/config/config.py",
    "app/__init__.py",
    "app/app.py",
    ".gitignore",
    "run.py",
]


for folder in project_structure:
    os.makedirs(folder, exist_ok=True)


for file in files:
    with open(file, "w") as f:
        pass