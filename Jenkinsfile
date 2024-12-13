pipeline {
    agent any
    triggers {
        cron('*/5 * * * *') // Runs every day at 11 PM (23:00)
    }
    stages {
        stage('main_pipeline') {
            steps {
                echo 'Starting main pipeline'
            }
        }
        stage('Install Python') {
            steps {
                echo 'Installing Python...'
                retry(3) {
                    sh '''
                    apt update -y || sudo rm -rf /var/lib/apt/lists/*
                    DEBIAN_FRONTEND=noninteractive apt install -y python3 python3-venv || {
                        echo "Failed to install Python";
                        exit 1;
                    }
                    '''
                }
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
    }
}
