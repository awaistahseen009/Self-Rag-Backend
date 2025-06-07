pipeline {
    agent any
    stages {
        stage("Setting up the python environment"){
            steps {
                echo "Setting up the python environment"
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip 
                pip install -r requirements.txt 
                '''
            }
        }

        stage("Running the tests"){
            steps {
                echo "Running the tests using pytest"
                withCredentials([
                    string(credentialsId: 'GOOGLE_API_KEY', variable: 'GOOGLE_API_KEY'),
                    string(credentialsId: 'LANGSMITH_TRACING', variable: 'LANGSMITH_TRACING'),
                    string(credentialsId: 'LANGSMITH_ENDPOINT', variable: 'LANGSMITH_ENDPOINT'),
                    string(credentialsId: 'LANGSMITH_API_KEY', variable: 'LANGSMITH_API_KEY'),
                    string(credentialsId: 'LANGSMITH_PROJECT', variable: 'LANGSMITH_PROJECT'),
                    string(credentialsId: 'OPENAI_API_KEY', variable: 'OPENAI_API_KEY'),
                    string(credentialsId: 'TAVILY_API_KEY', variable: 'TAVILY_API_KEY'),
                    string(credentialsId: 'PINECONE_API_KEY', variable: 'PINECONE_API_KEY'),
                    string(credentialsId: 'PINECONE_INDEX_NAME', variable: 'PINECONE_INDEX_NAME')
                ]) {
                    sh '''
                    . venv/bin/activate
                    pytest . -s -v 
                    '''
                }
            }
        }
    }
}