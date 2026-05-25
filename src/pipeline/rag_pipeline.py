# Enterprise-AI-Assistant/src/pipeline/rag_pipeline.py

import os

from ..components.pdf_loader import load_pdf_documents
from ..components.embeddings import (
    add_documents_to_chroma,
    search_documents,
)
from ..components.llm_helper import generate_response


RAW_DATA_PATH = "data/raw"

PROCESSED_FILES_PATH = "data/processed/processed_files.txt"


def load_processed_files():

    if not os.path.exists(PROCESSED_FILES_PATH):
        return set()

    with open(PROCESSED_FILES_PATH, "r") as f:
        return set(line.strip() for line in f)


def mark_file_as_processed(file_name):

    with open(PROCESSED_FILES_PATH, "a") as f:
        f.write(file_name + "\n")


def ingest_documents():

    processed_files = load_processed_files()

    all_documents = []

    for file_name in os.listdir(RAW_DATA_PATH):

        if not file_name.endswith(".pdf"):
            continue

        if file_name in processed_files:

            print(f"\nSkipping already processed file: {file_name}")

            continue

        pdf_path = os.path.join(RAW_DATA_PATH, file_name)

        print(f"\nProcessing: {file_name}")

        documents = load_pdf_documents(pdf_path)

        print(f"Created {len(documents)} chunks")

        all_documents.extend(documents)

        mark_file_as_processed(file_name)

    if not all_documents:

        print("\nNo new documents to ingest.")

        return

    print(f"\nTotal new chunks created: {len(all_documents)}")

    add_documents_to_chroma(all_documents)

    print("\nDocuments stored in ChromaDB.")


# def retrieve_context(query, top_k=3):

#     results = search_documents(query, top_k=top_k)

#     retrieved_chunks = results["documents"][0]

#     context = "\n\n".join(retrieved_chunks)

#     return context
def retrieve_context(query, top_k=3):

    results = search_documents(query, top_k=top_k)

    retrieved_chunks = results["documents"][0]

    distances = results["distances"][0]

    metadatas = results["metadatas"][0]

    return {
        "chunks": retrieved_chunks,
        "distances": distances,
        "metadatas": metadatas
    }

# def ask_rag(question):

#     context = retrieve_context(question)

#     if not context.strip():

#         return {
#             "answer": (
#                 "The requested information is not available in the current "
#                 "knowledge base. Please contact the support team or refer to "
#                 "official documentation."
#             ),
#             "sources": []
#         }

#     prompt = f"""
#     You are an enterprise AI assistant.

#     STRICT RULES:
#     - Answer ONLY using the provided context.
#     - Do NOT use external knowledge.
#     - If the answer is not clearly available in the context,
#       respond with:
#       'The requested information is not available in the current knowledge base.'

#     Context:
#     {context}

#     User Question:
#     {question}
#     """

#     response = generate_response(prompt)

#     return {
#         "answer": response,
#         "sources": context
#     }

def ask_rag(question):

    retrieval_result = retrieve_context(question)

    chunks = retrieval_result["chunks"]

    distances = retrieval_result["distances"]

    metadatas = retrieval_result["metadatas"]

    # Safety threshold
    BEST_DISTANCE_THRESHOLD = 1.2

    best_distance = min(distances) if distances else None

    if best_distance is None or best_distance > BEST_DISTANCE_THRESHOLD:

        return {
            "answer": (
                "The requested information is not available "
                "in the current knowledge base. "
                "Please contact the support team or refer "
                "to official documentation."
            ),
            "sources": [],
            "distances": []
        }

    context = "\n\n".join(chunks)

    prompt = f"""
    You are an enterprise AI assistant.

    STRICT RULES:
    - Answer ONLY using the provided context.
    - Do NOT use external knowledge.
    - If the answer is not clearly available in the context,
      say the information is unavailable.

    Context:
    {context}

    User Question:
    {question}
    """

    response = generate_response(prompt)

    return {
        "answer": response,
        "sources": metadatas,
        "distances": distances
    }


def run_rag_pipeline():

    ingest_documents()

    question = "Who are the members of BTS boy band?"

    result = ask_rag(question)

    print("\n FINAL ANSWER:\n")

    print(result["answer"])

    print("\n SOURCES:\n")

    print(result["sources"])

    print("\n DISTANCES:\n")

    print(result["distances"])