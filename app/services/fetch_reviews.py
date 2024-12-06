import aiohttp
from bs4 import BeautifulSoup

# URL страницы с отзывами
URL = 'https://otzovik.com/reviews/otdih_v_g_arhangelsk_russia/'

# Функция для загрузки страницы с повторными попытками
async def fetch(session, url, retries=3, delay=5):
    for attempt in range(retries):
        try:
            async with session.get(url) as response:
                response.raise_for_status()  # Проверка на успешный статус
                return await response.text()
        except aiohttp.ClientResponseError as e:
            if e.status == 507:  # Если сервер перегружен
                print(f"Сервис временно недоступен. Попытка {attempt + 1} из {retries}. Повтор через {delay} секунд...")
                await asyncio.sleep(delay)
            else:
                print(f"Ошибка клиента: {e}")
                return None
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
    print("Достигнуто максимальное число попыток.")
    return None

# Функция для парсинга отзывов
async def parse_reviews(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        if html is None:
            return []  # Если запрос не удался, возвращаем пустой список

        soup = BeautifulSoup(html, 'html.parser')

        # Поиск всех блоков с отзывами
        reviews = soup.find_all('div', class_='review-body-wrap')
        review_texts = []
        for review in reviews:
            review_text = review.find('div', class_='review-teaser')
            if review_text:
                review_texts.append(review_text.get_text(strip=True))
        
        return review_texts

# Функция для получения отзывов
async def get_reviews_parser():
    reviews = await parse_reviews(URL)
    return reviews
