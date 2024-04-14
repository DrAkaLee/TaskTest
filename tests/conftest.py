import pytest
import requests
from configuration import SERVICE_URL_GENDER
from configuration import SERVICE_URL_ID

@pytest.fixture
def service_url_gender():
    return SERVICE_URL_GENDER

@pytest.fixture
def service_url_id():
    return SERVICE_URL_ID

@pytest.fixture
def user_ids(service_url_gender):
    response = requests.get(f"{service_url_gender}")
    response.raise_for_status()
    data = response.json()

    return data.get('idList',[])



