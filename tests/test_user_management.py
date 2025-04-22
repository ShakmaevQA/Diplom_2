import pytest
import allure
import requests

from helpers.data import Data
from helpers.urls import CHANGING_USER_URL


@allure.suite("Изменение данных пользователя")
class TestUserManagement:

    @allure.title("С авторизацией: email")
    def test_changind_with_email(self, create_and_delete_user):
        user, token = create_and_delete_user
        success_data = {
            "email": user["email"]
        }
        headers = {'Authorization': f'{token}'}
        response = requests.patch(CHANGING_USER_URL, data=success_data, headers=headers)
        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert response.json()["success"] is True, "Поле success не True"

    @allure.title("C авторизацией: password")
    def test_changind_with_password(self, create_and_delete_user):
        user, token = create_and_delete_user
        success_data = {
            "password": user["password"]
        }
        headers = {'Authorization': f'{token}'}
        response = requests.patch(CHANGING_USER_URL, data=success_data, headers=headers)
        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert response.json()["success"] == True, "Поле success не True"

    @allure.title("C авторизацией: name")
    def test_changind_with_name(self, create_and_delete_user):
        user, token = create_and_delete_user
        success_data = {
            "name": user["name"]
        }
        headers = {'Authorization': f'{token}'}
        response = requests.patch(CHANGING_USER_URL, data=success_data, headers=headers)
        assert response.status_code == 200, f"Ошибка: {response.text}"
        assert response.json()["success"] is True, "Поле success не True"

    @allure.title("Без авторизациии: email")
    def test_logaut_changind_with_email(self):
        success_data = {
            "email": Data.create_email_user()
        }
        response = requests.patch(CHANGING_USER_URL, data=success_data)
        assert response.status_code == 401, f"Ошибка: {response.text}"
        assert response.json()["message"] == "You should be authorised", "Поле 'message' не 'You should...'"

    @allure.title("Без авторизациии: password")
    def test_logaut_changind_with_password(self):
        success_data = {
            "password": "Пупа"
        }
        response = requests.patch(CHANGING_USER_URL, data=success_data)
        assert response.status_code == 401, f"Ошибка: {response.text}"
        assert response.json()["message"] == "You should be authorised", "Поле 'message' не 'You should...'"

    @allure.title("Без авторизациии: password")
    def test_logaut_changind_with_name(self):
        success_data = {
            "name": "Пупа"
        }
        response = requests.patch(CHANGING_USER_URL, data=success_data)
        assert response.status_code == 401, f"Ошибка: {response.text}"
        assert response.json()["message"] == "You should be authorised", "Поле 'message' не 'You should...'"
