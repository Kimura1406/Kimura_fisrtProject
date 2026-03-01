from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db import get_db
from app.models import Message
from app.schema import HistoryResponse
from app.schema import HistoryItem, HistoryResponse

router = APIRouter()


@router.get("/history", response_model=HistoryResponse)
def get_history(
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    messages = (
        db.query(Message)
        .order_by(Message.id.desc())
        .limit(limit)
        .all()
    )
    messages.reverse()

    return HistoryResponse(
         items=[
             HistoryItem(
               id=msg.id,
                text=msg.text,
               created_at=msg.created_at,
             )
             for msg in messages
         ]
      )
