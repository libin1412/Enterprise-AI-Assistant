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
