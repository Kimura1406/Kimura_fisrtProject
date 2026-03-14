from fastapi import APIRouter, Depends, HTTPException, status
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
from app.services.chat_service import ChatServiceError, generate_reply

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    user_message = req.message.strip()
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    try:
        reply = generate_reply(user_message)
    except ChatServiceError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Chat provider request failed.",
        ) from exc

    db.add(Message(text=user_message))
    db.commit()

    return ChatResponse(reply=reply)


@router.post("/sum", response_model=SumResponse)
def sum_number(req: SumRequest):
    result = req.a + req.b
    return SumResponse(result=result)


@router.get("/ping", response_model=PingResponse)
def ping():
    return PingResponse(status="Kimura API is ready")
