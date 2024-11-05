pipeline {
    agent { label 'new_master' }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ruchir-panchamukhi/demo-githubactions', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    pip install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_main.py'
            }
        }
    }

    post {
        always {
            echo 'Build finished'
        }
        
        success {
            mail to: 'ruuchirappu@gmail.com', 
                 subject: "Jenkins Build Successful: ${env.JOB_NAME} #${env.BUILD_NUMBER}", 
                 body: "Good news! The Jenkins build for job ${env.JOB_NAME} #${env.BUILD_NUMBER} completed successfully.\nCheck it at ${env.BUILD_URL}"
        }

        failure {
            mail to: 'ruuchirappu@gmail.com', 
                 subject: "Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}", 
                 body: "Unfortunately, the Jenkins build for job ${env.JOB_NAME} #${env.BUILD_NUMBER} failed.\nCheck it at ${env.BUILD_URL}"
        }
    }
}

