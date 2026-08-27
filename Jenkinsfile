pipeline{
    agent any
    stages{
        stage(' checkout'){
            steps{
                echo "chekout scm "
                checkout scm
            }
        }
        stage('Project check  '){
            steps{
                echo "project check "
                sh 'ls -la'
                sh 'ls -la backend'
                 sh 'ls -la frontend'
            }
        }
        stage(' Docker check '){
            steps{
                echo "Docker check "
                sh 'docker --version'
            }
        }
        stage('Docker build - backend'){
            steps{
                echo "docker build process started"
                sh "docker build -t ecommerce-backend:jenkins ./backend"
            }
        }
        stage('Docker build - frontend'){
            steps{
                echo "docker build process started"
                sh "docker build -t ecommerce-frontend:jenkins ./frontend"
            }
        }
        
    }
    post {
        success{
            echo "build completed successfully"
        }
        failure{
            echo "build failed"
        }
    }
}