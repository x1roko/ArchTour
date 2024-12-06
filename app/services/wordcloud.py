from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from collections import Counter
import io

def normalize_words(words):
    """
    Нормализует слова, оставляя только допустимые формы.
    """
    allowed_words = {"архангельск", "архангельская область"}
    normalized_words = []

    for word in words:
        if word.startswith("арх"):
            # Оставляем только разрешённые слова
            if word in allowed_words:
                normalized_words.append(word)
        else:
            # Оставляем все остальные слова
            normalized_words.append(word)
    
    return normalized_words

def generate_wordcloud_image(search_queries: list[str], reviews: list[str]):
    # Объединение данных
    text_data = ' '.join(search_queries) + ' ' + ' '.join(reviews)
    words = text_data.lower().split()

    # Фильтрация слов
    stop_words = set()  # Добавьте ваши стоп-слова
    filtered_words = [word for word in words if word not in stop_words and len(word) > 2]

    # Применение нормализации
    normalized_words = normalize_words(filtered_words)

    # Подсчет частоты слов
    word_counts = Counter(normalized_words)

    # Генерация облака слов
    bird_mask = np.array(Image.open('bird_shape.png'))
    wordcloud = WordCloud(
        mask=bird_mask,
        background_color='black',
        contour_color='black',
        contour_width=1
    ).generate_from_frequencies(word_counts)

    # Сохранение изображения в память
    image_stream = io.BytesIO()
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(image_stream, format='png', bbox_inches='tight')
    plt.close()

    # Возврат потока
    image_stream.seek(0)
    return image_stream

