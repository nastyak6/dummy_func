pipeline {
    agent any
    environment {
        GITHUB_TOKEN = credentials('github-token')
    }
    stages {
        stage('Main Pipeline') {
            steps {
                echo 'Starting main pipeline'
            }
        }
        stage('Install Python') {
            steps {
                sh '''
                    apt update
                    apt install -y python3 python3-venv
                '''
            }
        }
        stage('Setup') {
            steps {
                echo 'Setting up the environment...'
                sh '''

                    python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install --upgrade pip
                    '''
            }
        }
        stage('Install Codespell') {
            steps {
                sh '''
                . venv/bin/activate
                 python3 -m pip install codespell
                 '''
            }
        }
        stage('Spell Check') {
            steps {
                echo 'Checking spell check'
                script {
                    try {
                    def output = sh(returnStdout: true, script: 'codespell *').trim()
                    echo "Output: '${output}'"
                    } catch (Exception e) {
                        currentBuild.result = 'UNSTABLE' //so that if pylint failes if pylint failes 
                    }
                
                }
            }
        }
        stage('Syntax Check') {
            steps {
                echo 'Checking syntax check'
                script{
                    try {
                    def output = sh(returnStdout: true, script: 'pylint --disable=missing-module-docstring,missing-function-docstring *.py').trim()
                    echo "Output: '${output}'"
                    } catch (Exception e) {
                        currentBuild.result = 'UNSTABLE' //so that if pylintfailes if pylint failes 
                    }
                }
            }
        }
        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    . venv/bin/activate
                    python -m unittest discover -s . -p "test_*.py"
                '''
            }
        }

        stage('Create GitHub Release') {
            steps {
                script {
                    def timestamp = sh(script: "date +%Y%m%d%H%M%S", returnStdout: true).trim()
                    def tag = "v1.0-${timestamp}"
                    sh """
                    curl -X POST -H "Authorization: token ${GITHUB_TOKEN}" \
                        -H "Accept: application/vnd.github.v3+json" \
                        https://api.github.com/repos/nastyak6/dummy_func/releases \
                        -d '{"tag_name": "${tag}", "name": "${tag}", "body": "Release ${tag}", "draft": false, "prerelease": false}'
                    """
                }
            }
        }
    }
}
