# 🛒 Flipkart Recommendation System

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.1.0-yellow.svg)](https://python.langchain.com/)
[![Docker](https://img.shields.io/badge/Docker-20.10-blue.svg)](https://docker.com)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-1.28-purple.svg)](https://kubernetes.io)

A sophisticated RAG (Retrieval-Augmented Generation) based e-commerce recommendation system built with Flask, LangChain, and modern AI/ML components. This system provides intelligent product recommendations and conversational assistance for Flipkart-like e-commerce platforms.

## 📋 Project Description

The Flipkart Recommendation System is an advanced AI-powered chatbot that leverages Retrieval-Augmented Generation (RAG) architecture to provide accurate and context-aware product recommendations. The system processes product reviews and titles, stores them in a vector database, and uses large language models to generate intelligent responses to user queries.

### Key Features

- **🤖 Conversational AI**: Interactive chat interface for product inquiries
- **🔍 RAG Architecture**: Combines retrieval-based and generative AI for accurate responses
- **📊 Real-time Monitoring**: Prometheus integration for system metrics
- **☸️ Kubernetes Ready**: Containerized deployment with Kubernetes manifests
- **📈 Observability**: Grafana dashboards for system visualization
- **🗃️ Vector Database**: AstraDB for efficient similarity search
- **🎯 Context-Aware**: Maintains conversation history for better responses

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐     ┌─────────────────┐
│   User Interface│    │   Flask Backend │     │   Vector Store  │
│   (HTML/JS)     │◄──►│   (app.py)      │◄──► │   (AstraDB)     │
└─────────────────┘    └─────────────────┘     └─────────────────┘
                                │                       │
                                ▼                       ▼
                       ┌─────────────────┐    ┌─────────────────┐
                       │   LLM Service   │    │   Data Pipeline │
                       │   (Groq)        │    │   (CSV → Docs)  │
                       └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Monitoring    │
                       │   (Prometheus)  │
                       └─────────────────┘
```

### Core Components

1. **Data Ingestion Pipeline**: Converts CSV product data into LangChain documents
2. **Vector Store**: AstraDB for semantic search and similarity matching
3. **RAG Chain**: Combines retrieval and generation for intelligent responses
4. **Web Interface**: Flask-based chat interface with real-time communication
5. **Monitoring**: Prometheus metrics collection and Grafana visualization

## 🛠️ Technology Stack

### Backend

- **Python 3.12**: Core programming language
- **Flask**: Web framework for API and web interface
- **LangChain**: LLM orchestration and RAG pipeline
- **LangChain Community**: Extended LangChain functionality
- **LangChain Classic**: Legacy LangChain components

### AI/ML Components

- **Groq LLM**: 

Groq model for response generation
- **HuggingFace Embeddings**: Sentence transformers for text embeddings
- **AstraDB Vector Store**: Apache Cassandra vector database

### Data Processing

- **Pandas**: Data manipulation and CSV processing
- **PyPDF**: PDF document processing (if needed)

### Monitoring & DevOps

- **Prometheus**: Metrics collection and monitoring
- **Grafana**: Data visualization and dashboards
- **Docker**: Containerization
- **Kubernetes**: Orchestration

### Frontend

- **HTML/CSS/JavaScript**: Web interface
- **Bootstrap**: UI framework
- **jQuery**: DOM manipulation and AJAX

## 📋 Prerequisites

Before setting up the project, ensure you have the following installed:

### System Requirements

- Python 3.12 or higher
- Docker and Docker Compose (optional)
- Kubernetes cluster (optional)
- Git

### API Keys and Services

- **Groq API Key**: For LLM inference
- **HuggingFace Hub Token**: For model access
- **AstraDB Credentials**:
  - API Endpoint
  - Application Token
  - Keyspace

### Environment Variables

Create a `.env` file with the following variables:

```bash
# Groq API Configuration
GROQ_API_KEY=your_groq_api_key_here

# HuggingFace Configuration
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
HF_TOKEN=your_hf_token_here

# AstraDB Configuration
ASTRA_DB_API_ENDPOINT=your_astradb_endpoint_here
ASTRA_DB_APPLICATION_TOKEN=your_astradb_token_here
ASTRA_DB_KEYSPACE=your_astradb_keyspace_here
```

## 🚀 Installation and Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Flipkart_Recommendation_System
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Package in Development Mode

```bash
pip install -e .
```

### 5. Set Environment Variables

```bash
cp .env.example .env  # Create from template if available
# Edit .env file with your credentials
```

### 6. Initialize Data (Optional)

```bash
python -c "from flipkart.data_ingestion import DataIngestion; DataIngestion().ingest(load_existing=False)"
```

### 7. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## ⚙️ Configuration

### Application Configuration

The system uses environment variables for configuration defined in [`flipkart/config.py`](flipkart/config.py:1):

```python
class Config():
    ASTRA_DB_API_ENDPOINT = os.getenv('ASTRA_DB_API_ENDPOINT')
    ASTRA_DB_APPLICATION_TOKEN = os.getenv('ASTRA_DB_APPLICATION_TOKEN')
    ASTRA_DB_KEYSPACE = os.getenv('ASTRA_DB_KEYSPACE')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
    HF_TOKEN = os.getenv('HF_TOKEN')
    EMBEDDING_MODEL = "sentence-transformers/all-mpnet-base-v2"
    RAG_MODEL = "openai/gpt-oss-120b"
```

### Model Configuration

- **Embedding Model**: `sentence-transformers/all-mpnet-base-v2`
- **RAG Model**: `openai/gpt-oss-120b` (via Groq)
- **Vector Store**: AstraDB with collection name `flipkart_database`

## 📖 Usage Instructions

### Web Interface

1. Open `http://localhost:5000` in your browser
2. Type your product-related questions in the chat interface
3. Receive AI-powered responses based on product data

### API Usage

The system provides REST API endpoints:

#### Chat Endpoint

```bash
curl -X POST http://localhost:5000/get \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "msg=What are the best headphones under 5000?"
```

#### Metrics Endpoint

```bash
curl http://localhost:5000/metrics
```

### Python API Usage

```python
from flipkart.rag_chain import RagChainBuilder
from flipkart.data_ingestion import DataIngestion

# Initialize the system
vector_store = DataIngestion().ingest(load_existing=True)
rag_chain = RagChainBuilder(vector_store).build_chain()

# Get response
response = rag_chain.invoke(
    {"input": "What are the best headphones?"},
    config={"configurable": {"session_id": "user_session"}}
)
print(response['answer'])
```

## 🔌 API Endpoints

| Endpoint   | Method | Description        | Response Format |
| ---------- | ------ | ------------------ | --------------- |
| `/`        | GET    | Web interface      | HTML            |
| `/get`     | POST   | Chat response      | Plain text      |
| `/metrics` | GET    | Prometheus metrics | Plain text      |

### Request/Response Examples

#### Chat Request

```json
{
  "msg": "What are the best wireless earphones under 3000 rupees?"
}
```

#### Chat Response

```
Based on the product data, some good wireless earphones under 3000 rupees include BoAt Airdopes 141 with good battery life and sound quality.
```

## 🚢 Deployment Options

### Local Development

```bash
python app.py
```

### Docker Deployment

```bash
# Build image
docker build -t flask-app:latest .

# Run container
docker run -p 5000:5000 --env-file .env flask-app:latest
```

### Kubernetes Deployment

```bash
# Apply Kubernetes manifests
kubectl apply -f flask_deployment.yaml
kubectl apply -f prometheus/prometheus-deployment.yaml
kubectl apply -f prometheus/prometheus-configmap.yaml
```

### Production Deployment

1. **Environment Setup**: Configure all required environment variables
2. **Database Setup**: Initialize AstraDB vector store
3. **SSL Configuration**: Set up HTTPS for production
4. **Load Balancing**: Configure load balancer for multiple instances
5. **Monitoring**: Set up Prometheus and Grafana dashboards

## 📊 Monitoring and Observability

### Prometheus Metrics

The system exposes metrics at `/metrics` endpoint:

- `http_request_total`: Total number of HTTP requests
- Response time metrics
- Error rate metrics

### Grafana Dashboard

Configure Grafana to connect to Prometheus for:

- Request volume and trends
- Response time analysis
- Error rate monitoring
- System performance metrics

### Log Management

Logs are stored in the `logs/` directory with timestamps:

- Application logs
- Error logs
- Access logs

## 📁 Project Structure

```
Flipkart_Recommendation_System/
├── app.py                          # Main Flask application
├── requirements.txt               # Python dependencies
├── setup.py                       # Package setup
├── Dockerfile                     # Docker configuration
├── .env                          # Environment variables
├── README.md                     # Project documentation
├── flipkart/                     # Core application modules
│   ├── __init__.py
│   ├── config.py                 # Configuration management
│   ├── data_ingestion.py         # Data processing pipeline
│   ├── data_converter.py         # CSV to document conversion
│   └── rag_chain.py              # RAG chain implementation
├── utils/                        # Utility modules
│   ├── __init__.py
│   ├── custom_exception.py       # Custom exceptions
│   └── logger.py                 # Logging configuration
├── data/                         # Data files
│   └── flipkart_product_review.csv # Product data
├── templates/                    # HTML templates
│   └── index.html               # Chat interface
├── static/                       # Static files
│   └── style.css                # CSS styles
├── logs/                         # Log files
├── prometheus/                   # Monitoring configuration
│   ├── prometheus-deployment.yaml
│   └── prometheus-configmap.yaml
├── graphana/                     # Grafana configuration
│   └── graphana-deployment.yaml
└── flask_deployment.yaml         # Kubernetes deployment
```

## 🤝 Contributing Guidelines

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make your changes and commit them: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request

### Code Standards

- Follow PEP 8 style guidelines
- Include docstrings for all functions and classes
- Write unit tests for new features
- Update documentation as needed

### Testing

```bash
# Run tests (if available)
pytest

# Run linting
flake8 .
black .
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🔗 Related Links

- [LangChain Documentation](https://python.langchain.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [AstraDB Documentation](https://docs.datastax.com/en/astra-db/)
- [Groq API Documentation](https://console.groq.com/)
- [Prometheus Documentation](https://prometheus.io/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

## 📞 Support

For support and questions:

- Create an issue in the GitHub repository
- Check the logs in the `logs/` directory for troubleshooting
- Review the configuration in `flipkart/config.py`

---

**Built with ❤️ using modern AI/ML technologies for intelligent e-commerce recommendations.**
