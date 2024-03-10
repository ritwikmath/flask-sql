pipeline {
    agent {
        dockerfile { filename 'Dockerfile'}
    }
    stages {
        stage('Prebuilt') {
            steps {
                sh "ls -al"
                echo "$MONGO_USER"
            }
        }
    }
}