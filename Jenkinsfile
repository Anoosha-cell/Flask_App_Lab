pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        VENV = "venv"
        DEPLOY_DIR = "/tmp/flask_deploy"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning the GitHub repository'
                git branch: 'main',
                    url: 'https://github.com/your-username/flask-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies'
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Running unit tests'
                sh '''
                . $VENV/bin/activate
                pytest
                '''
            }
        }

        stage('Build Application') {
            steps {
                echo 'Building the application'
                sh '''
                mkdir -p build
                cp app.py requirements.txt build/
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                echo 'Deploying the application'
                sh '''
                mkdir -p $DEPLOY_DIR
                cp -r build/* $DEPLOY_DIR/
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully'
        }
        failure {
            echo 'Pipeline execution failed'
        }
    }
}
