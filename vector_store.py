import chromadb


# ChromaDB Configuration

CHROMA_PATH = "chroma_db"
COLLECTION_NAME = "medical_research"


# Create / Load ChromaDB Collection

def get_collection():

    client = chromadb.PersistentClient(
        path=CHROMA_PATH
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )

    return collection


# Add Chunks and Embeddings

def add_documents(collection, chunks, embeddings):

    documents = [
        chunk["text"]
        for chunk in chunks
    ]

    metadatas = [
        {
            "page": chunk["page"]
        }
        for chunk in chunks
    ]

    ids = [
        f"chunk_{index}"
        for index in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )


# Search the Vector Database

def search_collection(collection, query_embedding, n_results=5):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    return results


# Test the Vector Store

if __name__ == "__main__":

    from ingest import extract_text_from_pdf
    from chunking import create_chunks
    from embeddings import load_embedding_model, create_embeddings

    pdf_path = "rheum_meta_1.pdf"

    print("Extracting PDF...")

    pages = extract_text_from_pdf(pdf_path)

    print("Creating chunks...")

    chunks = create_chunks(pages)

    print("Loading embedding model...")

    model = load_embedding_model()

    print("Creating embeddings...")

    embeddings = create_embeddings(
        chunks,
        model
    )

    print("Connecting to ChromaDB...")

    collection = get_collection()

    print("Adding documents to ChromaDB...")

    # Avoid adding the same chunks repeatedly
    if collection.count() == 0:

        add_documents(
            collection,
            chunks,
            embeddings
        )

        print("Documents successfully added.")

    else:

        print(
            f"Collection already contains "
            f"{collection.count()} documents."
        )

    print(
        "\nTotal documents in ChromaDB:",
        collection.count()
    )