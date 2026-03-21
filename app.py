from flask import Flask, render_template, request, Response
from prometheus_client import Counter,generate_latest
from flipkart.data_ingestion import DataIngestion
from flipkart.rag_chain import RagChainBuilder
from utils.logger import logging
from dotenv import load_dotenv
load_dotenv()

REQUEST_COUNT= Counter("http_request_total", "Total number of HTTP requests")

def create_app():
    app = Flask(__name__)
    print("[DEBUG] Initializing DataIngestion...")
    vector_store=DataIngestion().ingest(load_existing=True)
    print("[DEBUG] DataIngestion complete. Building RAG chain...")
    rag_chain = RagChainBuilder(vector_store).build_chain()
    print("[DEBUG] RAG chain built successfully.")
    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/get', methods = ['POST'])
    def get_response():
        REQUEST_COUNT.inc()
        user_input = request.form['msg']
        logging.info(f"Received user input: {user_input}")
        
        response = rag_chain.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": "user_session"}}
        )
        
        logging.info(f"Generated response: {response}")
        return Response(response['answer'], mimetype='text/plain')
    
    @app.route('/metrics')
    def metrics():
        return Response(generate_latest(), mimetype='text/plain')
    
    return app

if __name__ == '__main__':
    app= create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)