from pydantic import BaseModel

class ChatResponse(BaseModel):
    user_key: str