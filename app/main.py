from fastapi import FastAPI
from app.db import Base, engine
from app.routers.chat import router as chat_router
from app.routers.history import router as history_router

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(chat_router)
app.include_router(history_router)


@app.get("/")
def root():
    return {"message": "Xin chào Kimura"}
