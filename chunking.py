from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text:
            pages.append({
                "page": page_number,
                "text": text
            })

    return pages


def create_chunks(pages, chunk_size=1000, overlap=200):
    chunks = []

    for page in pages:

        text = page["text"]

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunk_text = text[start:end]

            chunks.append({
                "text": chunk_text,
                "page": page["page"]
            })

            start += chunk_size - overlap

    return chunks

# Test

pdf_path = "rheum_meta_1.pdf"

pages = extract_text_from_pdf(pdf_path)

chunks = create_chunks(pages)

print("Total pages:", len(pages))
print("Total chunks:", len(chunks))

print("\nFirst chunk:\n")
print(chunks[0]["text"])

print("\nPage:", chunks[0]["page"])