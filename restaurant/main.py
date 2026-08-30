from chef import Chef
from waiter import Waiter
from pizza_order import PizzaOrder
from burger_order import BurgerOrder

chef = Chef()
waiter = Waiter()

burger = BurgerOrder(chef)
Pizza = PizzaOrder(chef)

waiter.takeorder(burger)
waiter.takeorder(Pizza)