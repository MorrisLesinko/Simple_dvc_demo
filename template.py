import os

# Define directory paths
dirs = [
    os.path.join("data", "raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]

# Create directories if they do not exist
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)

    # Create a .gitkeep file in each directory
    with open(os.path.join(dir_, ".gitkeep"), 'a'):
        os.utime(os.path.join(dir_, ".gitkeep"), None)

# Define file paths
files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")
]

# Create empty files
for file_ in files:
    with open(file_, "w") as f:
        pass
