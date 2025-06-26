import PyPDF2

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except PyPDF2.errors.PdfReadError:
        return "Unable to read PDF. Please upload a valid, uncorrupted PDF file."


