from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- DATABASE CONFIGuration ---
# Replace with your MySQL credentials
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "devops_db")

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# SQLAlchemy Setup
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- DATABASE MODEL ---
class UserSubmission(Base):
    __tablename__ = "submissions"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)

# Create tables in the database
# In a real DevOps flow, we might use migrations (Alembic), but here we keep it simple.
def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")

# --- FASTAPI APP SETUP ---
app = FastAPI(title="DevOps Practice API")

# Enable CORS so frontend (HTML file) can call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- PYDANTIC SCHEMA ---
class SubmissionCreate(BaseModel):
    name: str
    phone: str

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- API ENDPOINTS ---

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Backend is running! Use POST /submit to send data."}

@app.post("/submit")
def create_submission(submission: SubmissionCreate, db: Session = Depends(get_db)):
    try:
        # Create a new record
        new_entry = UserSubmission(name=submission.name, phone=submission.phone)
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)
        return {"status": "success", "id": new_entry.id, "message": "Data saved successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Start the server on port 8000
    uvicorn.run(app, host="0.0.0.0", port=8000)
