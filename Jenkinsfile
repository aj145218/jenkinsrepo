pipeline{
    agent {
        node{
            label 'jenkins_slave_node1'
        }
    }
    stages{
        stage("checkout Code"){
            steps{
                git url:'https://github.com/aj145218/jenkinsrepo.git', branch:'main'
                }

        }
        /*stage('Cleanup Stage'){
            steps{
                sh 'docker rm -f $(docker ps -aq)'
            }

        }*/
        stage('Build Docker image'){
            steps{
                sh 'docker build -t myimage .'
            }

        }
        stage('Add tag and Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', 
                usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker tag myimage $DOCKER_USERNAME/myimage'
                    sh 'docker push $DOCKER_USERNAME/myimage'
                }
                   
            }
        }
        stage('Deploy application to kubernetes') {
            steps {
                sh 'kubectl apply -f my-deployment.yml'
            }
        }
    }
}

        