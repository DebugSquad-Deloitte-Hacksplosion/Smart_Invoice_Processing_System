import imaplib
import email
from email.header import decode_header
import os
from datetime import datetime

def fetch_invoice_email():
    EMAIL_USER = "manojkprdev@gmail.com"
    EMAIL_PASS = "oigvttknbrhxjfkc"
    IMAP_SERVER = "imap.gmail.com"
    INVOICE_FOLDER = "./invoices"
    os.makedirs(INVOICE_FOLDER, exist_ok=True)

    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

        _, search_data = mail.search(None, 'SUBJECT "invoice"')
        email_ids = search_data[0].split()

        if not email_ids:
            return None

        for email_id in reversed(email_ids):
            _, msg_data = mail.fetch(email_id, "(RFC822)")
            email_body = msg_data[0][1]
            msg = email.message_from_bytes(email_body)

            for part in msg.walk():
                if part.get_content_type() == "application/pdf":
                    filename = part.get_filename()
                    if filename:
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        safe_filename = f"invoice_{timestamp}.pdf"
                        filepath = os.path.join(INVOICE_FOLDER, safe_filename)
                        
                        with open(filepath, "wb") as f:
                            f.write(part.get_payload(decode=True))
                        return filepath

        return None
    except Exception as e:
        print(f"⚠️ Email Fetching Error: {e}")
        return None
    finally:
        try:
            mail.logout()
        except:
            pass                                                                                                                                    