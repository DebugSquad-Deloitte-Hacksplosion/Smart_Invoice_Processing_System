from db_service.db_connection import connect_db

def fetch_po_details(po_number):
    """Fetch purchase order details from the database."""
    try:
        conn = connect_db()
        if not conn:
            return None
            
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM PurchaseOrders WHERE PO_Number = ?", (po_number,))
        po = cursor.fetchone()
        cursor.close()
        conn.close()
        return po
    except Exception as e:
        print(f"⚠️ Database Error: {e}")
        return None
