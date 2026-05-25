# Enterprise-AI-Assistant/src/components/embeddings.py

from sentence_transformers import SentenceTransformer
import chromadb


# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# Initialize Chroma client
#chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Create or get collection
collection = chroma_client.get_or_create_collection(
    name="enterprise_documents"
)


def generate_embedding(text):
    """
    Generate embedding vector for text.
    """

    embedding = embedding_model.encode(text)

    return embedding.tolist()


def add_documents_to_chroma(documents):
    """
    Add chunked documents into ChromaDB.
    """

    for idx, doc in enumerate(documents):

        embedding = generate_embedding(doc["text"])

        collection.add(
            documents=[doc["text"]],
            embeddings=[embedding],
            metadatas=[
                {
                    "source": doc["source"],
                    "page": doc["page"],
                    "chunk_index": doc["chunk_index"],
                }
            ],
            ids=[f"doc_{idx}"],
        )


def search_documents(query, top_k=3):
    """
    Perform semantic similarity search.
    """

    query_embedding = generate_embedding(query)

    # results = collection.query(
    #     query_embeddings=[query_embedding],
    #     n_results=top_k,
    # )
    results = collection.query(
    query_embeddings=[query_embedding],
    n_results=top_k,
    include=["documents", "metadatas", "distances"]
    )

    return results
