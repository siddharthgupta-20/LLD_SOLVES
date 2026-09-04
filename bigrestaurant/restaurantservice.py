from foodfactory import FoodFactory
class RestaurantService:
    def take_order(self,order:str):
        p = FoodFactory.create_food(order)
        p.prepare()

    