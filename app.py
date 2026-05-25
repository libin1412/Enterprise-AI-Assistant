# Enterprise-AI-Assistant/app.py

import streamlit as st

from src.pipeline.rag_pipeline import (
    ingest_documents,
    ask_rag,
)


st.set_page_config(
    page_title="Enterprise AI Assistant",
    layout="wide"
)


st.title("Enterprise AI Knowledge Assistant")

st.markdown(
    "Ask questions based on the enterprise knowledge base."
)


# Run ingestion once
if "ingested" not in st.session_state:

    ingest_documents()

    st.session_state.ingested = True


question = st.text_input(
    "Enter your question:"
)


if st.button("Ask AI Assistant"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Generating answer..."):

            result = ask_rag(question)

        st.subheader("Answer")

        st.write(result["answer"])

        st.subheader("Sources")

        if result["sources"]:

            for source in result["sources"]:

                st.markdown(
                    f"""
                    - **File:** {source['source']}
                    - **Page:** {source['page']}
                    - **Chunk:** {source['chunk_index']}
                    """
                )

        else:

            st.write("No relevant sources found.")