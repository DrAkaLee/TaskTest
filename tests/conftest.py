import pytest
import requests

# Импортируем константы URL из модуля configuration, которые указывают на конкретные эндпоинты API
from configuration import SERVICE_URL_GENDER
from configuration import SERVICE_URL_ID

@pytest.fixture    # Фикстура pytest, возвращающая URL для API, который возвращает список пользователей
def service_url_gender():
    return SERVICE_URL_GENDER
    
@pytest.fixture    # Фикстура pytest, возвращающая URL для API, который возвращает данные пользователей по ID
def service_url_id():
    return SERVICE_URL_ID

@pytest.fixture
def user_ids(service_url_gender):
    response = requests.get(f"{service_url_gender}")    # Отправляем GET-запрос на URL, предоставленный фикстурой service_url_gender
    response.raise_for_status()
    data = response.json()     # Преобразуем ответ из формата JSON в Python объект

    return data.get('idList', [])        # Возвращаем список ID пользователей, полученный из ключа 'idList' в ответе JSON
                                         # Если ключ 'idList' отсутствует, возвращаем пустой список
