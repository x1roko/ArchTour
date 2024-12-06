from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.services.file_loader import load_queries_from_file
from app.services.autocomplete import get_google_autocomplete
from app.services.wordcloud import generate_wordcloud_image
from app.services.fetch_reviews import get_reviews_parser


router = APIRouter()

@router.get("/generate-wordcloud/")
async def generate_wordcloud():
    try:
        # Загрузка запросов из файла
        queries = load_queries_from_file('data/search.txt')

        # Получение автозаполнений
        search_queries = []
        for query in queries:
            suggestions = await get_google_autocomplete(query)
            search_queries.extend(suggestions)

        # Загрузка отзывов
        reviews = await get_reviews_parser()

        # Генерация изображения облака слов
        image_stream = generate_wordcloud_image(search_queries, reviews)

        # Возвращение изображения в виде потока
        return StreamingResponse(image_stream, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка: {e}")
