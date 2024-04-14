import requests

from configuration import SERVICE_URL_GENDER
from configuration import SERVICE_URL_ID

from src.classes.response import Response
from src.schemas.GenderResponse import GenderResponse_SCHEMA



def test_getting_gender():
    r = requests.get(url=SERVICE_URL_GENDER)
    response = Response(r)
    response.assert_status_code(200).validate(GenderResponse_SCHEMA)

def test_gender_for_ids(user_ids, service_url_id):
    valid_genders = ['male']
    errors = []

    for id in user_ids:
        url = f"{service_url_id}/{id}"
        response = requests.get(url)
        response_wrapper = Response(response)
        response_wrapper.assert_status_code(200)
        gender_data = response_wrapper.response_json

        if 'user' not in gender_data:
            errors.append(f"Ответ не содержит 'user' для ID {id}: {gender_data}")
            continue

        user_data = gender_data['user']
        if 'gender' not in user_data:
            errors.append(f"Ответ в 'user' не содержит 'gender' для ID {id}: {user_data}")
            continue

        if user_data['gender'] not in valid_genders:
            errors.append(f"Гендер c ID {id} не соответствует ожидаемым значениям: {user_data['gender']}")
    if errors:
        error_messages = "\n".join(errors)
        assert False, f"Были обнаружены следующие ошибки в данных:\n{error_messages}"

    # for id in user_ids:
    #     url = f"{service_url_id}/{id}"
    #     response = requests.get(url)
    #     response_wrapper = Response(response)
    #     response_wrapper.assert_status_code(200)
    #     gender_data = response_wrapper.response_json
    #
    #     assert 'user' in gender_data, f"Ответ не содержит 'user': {gender_data}"
    #     user_data = gender_data['user']
    #     assert 'gender' in user_data, f"Ответ в 'user' не содержит 'gender': {user_data}"
    #     assert user_data['gender'] == 'male', f"Гендер c ID {id} не male"

