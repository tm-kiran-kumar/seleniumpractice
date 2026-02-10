pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                # Use a virtual environment to keep your Mac clean
                python3 -m venv venv --clear
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Smoke Tests') {
            steps {
                sh '''
                source venv/bin/activate
                # Run only tests marked with @pytest.mark.smoke
                # --junitxml saves results so Jenkins can read them
                pytest -m smoke --junitxml=results.xml
                '''
            }
        }
    }
    post {
        always {
            // 2. Publish test results visually in Jenkins
            junit 'results.xml'

            // Clean up workspace after run
            deleteDir()
        }
    }
}
