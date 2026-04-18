# DevOps Practice Project

A simple full-stack application for learning DevOps concepts like CI/CD, Containerization, and Database Management.

## Project Structure
- `frontend/`: Contains the UI (HTML/JS)
- `backend/`: Contains the API (Python/FastAPI) and SQL scripts

---

## 1. Prerequisites
- Python 3.8+
- MySQL Server (Running on localhost)

---

## 2. Database Setup
1. Log in to your MySQL terminal/client.
2. Run the commands in `backend/init.sql` to create the database and table:
   ```sql
   CREATE DATABASE devops_db;
   ```
   *(The backend code will automatically create the table if it's missing)*

---

## 3. Backend Setup
1. Open a terminal in the `backend` folder.
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure Database (Optional):
   Update the database credentials in `main.py` if your MySQL username/password is different from `root`/`password`.
5. **Run the Backend**:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at: [http://localhost:8000](http://localhost:8000)

---

## 4. Frontend Setup
1. Simply open `frontend/index.html` in any modern web browser.
2. Enter a name and phone number.
3. Click "Submit Data" to send it to the backend.

---

## 5. Testing the API
You can also view the interactive API documentation at:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)