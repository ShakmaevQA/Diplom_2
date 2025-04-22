import pytest
import allure
import requests

from helpers.data import Data
from helpers.urls import CREATE_USER_URL


@allure.suite("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_uni_user(self):
        success_data = Data.create_valid_user()
        response = requests.post(CREATE_USER_URL, data=success_data)
        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert response.json()["success"] is True

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_exists_user(self):
        success_data={
        "email": "petuxfm@yandex.ru",
        "password": "123456",
        "name": "petuxfm@yandex.ru"
    }
        response = requests.post(CREATE_USER_URL, data=success_data)
        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя с незаполненным обязательным полем")
    def test_create_invalid_user(self):
        success_data = Data.create_invalid_user()
        response = requests.post(CREATE_USER_URL, data=success_data)
        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"