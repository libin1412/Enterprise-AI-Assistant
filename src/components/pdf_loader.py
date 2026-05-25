# Enterprise-AI-Assistant/src/components/pdf_loader.py
import os
from typing import List

from pypdf import PdfReader


__all__ = [
    "extract_text_from_pdf",
    "chunk_text",
    "load_pdf_as_chunks",
    "load_pdf_documents",
]


def extract_text_from_pdf(pdf_path: str) -> List[str]:
    """Read a PDF and return a list of page texts."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    reader = PdfReader(pdf_path)
    pages: List[str] = []

    for page_number, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception as exc:
            raise RuntimeError(
                f"Failed to extract text from page {page_number} of {pdf_path}: {exc}"
            ) from exc

        pages.append(text.strip())

    return pages


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """Split text into overlapping chunks for embeddings or retrieval."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    if overlap < 0:
        raise ValueError("overlap must be non-negative")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    normalized = " ".join(text.split())
    if not normalized:
        return []

    chunks: List[str] = []
    start = 0
    while start < len(normalized):
        end = min(len(normalized), start + chunk_size)
        chunk = normalized[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end == len(normalized):
            break
        start += chunk_size - overlap

    return chunks


def load_pdf_as_chunks(
    pdf_path: str,
    chunk_size: int = 1000,
    overlap: int = 200,
    min_chunk_length: int = 50,
) -> List[str]:
    """Load a PDF and return a list of cleaned, overlapping text chunks."""
    pages = extract_text_from_pdf(pdf_path)
    chunks: List[str] = []

    for page_text in pages:
        if not page_text:
            continue

        for chunk in chunk_text(page_text, chunk_size=chunk_size, overlap=overlap):
            if len(chunk) >= min_chunk_length:
                chunks.append(chunk)

    return chunks


def load_pdf_documents(
    pdf_path: str,
    chunk_size: int = 1000,
    overlap: int = 200,
    min_chunk_length: int = 50,
) -> List[dict]:
    """Load a PDF and return document chunks with page-level metadata."""
    pages = extract_text_from_pdf(pdf_path)
    documents: List[dict] = []

    for page_number, page_text in enumerate(pages, start=1):
        if not page_text:
            continue

        for chunk_index, chunk in enumerate(
            chunk_text(page_text, chunk_size=chunk_size, overlap=overlap), start=1
        ):
            if len(chunk) < min_chunk_length:
                continue

            documents.append(
                {
                    "source": os.path.basename(pdf_path),
                    "page": page_number,
                    "chunk_index": chunk_index,
                    "text": chunk,
                }
            )

    return documents


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Load a PDF and optionally print page text or chunks."
    )
    parser.add_argument("pdf_path", help="Path to the PDF file.")
    parser.add_argument("--chunk-size", type=int, default=1000)
    parser.add_argument("--overlap", type=int, default=200)
    parser.add_argument("--min-length", type=int, default=50)
    parser.add_argument("--show-pages", action="store_true")
    parser.add_argument("--show-chunks", action="store_true")
    args = parser.parse_args()

    if args.show_pages:
        pages = extract_text_from_pdf(args.pdf_path)
        for i, page in enumerate(pages, 1):
            print(f"--- Page {i} ---")
            print(page)
            print()

    if args.show_chunks:
        chunks = load_pdf_as_chunks(
            args.pdf_path,
            chunk_size=args.chunk_size,
            overlap=args.overlap,
            min_chunk_length=args.min_length,
        )
        for i, chunk in enumerate(chunks, 1):
            print(f"--- Chunk {i} ---")
            print(chunk)
            print()

    if not args.show_pages and not args.show_chunks:
        chunks = load_pdf_as_chunks(
            args.pdf_path,
            chunk_size=args.chunk_size,
            overlap=args.overlap,
            min_chunk_length=args.min_length,
        )
        print(f"Loaded {len(chunks)} chunks from {args.pdf_path}")
