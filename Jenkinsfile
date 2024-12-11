pipeline {
    agent any
    parameters {
        choice(name: 'host', choices: ['worker11', 'worker2'], description: 'Choose the host to configure')
        string(name: 'sleep_time', defaultValue: '2', description: 'Time to sleep')
    }
    triggers {
        cron('0 21 * * *') // Runs every day at 9 PM (21:00)
    }
    stages {
        stage('main_pipeline') {
            steps {
                echo 'Starting main pipeline'
                sleep time: sleep_time.toInteger(), unit: 'SECONDS'
            }
        }
        stage('pre-requisites') {
            steps {
                echo 'Checking pre-requisites'
                sleep time: sleep_time.toInteger(), unit: 'SECONDS'
            }
        }
        stage('trigger_spell_check_pipeline') {
            steps {
                echo 'Checking spell check'
                sleep time: sleep_time.toInteger(), unit: 'SECONDS'
            }
        }
        stage('trigger_syntax_check_pipeline') {
            steps {
                echo 'Checking syntax check'
                sleep time: sleep_time.toInteger(), unit: 'SECONDS'
            }
        }
        stage('trigger_test_pipeline') {
            steps {
                echo 'Testing'
                sleep time: sleep_time.toInteger(), unit: 'SECONDS'
            }
        }
    }
}
