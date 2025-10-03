from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy
import pandas

#....

app = FastAPI()

# Fake in-memory DB
fake_db = []

# Schema
class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users")
def get_users():
    return {"name":"Venu", "age":21, "gender":"Male"}

