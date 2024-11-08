pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/nandhuk043/deepesh_repo.git'
            }
        }

        stage('Build and Deploy') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d --build'
            }
        }

        stage('Test') {
            steps {
                sh 'sleep 10'  // Allow time for services to start
                sh 'curl -f http://localhost:3000 || echo "App failed to respond!"'
            }
        }
    }

    post {
        always {
            sh 'docker-compose down'
        }
    }
}
