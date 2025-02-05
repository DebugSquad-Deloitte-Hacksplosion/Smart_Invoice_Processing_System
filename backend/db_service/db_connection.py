import pyodbc

# Azure SQL Database Configuration
DB_SERVER = "tcp:debug-squad-hacksplosion.database.windows.net,1433"
DB_DATABASE = "Purchase Orders"
DB_USERNAME = "CloudSA6f455c92"
DB_PASSWORD = "MySfG78hgHHtygg3"

def connect_db():
    """Establish a connection with Azure SQL Server."""
    try:
        conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={DB_SERVER};DATABASE={DB_DATABASE};'
        f'UID={DB_USERNAME};PWD={DB_PASSWORD};'
        f'ENCRYPT=yes;TRUSTSERVERCERTIFICATE=no;CONNECTION TIMEOUT=30;'
        )
        return conn
    except pyodbc.Error as e:
        print(f"⚠️ Error connecting to the database: {e}")
        return None
    
