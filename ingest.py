from pypdf import PdfReader

pdf_path = "rheum_meta_1.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text + "\n"

print("Total characters:", len(text))

print("\nFirst 2000 characters:\n")
print(text[:2000])