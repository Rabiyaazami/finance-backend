from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Temporary database
users = []
records = []

# User model
class User(BaseModel):
    id: int
    name: str
    email: str
    role: str  # admin / analyst / viewer
    is_active: bool = True

# Record model
class Record(BaseModel):
    id: int
    amount: float
    type: str  # income / expense
    category: str
    date: str
    description: str

# Dashboard summary
@app.get("/summary")
def get_summary():
    total_income = sum(r.amount for r in records if r.type == "income")
    total_expense = sum(r.amount for r in records if r.type == "expense")
    net_balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance
    }

# Category-wise summary
@app.get("/category-summary")
def category_summary():
    result = {}

    for r in records:
        if r.category not in result:
            result[r.category] = 0
        
        result[r.category] += r.amount

    return result

# Root API
@app.get("/")
def read_root():
    return {"message": "Backend is running 🚀"}

# Create user (ONLY ADMIN ALLOWED)
@app.post("/users")
def create_user(user: User, role: str):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create users")
    
    users.append(user)
    return {
        "message": "User created successfully",
        "data": user
    }

# Get all users
@app.get("/users")
def get_users():
    return users

# Create record
@app.post("/records")
def create_record(record: Record, role: str):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create records")
    
    records.append(record)
    return {
        "message": "Record created successfully",
        "data": record
    }

# Get all records
@app.get("/records")
def get_records():
    return records