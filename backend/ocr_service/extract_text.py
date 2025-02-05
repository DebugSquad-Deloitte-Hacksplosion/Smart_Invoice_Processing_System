import pdf2image
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_invoice_text(pdf_path):
    """Extract text from an invoice PDF using OCR."""
    try:
        # Convert PDF to images
        images = pdf2image.convert_from_path(pdf_path)
        text = ""

        for img in images:
            np_img = np.array(img)

            if len(np_img.shape) == 2:
                gray = np_img
            else:
                gray = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)

            # Image preprocessing
            denoised = cv2.fastNlMeansDenoising(gray)
            thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            
            # OCR
            text += pytesseract.image_to_string(thresh)
        
        return text.strip()
    except Exception as e:
        print(f"⚠️ OCR Extraction Error: {e}")
        return ""
