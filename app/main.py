from fastapi import FastAPI
from app.routes import router

# Инициализация FastAPI
app = FastAPI()

# Подключение маршрутов
app.include_router(router)

