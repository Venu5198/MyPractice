from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

# Fake in-memory DB
fake_db = []

# Schema
class User(BaseModel):
    id: int
    name: str
    email: EmailStr  # Better validation for email

@app.get("/users", response_model=List[User])
def get_users():
    return fake_db

@app.post("/users", response_model=User)
def add_user(user: User):
    # Check if user ID already exists
    for existing_user in fake_db:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail="User ID already exists")
    fake_db.append(user)
    return user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in fake_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in fake_db:
        if user.id == user_id:
            fake_db.remove(user)
            return {"message": f"User {user_id} deleted"}
    raise HTTPException(status_code=404, detail="User not found")
