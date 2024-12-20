# Dummy Function Project

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python](https://img.shields.io/badge/python-3.8+-blue)

## Overview

The **Dummy Function Project** serves as a demonstration repository to showcase the capabilities of a Jenkins multi-branch pipeline. This repository contains a simple Python function, `say_hello`, accompanied by a unit test to validate the function. The primary focus is on the integration and automation provided by the Jenkins pipeline.

## Features

- **Python Functionality**:
  - `say_hello`: A simple function that returns `"Hello, World!"`.
  - Unit tests written using `unittest` to validate the function.
  
- **Jenkins Pipeline**:
  - **Multi-Branch Pipeline**: Pipelines for each branch in the repository.
  - **Stages**:
    - **Spell Check**: Ensures code quality by identifying spelling errors using `codespell`.
    - **Syntax Check**: Validates Python code with `pylint`.
    - **Unit Tests**: Runs all test cases to ensure code functionality.
    - **GitHub Release**: Automatically creates a new GitHub release based on the pipeline's output.
  - **Cron Trigger**: The pipeline can be scheduled to run periodically, currently implemented in `nightly` branch (e.g., every 12 hours).

## How It Works

### Jenkins Pipeline
The `Jenkinsfile` in this repository defines the following stages:
1. **Install Python Environment**:
   - Installs `Python 3`, `venv`, and necessary dependencies (`codespell`, `pylint`).
   - Sets up a virtual environment to isolate the build environment.
   
2. **Spell Check**:
   - Runs `codespell` to detect and report spelling issues in the codebase.
   - Skips unnecessary directories like `venv` to optimize performance.

3. **Syntax Check**:
   - Executes `pylint` to enforce coding standards and validate the code.

4. **Unit Testing**:
   - Runs all unit tests using Python’s `unittest` module.
   - Ensures the correctness of the `say_hello` function.

5. **GitHub Release**:
   - Uses the GitHub API to create a new release based on the pipeline results.
   - The release tag is dynamically generated with a timestamp.

6. **Multi-Branch Integration**:
   - The pipeline is triggered for each branch in the repository.
   - Enables parallel testing and validation for feature branches.

### Key Benefits
- **Automation**: Reduces manual effort by automating code quality checks and testing.
- **Scalability**: Supports multiple branches, enabling developers to work in parallel without conflicts.
- **Continuous Integration**: Ensures code quality and functionality with every commit and branch creation.

## Requirements

- **Jenkins**: A working Jenkins setup with a multi-branch pipeline plugin installed.
- **Python 3.8 or higher**: For running the code and tests.


  ## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nastyak6/dummy_func.git
   
2. **Set up the Jenkins multi-branch pipeline**:

    Configure the repository URL in Jenkins.
    Add credentials for accessing GitHub.
    Start the pipeline to see automated checks and releases.


## Example Pipeline Output
![image](https://github.com/user-attachments/assets/6594fd6f-535c-4bc8-adb8-47fb1912dfdc)


