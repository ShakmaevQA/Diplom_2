import random

class Data:
    bases = ["ninja", "shadow", "ghost", "dragon", "tiger", "wolf", "storm", "fire"]
    ingredients = ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6c"]

    @staticmethod
    def create_name_user():
        name = f"{random.choice(Data.bases)}{random.randint(100, 9999)}"
        return name

    @staticmethod
    def create_order_ingredients():
        ingredients = f"{random.choice(Data.ingredients)}"
        return ingredients

    @staticmethod
    def create_order_ingredients_more_two():
        ingredient = Data.create_order_ingredients()
        extended_ingredients = [ingredient, "61c0c5a71d1f82001bdaaa73"]
        return extended_ingredients

    @staticmethod
    def create_invalid_order_ingredients():
        ingredients = {[f"{random.choice(Data.ingredients)}1"]}
        return ingredients

    @staticmethod
    def create_email_user():
        email = f"{random.choice(Data.bases)}{random.randint(100, 9999)}@mail.ru"

        return email

    @staticmethod
    def create_valid_user():
        result = {
            "email": Data.create_email_user(),
            "password": "testpassword",
            "name": Data.create_name_user()
        }
        return result

    @staticmethod
    def create_invalid_user():
        result = {
            "email": Data.create_email_user(),
            "password": "asdfasdfsad"
        }
        return result






