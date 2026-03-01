from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone

from .db import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    created_at = Column(
        DateTime,
        default=lambda: datetime.now(timezone.utc)
    )