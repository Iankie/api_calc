pipeline {
    agent any
    
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
                    def trivyReport = sh(script: 'trivy --format json --output ./reports/trivy-report.json api_calc:latest', returnStatus: true)
                    archiveArtifacts artifacts: 'reports/trivy-report.json', allowEmptyArchive: true
                    if (trivyReport != 0) {
                        error("Trivy scan failed with a non-zero exit code")
                    }
                }
            }
        }
        stage('Security Scan with Semgrep') {
            steps {
                script {
                    sh 'semgrep -o ./reports/semgrep-report.json -e ./semgrep-policies/security-policy.yml ./api_calc.py'
                    archiveArtifacts artifacts: 'reports/semgrep-report.json', allowEmptyArchive: true
                }
            }
        }
    }
}
