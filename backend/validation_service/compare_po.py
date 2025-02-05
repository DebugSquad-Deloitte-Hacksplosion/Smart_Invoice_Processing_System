import re
from fuzzywuzzy import fuzz
from db_service.fetch_po import fetch_po_details

def extract_po_number(invoice_text):
    """Extracts PO Number using regex-based approach."""
    patterns = [r"PO\s*#?:?\s*(\w+)", r"Purchase\s*Order\s*#?:?\s*(\w+)"]
    
    for pattern in patterns:
        match = re.search(pattern, invoice_text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    return None

def validate_invoice(invoice_text):
    """Validate extracted invoice text against database."""
    if not invoice_text:
        return "🚫 No text could be extracted from invoice."

    po_number = extract_po_number(invoice_text)

    if not po_number:
        return "🚫 PO Number not found in invoice."

    po = fetch_po_details(po_number)
    if not po:
        return f"🚫 No matching PO found in the database for PO Number: {po_number}."

    po_details = str(po[1])  # Assuming PO details are in the second column of the database
    validation_score = fuzz.partial_ratio(po_details, invoice_text)

    threshold = 80

    if validation_score > threshold:
        return f"✅ Invoice Validated! Match Score: {validation_score}%"
    else:
        return f"⚠️ Mismatch Detected! Match Score: {validation_score}%"
