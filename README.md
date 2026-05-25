Enterprise AI Knowledge Assistant

An enterprise-grade AI Knowledge Assistant built using Python, Streamlit, ChromaDB, Sentence Transformers, and Google Gemini API.

The system enables users to ask questions against an internal document knowledge base using a Retrieval-Augmented Generation (RAG) pipeline with semantic search, vector embeddings, grounded LLM responses, and hallucination prevention mechanisms.

Features
Enterprise-style RAG architecture
PDF document ingestion
Semantic chunk retrieval
Vector database with ChromaDB
Persistent embedding storage
Duplicate document prevention
Grounded answer generation
Hallucination reduction using retrieval confidence thresholds
Streamlit frontend interface
Source citation display
Modular project architecture
Tech Stack
Python 3.11
Streamlit
ChromaDB
Sentence Transformers
Google Gemini API
PyPDF
LangChain utilities

Project Architecture
Enterprise-AI-Assistant/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .env
│
├── chroma_db/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── components/
│   │   ├── embeddings.py
│   │   ├── llm_helper.py
│   │   └── pdf_loader.py
│   │
│   ├── pipeline/
│   │   └── rag_pipeline.py
│   │
│   └── utils/
│
└── notebooks/
How the System Works
1. Document Ingestion

PDF files placed inside:

data/raw/

are automatically:

loaded
parsed
chunked
embedded
stored in ChromaDB
2. Semantic Retrieval

User queries are converted into vector embeddings and matched against the document embeddings using semantic similarity search.

3. Grounded Generation

Relevant retrieved chunks are passed to Gemini to generate grounded responses strictly based on the retrieved context.

4. Hallucination Prevention

The system uses retrieval confidence thresholds to prevent the LLM from generating answers when relevant information is not found in the knowledge base.

Key Engineering Features
Persistent Vector Database

Embeddings are stored locally using:

chromadb.PersistentClient()

allowing embeddings to persist across application restarts.

Duplicate Prevention

The system tracks already-ingested documents and prevents duplicate embedding generation using:

data/processed/processed_files.txt
Retrieval Confidence Filtering

Similarity thresholds are used to validate retrieval quality before generating responses.

This reduces hallucinations and improves enterprise reliability.

Setup Instructions
1. Clone Repository
git clone <your_repo_url>
cd Enterprise-AI-Assistant
2. Create Virtual Environment
py -3.11 -m venv .venv

Activate environment:

Windows
.\.venv\Scripts\Activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key_here
Running the Application
Streamlit Frontend
streamlit run app.py
Example Use Cases
Enterprise knowledge assistants
Internal documentation copilots
Engineering knowledge retrieval
AI-powered document search
Research assistants
Technical knowledge systems
Example Queries
What are Graph Neural Networks?
Explain surrogate models in crashworthiness prediction.
What are the applications of GNNs in mechanics?
Future Improvements
Multi-document chat history
API deployment with FastAPI
Authentication and access control
Advanced reranking
Metadata filtering
Multi-user support
Cloud deployment
Real-time document ingestion
Learning Outcomes

This project demonstrates practical implementation of:

Retrieval-Augmented Generation (RAG)
LLM orchestration
Vector databases
Embedding pipelines
Semantic search
Grounded AI systems
Hallucination prevention
Enterprise AI workflows
Modular AI application architecture
