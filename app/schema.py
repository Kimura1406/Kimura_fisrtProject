from datetime import datetime
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


class SumRequest(BaseModel):
    a: int
    b: int


class SumResponse(BaseModel):
    result: int


class PingResponse(BaseModel):
    status: str


class HistoryItem(BaseModel):
    id: int
    text: str
    created_at: datetime | None


class HistoryResponse(BaseModel):
    items: list[HistoryItem]
