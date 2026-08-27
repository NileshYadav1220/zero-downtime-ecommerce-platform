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
        stage('Docker login'){
            steps{
                echo "docker login process startes"
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME',passwordVariable:'DOCKER_PASSWORD')]) {
                sh '''
                   echo "$DOCKER_PASSWORD" | docker login \
                   -u "$DOCKER_USERNAME" \
                  --password-stdin   
                   '''
                }
            }
        }
        stage('docker push backend to hub '){
            steps{
                echo " pushing all the stuff to docker hub "
                sh " docker push nileshyadav1220/zero-downtine-ecommerce-backend:latest"
            }
        }
        stage('docker push frontend to hub '){
            steps{
                    echo " pushing all the stuff to docker hub "
                    sh " docker push nileshyadav1220/zero-downtine-ecommerce-frontend:latest"
            }
        }
    }
    post {
        always{
            sh "docker logout || true"
        }
        success{
            echo "build completed successfully"
        }
        failure{
            echo "build failed"
        }
    }
}