import pdf2image
import pytesseract
import cv2
import numpy as np
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_invoice_text(pdf_path):
    try:
        # Convert PDF to images
        images = pdf2image.convert_from_path(pdf_path)
        text = ""
        

        for img in images:
            # Convert PIL Image to numpy array
            np_img = np.array(img)
            
            # Check if image is already grayscale
            if len(np_img.shape) == 2:
                gray = np_img
            else:
                # Convert to grayscale properly handling BGR or RGB
                if len(np_img.shape) == 3:
                    gray = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
            
            # Image preprocessing
            denoised = cv2.fastNlMeansDenoising(gray)
            thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            
            # OCR
            text += pytesseract.image_to_string(thresh)
        
        return text
    except Exception as e:
        print(f"⚠️ OCR Extraction Error: {e}")
        return ""