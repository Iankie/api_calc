pipeline {
    agent any
        environment {
            SEMGREP_APP_TOKEN = credentials('SEMGREP_APP_TOKEN')
        }
    
    stages {
        stage('Clear docker images') {
            steps {
                script {
                    sh 'docker stop $(docker ps -qa)'
                    sh 'docker rm $(docker ps -qa)'
                    sh 'docker rmi $(docker images -q)'
                }
            }
        }
        stage('Build and run docker-container') {
            steps {
                script {
                    sh 'docker build -f Dockerfile -t api_calc .'
                    sh 'docker run -d -p 5000:5000 api_calc:latest'
                }
            }
        }
        stage('Security Scan with Trivy') {
            steps {
                script {
                    def trivyReport = sh(script: 'sudo trivy image -f json -o ./reports/trivy-report.json --security-checks vuln api_calc:latest', returnStatus: true)
                    archiveArtifacts artifacts: 'reports/trivy-report.json', allowEmptyArchive: true
                }
            }
        }
        stage('Security Scan with Semgrep') {
            steps {
                script {
                    sh 'python -m venv venv && source ./venv/bin/activate && pip install semgrep && deactivate'
                    sh './venv/bin/semgrep -o ./reports/semgrep-report.json ./api_calc.py'
                    archiveArtifacts artifacts: 'reports/semgrep-report.json', allowEmptyArchive: true
                }
            }
        }
    }
}
