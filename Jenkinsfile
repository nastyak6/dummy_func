pipeline {
    agent any
    parameters {
        choice(name: 'host', choices: ['worker11', 'worker2'], description: 'Choose the host to configure')
        string(name: 'sleep_time', defaultValue: '2', description: 'Time to sleep')
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
                    pip install --upgrade pip
                    pip install unittest
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
