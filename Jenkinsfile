pipeline {

    agent any

    stages {

        stage('Checkout') {

            steps {
                echo "Checkout SCM"
                checkout scm
            }
        }

        stage('Project Check') {

            steps {
                echo "Project check"

                sh 'ls -la'
                sh 'ls -la backend'
                sh 'ls -la frontend'
            }
        }

        stage('Docker Check') {

            steps {
                echo "Docker check"

                sh 'docker --version'
            }
        }

        stage('Docker Build - Backend') {

            steps {
                echo "Building backend Docker image"

                sh 'docker build -t ecommerce-backend:jenkins ./backend'

                echo "Tagging backend image"

                sh 'docker tag ecommerce-backend:jenkins nileshyadav1220/zero-downtime-ecommerce-backend:latest'
            }
        }

        stage('Docker Build - Frontend') {

            steps {
                echo "Building frontend Docker image"

                sh 'docker build -t ecommerce-frontend:jenkins ./frontend'

                echo "Tagging frontend image"

                sh 'docker tag ecommerce-frontend:jenkins nileshyadav1220/zero-downtime-ecommerce-frontend:latest'
            }
        }

        stage('Docker Login') {

            steps {
                echo "Docker login started"

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {

                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login \
                        -u "$DOCKER_USERNAME" \
                        --password-stdin
                    '''
                }
            }
        }

        stage('Docker Push Backend') {

            steps {
                echo "Pushing backend image to Docker Hub"

                sh 'docker push nileshyadav1220/zero-downtime-ecommerce-backend:latest'
            }
        }

        stage('Docker Push Frontend') {

            steps {
                echo "Pushing frontend image to Docker Hub"

                sh 'docker push nileshyadav1220/zero-downtime-ecommerce-frontend:latest'
            }
        }
    }

    post {

        always {
            sh 'docker logout || true'
        }

        success {
            echo "========================================"
            echo "BUILD COMPLETED SUCCESSFULLY"
            echo "Docker images pushed to Docker Hub"
            echo "========================================"
        }

        failure {
            echo "========================================"
            echo "BUILD FAILED"
            echo "Check the stage where the pipeline failed"
            echo "========================================"
        }
    }
}