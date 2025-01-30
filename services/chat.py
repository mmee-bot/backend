from fastapi import UploadFile, File
from models.user import User

async def learn(user: User, kakaoTalkCsv: UploadFile = File(...)):
    kakaoTalkContents = await kakaoTalkCsv.read()
    