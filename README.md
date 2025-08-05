
# 📊 Shareholder Management API - Documentation

This RESTful API built with FastAPI and PostgreSQL allows for the management of shareholders and share issuance. It includes functionalities for both administrators and shareholders.

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/exceldev-237/test_python/tree/test_python
cd your-repo-folder
```

### 2. Set up PostgreSQL Database

Make sure PostgreSQL is installed and running.

```sql
CREATE DATABASE shareholders_db;
```

Update `DATABASE_URL` in `database.py` accordingly:

```python
DATABASE_URL = "postgresql://postgres:root@localhost/shareholders_db"
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 80
```

---

## 🔐 Authentication (JWT)

### `POST /api/token/`

**Login with an administrator or shareholder account.**

- **Request (form-data):**
  - `username`: admin
  - `password`: secret

- **Response:**
```json
{
  "access_token": "<your_token>",
  "token_type": "bearer"
}
```

🔑 Use the returned token in your requests with the `Authorization: Bearer <token>` header.

---

## 👨‍💼 Admin Endpoints

### `GET /api/shareholders/`

List all shareholders with their total shares.  
**(Admin only)**

### `POST /api/shareholders/`

Create a new shareholder.  
**(Admin only)**

- **Body (JSON):**
```json
{
  "name": "excel_sime",
  "email": "excel@gmail.com"
}
```

### `POST /api/issuances/`

Issue shares for a shareholder.  
**(Admin only)**

- **Body (JSON):**
```json
{
  "shareholder_id": 1,
  "shares": 100,
  "price": 50,
  "date": "2025-08-01"
}
```

### `GET /api/issuances/{issuance_id}/certificate/`

Download the share issuance certificate (PDF).  
**(Admin or corresponding shareholder)**

---

## 👤 Shareholder Endpoints

### `GET /api/issuances/`

List only your own share issuances.  
**(Shareholder only)**

---

## 🧪 Test Users

You can use these users for testing:

- **Admin:**
  - `username`: admin
  - `password`: secret

- **Shareholder (after creation):**
  - `username`: excel@gmail.com
  - `password`: any (password test: secret)

---

## 📄 PDF Certificate

PDF files are generated dynamically using ReportLab and include:

- Shareholder name
- Number of shares
- Issue date
- Watermark "Certified"

---

## 🧪 Testing

Test endpoints using tools like  **Thunder** or **Postman** or **curl** with the provided token.

---

Enjoy building 🚀


Développed by Excel SIME (excelsime10@gmail.com) 🧠