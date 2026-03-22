pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls the latest code from the repository
                git branch: 'main', url: 'https://github.com/2024ht66503-shash/devops-assignment-Shashwat-Sharma'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Installs Flask and Pytest
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Automated Testing') {
            steps {
                // Executes the test suite to confirm stability
                sh 'pytest'
            }
        }
        
        stage('Docker Image Assembly') {
            steps {
                // Builds the final containerized application
                sh 'docker build -t aceest-gym-app:latest .'
            }
        }
    }
    
    post {
        success {
            echo 'Jenkins BUILD completed successfully without errors.'
        }
        failure {
            echo 'Jenkins BUILD failed. Check the logs.'
        }
    }
}