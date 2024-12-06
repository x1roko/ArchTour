import aiohttp
import json

async def get_google_autocomplete(query: str):
    try:
        url = f"https://suggestqueries.google.com/complete/search?client=firefox&q={query}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json(content_type=None)
                    return data[1]  # Возвращаем автозаполнения
    except Exception as e:
        print(f"Ошибка при получении автозаполнений: {e}")
    return []
