# 🧾 SIPS (Smart Invoice Processing System)  
**Automating invoice validation with OCR & AI-driven PO matching**  

🚀 **Developed with love by Team DebugSquad ❤️**  

---

## 📌 Project Overview  
The **Invoice Processing & Validation System** is a powerful automation solution designed to fetch invoices from email, extract details using OCR, and validate them against Purchase Orders (POs) stored in a database. This ensures seamless invoice verification, reducing manual effort and improving financial accuracy.

> **Pain Point:** Manual invoice validation is time-consuming, error-prone, and inefficient.  
> **Our Solution:** A fully automated pipeline that extracts, processes, and validates invoices effortlessly.

---

## 🛠️ Tech Stack  
| Component           | Technology Used        |
|--------------------|----------------------|
| **Frontend**       | Angular JS |
| **Backend**        | Python (FastAPI for APIs) |
| **Database**       | Azure SQL Server |
| **OCR Engine**     | Google Document Ai |
| **Automation**     | Email Processing (IMAP, SMTP), RPA Automation (Ui Path) |
| **Cloud**         | Microsoft Azure Services |

---

## 📌 Features & Functionality  
### ✅ **Core Features**  
- 📩 **Fetch invoices** from an email inbox (IMAP protocol)  
- 🖼️ **Extract text** from invoice PDFs using OCR  
- 🔍 **Compare extracted data** with POs stored in the database  
- ✅ **Validate invoices** based on pre-set matching criteria  
- 📝 **Store and retrieve validation logs** for audit purposes  

### 🔥 **Upcoming Features**
- 🌐 Full **Angular UI** integration  
- 🤖 AI-based **PO matching with NLP**  
- 📊 **Dashboard for analytics & reporting**  
- 🔄 **Multi-cloud compatibility (Azure & AWS RDS)**
- 📧 **Email monitoring with RPA** 

---

## 🚀 Installation & Setup  

### **1️⃣ Clone the Repository**  
```shell
git clone https://github.com/your-repo/invoice-processing.git
cd invoice-processing
```

### **2️⃣ Setup Virtual Environment (Recommended)**
```shell
python -m venv env
source env/bin/activate  # MacOS/Linux
env\Scripts\activate      # Windows
```

### **3️⃣ Install Dependencies**
```shell
pip install -r requirements.txt
```

### **4️⃣ Configure Environment Variables**

Set up your .env file inside the project root with:

```
EMAIL_USER=<your-email>
EMAIL_PASSWORD=<your-app-password>
IMAP_SERVER=<your-imap-server>
SQL_SERVER=<azure-sql-server-url>
SQL_USER=<db-username>
SQL_PASSWORD=<db-password>
```

## 🏗️ Project Structure
```
📂 project_root/
│── 📂 backend/
│   ├── 📂 email_service/         # Email fetching service
│   │   ├── fetch_email.py
│   ├── 📂 ocr_service/           # OCR processing
│   │   ├── extract_text.py
│   ├── 📂 db_service/            # Database connection & PO fetching
│   │   ├── db_connection.py
│   │   ├── fetch_po.py
│   ├── 📂 validation/            # Invoice validation logic
│   │   ├── compare_po.py
│── 📂 invoices/                  # Folder to store fetched invoices
│── main.py                        # Core processing script
│── streamlit_app.py                # UI for demo purposes
│── requirements.txt                # Required dependencies
│── README.md                       # Project documentation

```

## Project Workflow
![image](https://github.com/user-attachments/assets/8ad158f9-0944-439d-b0c8-b1cbf8e895ec)

## Advanced Workflow
![image](https://github.com/user-attachments/assets/b6702475-6b70-4aa8-bac7-379d897dde05)


## 🖥️ How to Use

### **🔹 1. Start the Application (Demo Mode)**
```shell
streamlit run streamlit_app.py
```
This will open the Streamlit UI in your browser.
### **🔹 2. Fetch Invoices from Email**
- Click on **"Fetch Invoice from Email"** to download invoice PDFs.
- Extracted invoices are stored in the /invoices folder.
### **🔹 3. Process & Validate Invoices**
- Click **"Extract Text from Invoice"** to run OCR and extract data.
- Click **"Validate Invoice"** to compare extracted text with PO data from the database.
### **🔹 4. View Validation Results**
- The system will display whether the invoice **matches** or **mismatches** the PO (Purchase Orders).
- Logs can be saved for auditing.

## 📸 Screenshorts

### Login Page
![Login](https://github.com/user-attachments/assets/b0dde8f4-f9b6-4b2c-a601-3651ee98c81b)

### Dashboard
![Dashboard](https://github.com/user-attachments/assets/18d3d328-3548-440b-9de6-9131ece17f36)

### Upload Invoice
![Upload Invoice](https://github.com/user-attachments/assets/9a3bf192-c6a5-41a3-b831-123102c986aa)

### Invoice Details
![Invoice Details](https://github.com/user-attachments/assets/56ee1ed1-41bd-4c83-845f-04e7536b7013)

### Email Processing
![Email Processing](https://github.com/user-attachments/assets/cfff48f3-4e3b-4554-9097-42bb8135e6a0)

### Purchase Order Database
![PO DB](https://github.com/user-attachments/assets/812e43b5-cb70-4251-86a6-fa6ba9e4b942)

### Settings Page
![Setting](https://github.com/user-attachments/assets/feff7897-cab1-4a36-ab0c-a467d15b1029)

## 🛠️ Troubleshootin

Common issues and their solutions for the application.

### Known Issues

|Issue                       |             Solution |
|--------------------|----------------------|
|Emails not fetching?         | Ensure IMAP is enabled for your email account & correct credentials are in .env|
|OCR not working?             | Install Tesseract OCR (sudo apt install tesseract-ocr for Ubuntu)|
|Database connection failing? | Verify Azure SQL Server settings & allow firewall access|
|App crashes on validation?   | Check logs and ensure PO data exists in the database|

### 📄 Additional Information
For more detailed troubleshooting steps or if you encounter issues not listed above, please:
1. Check the application logs
2. Verify your environment configuration
3. Contact the development team if issues persist

### ⚙️ Requirements

- IMAP-enabled email account
- Tesseract OCR (for document processing)
- Azure SQL Server access
- Valid .env configuration

### 💁‍♂️ Support
If you need additional assistance, please create an issue in the repository or contact the support team.

Feel free to contribute to this guide by submitting pull requests! 🚀


## 🛡️ Security & Best Practices

- ✅ Use environment variables for storing credentials (.env file)
- ✅ Do not hardcode sensitive information in source code
- ✅ Implement logging & error handling for debugging
- ✅ Restrict database access to specific IPs for security

## 📢 Future Enhancements

- 🔹 Full Angular Frontend
- 🔹 REST API for integration with other systems
- 🔹 AI-based fraud detection for invoice discrepancies
- 🔹 Multi-user authentication & role-based access control

# ❤️ Made with Love by Team DebugSquad
Our mission is to build scalable, production-ready automation solutions to streamline financial workflows.
🔥 If you like this project, give it a ⭐ on GitHub!
