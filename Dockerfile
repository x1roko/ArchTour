FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# Указываем команду для запуска приложения
CMD ["uvicorn", "app.main:app", "--host", "localhost", "--port", "8000"]
