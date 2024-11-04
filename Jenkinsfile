pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone your repository (if using Git)
                git url: 'https://github.com/ruchir-panchamukhi/demo-githubactions', branch:'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
            pip install pytest
            pip install flake8
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run your tests
                sh 'pytest test_main.py'
            }
        }

        stage('Static Code Analysis') {
            steps {
                sh 'flake8 main.py test_main.py' 
            }
        }
    }

    post {
        always {
            echo 'Build finished'
        }
    }
}
