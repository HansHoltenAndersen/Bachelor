import PyPDF2

def count_normalsider_from_pdf(pdf_path):
    # Read PDF
    reader = PyPDF2.PdfReader(pdf_path)
    
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    # Count characters including spaces
    num_chars = len(text)

    # Normalsider (2400 chars per page)
    normalsider = num_chars / 2400

    return num_chars, normalsider


if __name__ == "__main__":
    pdf_path = "Bachelorprojekt (12).pdf"   # <-- replace with your file name
    
    num_chars, normalsider = count_normalsider_from_pdf(pdf_path)

    print(f"Characters (incl. spaces): {num_chars}")
    print(f"Normalsider (chars/2400): {normalsider:.2f}")