import pdfplumber

def get_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text()
            if page_text:
                # Add page separator for readability
                print(f"--- Page {i} ---")
                text += f"\n\n--- Page {i} ---\n\n"
                text += page_text
    return text

text = get_text("PDF/MusicTheory.pdf")

with open("pdf_text.txt", "w") as f:
    f.write(text)
    
print(text[:2000])