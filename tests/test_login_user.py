import pytest
import allure
import requests

from helpers.urls import LOGIN_USER_URL, GET_USER_URL


@allure.suite("Прохождение авторизации пользователем:")
class TestLogin:

    @allure.title("Логин под существующим пользователем")
    def test_valid_user(self, create_and_delete_user):
        user, token = create_and_delete_user
        headers = {"Authorization": token}
        response = requests.get(GET_USER_URL, headers=headers)
        assert response.status_code == 200

    @allure.title("Логин с неверным логином и паролем")
    def test_invaid_user(self):
        success_data = {
            "email": "пупу",
            "password": "ляля"
        }
        response = requests.post(LOGIN_USER_URL, data=success_data)
        assert response.status_code == 401
        assert response.json()["success"] is False, "Поле success не False"

