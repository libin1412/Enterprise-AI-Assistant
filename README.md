# 🚀 Enterprise AI Knowledge Assistant

An enterprise-grade AI Knowledge Assistant built using:

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- Google Gemini API

The system enables users to ask questions against an internal document knowledge base using a Retrieval-Augmented Generation (RAG) pipeline with semantic search, vector embeddings, grounded LLM responses, and hallucination prevention mechanisms.

---

# 🌟 Features

- 📄 PDF document ingestion
- 🧠 Semantic chunk retrieval
- 🗂 Vector database using ChromaDB
- 💾 Persistent embedding storage
- 🚫 Duplicate document prevention
- 🤖 Grounded answer generation
- 🛡 Hallucination prevention
- 🔍 Retrieval confidence filtering
- 🖥 Streamlit frontend interface
- 📚 Source citation display
- 🏗 Modular project architecture

---

# 🛠 Tech Stack

- Python 3.11
- Streamlit
- ChromaDB
- Sentence Transformers
- Google Gemini API
- PyPDF
- LangChain utilities

---

# 📂 Project Structure

```bash
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
 
# ⚙️ How the System Works
1️⃣ Document Ingestion

PDF files placed inside:

data/raw/

are automatically:

loaded
parsed
chunked
embedded
stored in ChromaDB
2️⃣ Semantic Retrieval

User queries are converted into vector embeddings and matched against stored document embeddings using semantic similarity search.

3️⃣ Grounded Generation

Relevant retrieved chunks are passed to Gemini to generate grounded responses strictly based on retrieved context.

4️⃣ Hallucination Prevention

Similarity threshold filtering is used to prevent the LLM from generating responses when relevant context is unavailable.

# 🔑 Key Engineering Features
# 💾 Persistent Vector Database

Embeddings are stored locally using:

chromadb.PersistentClient()

allowing persistence across application restarts.

# 🚫 Duplicate Prevention

Already processed files are tracked using:

data/processed/processed_files.txt

to avoid duplicate embeddings.

# 🛡 Retrieval Confidence Filtering

Similarity thresholds validate retrieval quality before passing context to the LLM.

This reduces hallucinations and improves enterprise reliability.

# 🎯 Example Use Cases
Enterprise knowledge assistants
Internal documentation copilots
Engineering knowledge retrieval
AI-powered document search
Research assistants
Technical knowledge systems

# 🔮 Future Improvements
Multi-document chat history
FastAPI deployment
Authentication and access control
Advanced reranking
Metadata filtering
Cloud deployment
Multi-user support

# 📚 Learning Outcomes

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

