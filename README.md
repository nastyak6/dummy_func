### dummy_func

dummy_func is a simple Python project designed to demonstrate continuous integration and continuous deployment (CI/CD) practices. It includes a basic function and corresponding unit tests to showcase automated testing workflows.
Features

    say_hello Function: Returns the string "Hello, World!".
    Unit Tests: Validates the output of the say_hello function.

## Getting Started
# Prerequisites

    Python 3.x

# Installation

    Clone the Repository:

git clone https://github.com/nastyak6/dummy_func.git
cd dummy_func

Set Up a Virtual Environment:

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:

    pip install -r requirements.txt

# Usage

from hello import say_hello

print(say_hello())  # Outputs: Hello, World!

# Running Tests

python -m unittest discover -s tests

# Contributing

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes.
    Commit your changes (git commit -m 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Open a pull request.
