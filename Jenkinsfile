pipeline {
    agent any
    environment {
        GITHUB_TOKEN = credentials('github-token')
    }
    stages {
        stage('main_pipeline') {
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
                    '''
            }
        }

        stage('trigger_spell_check_pipeline') {
            steps {
                echo 'Checking spell check'
            }
        }
        stage('trigger_syntax_check_pipeline') {
            steps {
                echo 'Checking syntax check'
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
