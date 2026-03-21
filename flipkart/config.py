import os
from dotenv import load_dotenv
load_dotenv()

class Config():
    ASTRA_DB_API_ENDPOINT=os.getenv('ASTRA_DB_API_ENDPOINT')
    ASTRA_DB_APPLICATION_TOKEN=os.getenv('ASTRA_DB_APPLICATION_TOKEN')
    ASTRA_DB_KEYSPACE=os.getenv('ASTRA_DB_KEYSPACE')
    GROQ_API_KEY=os.getenv('GROQ_API_KEY')
    HUGGINGFACEHUB_API_TOKEN=os.getenv('HUGGINGFACEHUB_API_TOKEN')
    HF_TOKEN=os.getenv('HF_TOKEN')
    EMBEDDING_MODEL="sentence-transformers/all-mpnet-base-v2"
    RAG_MODEL="openai/gpt-oss-120b"
    