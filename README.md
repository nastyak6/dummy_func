# Dummy Function Project

![Build Status](https://img.shields.io/badge/build-passing-brightgreen) ![Python](https://img.shields.io/badge/python-3.8+-blue)

## Overview

The **Dummy Function Project** serves as a demonstration repository to showcase the capabilities of a Jenkins multi-branch pipeline. This repository contains a simple Python function, `say_hello`, accompanied by a unit test to validate the function. The primary focus is on the integration and automation provided by the Jenkins pipeline.
This repo was created as a part of our devops course , and is used in this [PROJECT](https://github.com/annageryes/Final_Project_Devops)

## Features

- **Python Functionality**:
  - [say_hello](https://github.com/nastyak6/dummy_func/blob/main/test_hello.py): A simple function that returns `"Hello, World!"`.
  - Unit tests written using `unittest` to validate the function.
  
- **[Jenkins CI/CD Pipeline](https://github.com/nastyak6/dummy_func/blob/main/Jenkinsfile):**
  - **Multi-Branch Pipeline**: Pipelines for each branch in the repository.
  - **Stages**:
    - **Spell Check**: Ensures code quality by identifying spelling errors using `codespell`.
    - **Syntax Check**: Validates Python code with `pylint`.
    - **Unit Tests**: Runs all test cases to ensure code functionality.
    - **GitHub Release**: Automatically creates a new GitHub release based on the pipeline's output.
  - **Cron Trigger**: The pipeline can be scheduled to run periodically, currently implemented in [`nightly`](https://github.com/nastyak6/dummy_func/tree/nightly)  branch (e.g., every 12 hours).

## How It Works

### Jenkins  CI/CD Pipeline
The [Jenkinsfile](https://github.com/nastyak6/dummy_func/blob/main/Jenkinsfile) in this repository defines the following stages:
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

5. **[GitHub Release](https://github.com/nastyak6/dummy_func/releases)**:
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

- **Jenkins**: [A working Jenkins setup with a multi-branch pipeline plugin installed.](https://github.com/annageryes/Final_Project_Devops)
- **Python 3.8 or higher**: For running the code and tests.


  ## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nastyak6/dummy_func.git
   
2. **Set up the Jenkins multi-branch pipeline**:

    Configure the repository URL in Jenkins.
    Add credentials for accessing GitHub.
    Start the pipeline to see automated checks and releases.
   ![image](https://github.com/user-attachments/assets/075d984a-55e2-4ed7-8439-e4df36dc925c)



## Example Pipeline Output
![image](https://github.com/user-attachments/assets/fb964e4c-0282-4cd1-a219-4d1ebcff5f72)

![image](https://github.com/user-attachments/assets/4afa636d-7eb7-4906-85ff-cba2be050cd7)


### Jenkins Data Pipeline
- *Revert Pipeline*: Automates rollback to the last known good state.
- *Backup Pipeline*: Automates backup of critical data and artifacts.

 *we combined both actions into one pipline with condional arguments
The  [Jenkinsdata](https://github.com/nastyak6/dummy_func/blob/main/Jenkinsdata) in this repository defines the following stages:
1. **Define the args in Environment vars**
   
2. **CD into the Git repo;s directory**:
   - to be able to access the files easily

3. **Install smbclient**:
   - This tools will help us manage the Samba action easily
   - added installation here in case it is missing in the agent

4. **Backup data**:
   - if the action arg passed was backup this stage will run.
   - create a unique date+timestamp var
   - using the samba tool to authinticate and run the following commands:
      1- create a directory with the unique timestamp name
      2- cd into the new dir
      3- lcd changes the current directory on the local machine path (where the data that needed to be backed up exists)
      4- set prompt and recursive (turn off confirmation prompt before each file is uploaded , and run recusrivly on the given directory) 
      5- mput is used to upload multiple files from the local machine to the remote server

5. **Revert data**:
   - if the action arg passed was Revert this stage will run.
   - get the latest backup dir by the timestamp+date name from samba using smbclinet tool
   - put the wanted directory name in a variable and create a directoy to upload the reverted data in
   - using the samba tool to authinticate and run the following commands:
      1- cd into the latest backup folder found
      2- lcd changes the current directory on the local machine path (where the backed up data need to go to )
      4- set prompt and recursive (turn off confirmation prompt before each file is uploaded , and run recusrivly on the given directory) 
      5- mget downloads multiple files from the remote SMB server to the local system.

6. **print output msg for the user**


## Create a new Pipline in Jenkins
- make sure to add the git repo in the SCM with the jekinsdata file name
- run intial job , to get all the arguments , so that the next run you'll be able to view and input them.

## Example Pipeline ARGS

![image](https://github.com/user-attachments/assets/2e22bac3-6113-4303-96c3-8cb7d961c7be)



