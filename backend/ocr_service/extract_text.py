import pdf2image
import pytesseract
import cv2
import numpy as np

# def extract_invoice_text(pdf_path):
#     """Convert a PDF invoice into an image and extract text using OCR."""
#     try:
#         images = pdf2image.convert_from_path(pdf_path)
#         text = ""
#         for img in images:
#             gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
#             enhanced = cv2.detailEnhance(gray, sigma_s=10, sigma_r=0.15)
#             text += pytesseract.image_to_string(enhanced)
#         return text
#     except Exception as e:
#         print(f"⚠️ OCR Extraction Error: {e}")
#         return ""


def extract_invoice_text(pdf_path):
    """Convert a PDF invoice into an image and extract text using OCR."""
    try:
        images = pdf2image.convert_from_path(pdf_path)
        text = ""
        for img in images:
            # Convert PIL Image to numpy array correctly
            opencv_img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            # Convert to grayscale
            gray = cv2.cvtColor(opencv_img, cv2.COLOR_BGR2GRAY)
            # Now enhance the grayscale image
            enhanced = cv2.detailEnhance(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR), sigma_s=10, sigma_r=0.15)
            text += pytesseract.image_to_string(enhanced)
        return text
    except Exception as e:
        print(f"⚠️ OCR Extraction Error: {e}")
        return ""