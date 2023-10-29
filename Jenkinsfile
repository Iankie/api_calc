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
                    sh 'trivy image -f json -o ./reports/trivy-report.json --security-checks vuln api_calc:latest'
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
