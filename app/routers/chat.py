from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Message
from app.schema import (
    ChatRequest,
    ChatResponse,
    PingResponse,
    SumRequest,
    SumResponse,
)

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    user_message = req.message.strip()

    # mock trả lời (chưa dùng AI)
    reply = f"Bạn vừa nói: {user_message}"

    if user_message:
        db.add(Message(text=user_message))
        db.commit()

    return ChatResponse(reply=reply)


@router.post("/sum", response_model=SumResponse)
def sum_number(req: SumRequest):
    result = req.a + req.b
    return SumResponse(result=result)


@router.get("/ping", response_model=PingResponse)
def ping():
    return PingResponse(status="Kimura đã check server nhận chat thành công")
