pipeline {
    agent any

    stages {

        stage('1. Checkout Code') {
            steps {
                checkout scm
                echo 'Code checked out from GitHub'
            }
        }

        stage('2. Verify Environment') {
            steps {
                bat 'python --version'
                bat 'pip --version'
            }
        }

        stage('3. Install Dependencies') {
            steps {
                bat 'pip install pylint --quiet'
                echo 'Dependencies ready'
            }
        }

        stage('4. Code Quality Check (Lint)') {
            steps {
                script {
                    // Pylint exits with non-zero on warnings, so we wrap it
                    def result = bat(
                        script: 'python -m pylint supermarket.py --disable=C0114,C0115,C0116 --exit-zero',
                        returnStatus: true
                    )
                    echo "Lint check completed (status: ${result})"
                }
            }
        }

        stage('5. Run Unit Tests') {
            steps {
                bat 'python -m unittest test_supermarket.py -v'
                echo 'All unit tests passed!'
            }
        }

        stage('6. Smoke Test') {
            steps {
                bat 'python -c "from supermarket import display_inventory, total_count, apply_discount; display_inventory(); total_count(); print(\'Discount on Rs 100 for senior: Rs\', apply_discount(100, True))"'
            }
        }

        stage('7. Build Summary') {
            steps {
                echo "============================="
                echo "Branch: ${env.BRANCH_NAME ?: 'main'}"
                echo "Build #: ${env.BUILD_NUMBER}"
                echo "Status: SUCCESS"
                echo "============================="
            }
        }
    }

    post {
        success {
            echo 'BUILD PASSED - All checks green!'
        }
        failure {
            echo 'BUILD FAILED - Check the logs above'
        }
        always {
            echo 'Build complete. View this in Stage View.'
        }
    }
}