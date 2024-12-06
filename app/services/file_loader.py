from fastapi import HTTPException

def load_queries_from_file(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            queries = [line.strip() for line in file if line.strip()]
        return queries
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Файл {file_path} не найден")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при чтении файла: {e}")
