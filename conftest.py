import pytest
import allure
import requests
from helpers.urls import CREATE_USER_URL, LOGIN_USER_URL, DELETE_USER_URL
from helpers.data import Data


@pytest.fixture
def create_and_delete_user():
    user = Data.create_valid_user()
    with allure.step(f"POST запрос на {CREATE_USER_URL} для создания пользователя"):
        requests.post(CREATE_USER_URL, data=user)
    with allure.step(f"POST запрос на {LOGIN_USER_URL} для авторизации пользователя"):
        login_response = requests.post(LOGIN_USER_URL, data={
            "email": user["email"],
            "password": user["password"]
        })
    token = login_response.json()["accessToken"]
    headers = {'Authorization': f'{token}'}
    yield user, token
    with allure.step(f"DELETE запрос на {DELETE_USER_URL} для удаления пользователя"):
        requests.delete(f"{DELETE_USER_URL}", headers=headers)