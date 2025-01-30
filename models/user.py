from fastapi import Depends, Form
from pydantic import BaseModel
import json

class User(BaseModel):
    name: str
    gender: str
    job: str
    mbti: str

async def get_user_data(user: str = Form(...)) -> User:
    try:
        user_data = json.loads(user)
        return User(**user_data)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON provided for 'user'.")