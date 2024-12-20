pipeline {
    agent any
    triggers {
        cron('H */12 * * *') // Runs every 12 hours
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
                    whoami
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
    }
}
