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
        requests.post(CREATE_ORDER_URL, data=success_data, headers=headers)
        response = requests.get(GET_USER_URL,headers=headers)
        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Не авторизованный пользователь")
    def test_receiveing_order_login(self, create_and_delete_user):
        user, token = create_and_delete_user
        ingredients = Data.create_order_ingredients()
        success_data = {"ingredients": ingredients}
        headers = {'Authorization': f'{token}'}
        requests.post(CREATE_ORDER_URL, data=success_data, headers=headers)
        response = requests.get(GET_USER_URL)
        assert response.status_code == 401
        assert response.json()["success"] is False

