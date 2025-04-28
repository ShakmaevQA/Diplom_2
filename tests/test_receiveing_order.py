import pytest
import allure
import requests

from helpers.data import Data
from helpers.urls import CREATE_ORDER_URL, GET_USER_URL


@allure.suite("Получение заказов конкретного пользователя")
class TestReceiveingOrder:

    @allure.title("Авторизованный пользователь")
    def test_receiveing_order_login(self, create_and_delete_user):
        user, token = create_and_delete_user
        ingredients = Data.create_order_ingredients()
        success_data = {"ingredients": ingredients}
        headers = {'Authorization': f'{token}'}
        with allure.step(f"POST запрос на {CREATE_ORDER_URL} для создания заказа"):
            requests.post(CREATE_ORDER_URL, data=success_data, headers=headers)
        with allure.step(f"GET запрос на {GET_USER_URL} с авторизацией"):
            response = requests.get(GET_USER_URL, headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Не авторизованный пользователь")
    def test_receiveing_order_logout(self, create_and_delete_user):
        user, token = create_and_delete_user
        ingredients = Data.create_order_ingredients()
        success_data = {"ingredients": ingredients}
        headers = {'Authorization': f'{token}'}
        with allure.step(f"POST запрос на {CREATE_ORDER_URL} для создания заказа"):
            requests.post(CREATE_ORDER_URL, data=success_data, headers=headers)
        with allure.step(f"GET запрос на {GET_USER_URL} без авторизации"):
            response = requests.get(GET_USER_URL)
        assert response.status_code == 401
        assert response.json()["success"] is False