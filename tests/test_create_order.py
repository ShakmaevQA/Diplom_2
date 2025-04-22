import pytest
import allure
import requests

from helpers.data import Data
from helpers.urls import CREATE_ORDER_URL


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("С авторизацией")
    def test_create_order_login(self, create_and_delete_user):
        user, token = create_and_delete_user
        ingredients = Data.create_order_ingredients()
        success_data = {"ingredients": ingredients}
        headers = {'Authorization': f'{token}'}
        response = requests.post(CREATE_ORDER_URL, data=success_data, headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Без авторизации")
    def test_create_order_logaut(self):
        ingredients = Data.create_order_ingredients()
        success_data = {"ingredients": ingredients}
        response = requests.post(CREATE_ORDER_URL, data=success_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("С ингридиентами")
    def test_create_order_with_ingredients(self):
        ingredients = Data.create_order_ingredients_more_two()
        success_data = {"ingredients": ingredients}
        response = requests.post(CREATE_ORDER_URL, data=success_data)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Без ингридиентов")
    def test_create_order_without_ingredients(self):
        response = requests.post(CREATE_ORDER_URL)
        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Неверный хэш код")
    def test_create_order_invalid_hash(self):
        # Формируем тело с невалидным хэшем
        payload = {"ingredients": "invalid_hash"}
        response = requests.post(CREATE_ORDER_URL, data=payload)
        print(f"Status: {response.status_code}, Response: {response.text}")  # Отладка
        assert response.status_code == 400, f"Ожидался статус 400, получен {response.status_code}: {response.text}"
        assert "One or more ids provided are incorrect" in response.text, f"Ожидалось 'One or more ids provided are incorrect' в теле ответа: {response.text}"