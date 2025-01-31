from fastapi import UploadFile, File
from io import StringIO
import pandas as pd
from models.user import User

async def learn(user: User, kakaotalk_file: UploadFile = File(...)):
    kakao_read = await kakaotalk_file.read()
    
    kakao_csv = pd.read_csv(
        StringIO(kakao_read.decode("utf-8"))
    )
    
    user_messages = kakao_csv[kakao_csv["User"] == user.name]
    recent_messages = user_messages.sort_values(by="Date", ascending=False).head(30)

    combine = " ".join(recent_messages["Message"].tolist())
    print(combine)
    
