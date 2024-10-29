import fitz 
import docx  
from PIL import Image 
import pytesseract  
import os

def extract_text_from_pdf(file_path):
    """Extracts text from a PDF file using PyMuPDF."""
    text = ""
    try:
        pdf_document = fitz.open(file_path)
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text("text")
        pdf_document.close()
    except Exception as e:
        print(f"Error reading PDF file: {e}")
    return text

def extract_text_from_word(file_path):
    """Extracts text from a Word (.docx) file using python-docx."""
    text = ""
    try:
        doc = docx.Document(file_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
    except Exception as e:
        print(f"Error reading Word file: {e}")
    return text

def extract_text_from_image(file_path):
    """Extracts text from an image file using pytesseract."""
    text = ""
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
    except Exception as e:
        print(f"Error reading image file: {e}")
    return text

def extract_text(file_path):
    """Detects the file type and extracts text accordingly."""
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == ".pdf":
        return extract_text_from_pdf(file_path)
    elif file_extension == ".docx":
        return extract_text_from_word(file_path)
    elif file_extension in [".jpg", ".jpeg", ".png"]:
        return extract_text_from_image(file_path)
    else:
        print("Unsupported file type")
        return None

file_path = "help_test.png"
cv_text = extract_text(file_path)
print(cv_text)
