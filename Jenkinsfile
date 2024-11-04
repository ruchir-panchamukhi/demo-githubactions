pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone your repository (if using Git)
                git 'https://github.com/yourusername/your-repo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install pytest directly
                sh 'pip install pytest'
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
                // Run a static analysis tool like flake8 or pylint
                sh 'flake8 main.py test_main.py' // Adjust as necessary
            }
        }
    }

    post {
        always {
            // Clean up or notify (optional)
            echo 'Build finished'
        }
    }
}
