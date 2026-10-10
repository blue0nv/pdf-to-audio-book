from PyPDF2 import PdfReader

def extract_pages(path):
    reader = PdfReader(path)

    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)

    return pages

