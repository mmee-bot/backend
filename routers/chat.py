from fastapi import APIRouter, UploadFile, File, Depends
import services.chat as chat_service
from models.user import User, get_user_data
from models.response import ChatResponse

import uuid

router = APIRouter()

@router.post("/learn", response_model=ChatResponse)
async def chat_user(
    user: User = Depends(get_user_data),
    kakaoTalkFile: UploadFile = File(...)
):
    await chat_service.learn(user, kakaoTalkFile)
    user_uuid = str(uuid.uuid4())
    return ChatResponse(user_key=user_uuid)