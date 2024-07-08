# Project Setup Guide

## Environment Setup

```bash
# Create Conda Environment
conda create -n wineq python=3.11.9

# Activate the Environment
conda activate wineq

# Install Requirements
pip install -r requirements.txt



Download the data
## Project Initialization

# Initialize Git Repository
git init

# Initialize DVC
dvc init

# Add Data to DVC
dvc add data_given/winequality.csv

# Commit Initial Changes
git add .
git commit -m "First commit"

# Update README.md (if modified)
git add README.md
git commit -m "Update README.md"

# Add Remote Repository
git remote add origin https://github.com/MorrisLesinko/Simple_dvc_demo.git

# Push Changes to Remote Repository
git branch -M main  # Rename the branch to 'main' if necessary
git push -u origin main  # Push changes to the 'main' branch of the remote repository
