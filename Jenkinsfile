pipeline {
    agent { label 'built-in' } // This matches the "Name" in your Jenkins Nodes
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                # Use a virtual environment to keep your Mac clean
                python3 -m venv venv --clear
                source venv/bin/activate
                python3 -m pip install --upgrade pip
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
                pytest -m smoke --junitxml=results.xml --html=report.html --self-contained-html
                '''
            }
        }
    }
    post {
        always {
            // 2. Publish test results visually in Jenkins
            junit testResults: 'results.xml', allowEmptyResults: true

            //Archive the HTML report so it's clickable in the UI

            archiveArtifacts artifacts: 'report.html', fingerprint: true

            // Clean up workspace after run
            deleteDir()
        }
    }
}
