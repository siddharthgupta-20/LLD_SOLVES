from burger import  Burger
from pizza import  Pizza

class FoodFactory:
    @staticmethod
    def create_food(food: str):
        if food== "pizza":
            return Pizza()
        if food== "burger":
            return Burger()