from sentence_transformers import SentenceTransformer

# Embedding model
MODEL_NAME = "all-MiniLM-L6-v2"


def load_embedding_model():

    return SentenceTransformer(MODEL_NAME)


def create_embeddings(chunks, model=None):

    if not chunks:
        return []

    if model is None:
        model = load_embedding_model()

    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings

# Test the module directly

if __name__ == "__main__":

    from ingest import extract_text_from_pdf
    from chunking import create_chunks

    pdf_path = "rheum_meta_1.pdf"

    pages = extract_text_from_pdf(pdf_path)

    chunks = create_chunks(pages)

    print("Total chunks:", len(chunks))

    print("\nLoading embedding model...")

    model = load_embedding_model()

    print("Embedding model loaded.")

    embeddings = create_embeddings(
        chunks,
        model
    )

    print("\nEmbedding shape:", embeddings.shape)

    print("\nFirst embedding:")
    print(embeddings[0])