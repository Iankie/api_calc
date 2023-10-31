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
        stage('Create dir reports, venv, install semgrep') {
            steps {
                script {
                    sh '''#!/bin/bash 
                    mkdir reports
                    curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/html.tpl > html.tpl
                    python -m venv venv
                    source ./venv/bin/activate 
                    pip install semgrep
                    deactivate'''
                }
            }
        }
        stage('Security Scan with Trivy') {
            steps {
                script {
                    sh 'trivy image --format template --template "@html.tpl" -o ./reports/trivy-report.html --ignore-unfixed --security-checks vuln api_calc:latest'
                    publishHTML target : [
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'trivy-report.html',
                    reportName: 'Trivy Scan Vulns',
                    reportTitles: 'Trivy Scan Vulns'
                ]
                    sh 'trivy image --ignore-unfixed --exit-code 1 --severity HIGH,CRITICAL --security-checks vuln api_calc:latest'
                }
            }
        }
        stage('Security Scan with Semgrep') {
            steps {
                script {
                    sh './venv/bin/semgrep -o ./reports/semgrep-report.json ./api_calc.py'
                }
            }
        }
    }
}
