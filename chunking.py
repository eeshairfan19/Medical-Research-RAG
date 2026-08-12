from ingest import extract_text_from_pdf


def create_chunks(pages, chunk_size=1000, overlap=200):

    if overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")

    chunks = []

    for page in pages:

        text = page["text"]
        page_number = page["page"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append({
                    "text": chunk_text,
                    "page": page_number
                })

            start += chunk_size - overlap

    return chunks

# Test the module directly

if __name__ == "__main__":

    pdf_path = "rheum_meta_1.pdf"

    pages = extract_text_from_pdf(pdf_path)

    chunks = create_chunks(pages)

    print("Total pages:", len(pages))
    print("Total chunks:", len(chunks))

    if chunks:
        print("\nFirst chunk:")
        print(chunks[0]["text"])

        print("\nSource page:", chunks[0]["page"])