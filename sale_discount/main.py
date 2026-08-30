from discountstrategy import DiscountStategy
from sales import Sales
from diwalistrat import Diwalistrat
from holistrat import Holistrat

diwali = Diwalistrat()
holi = Holistrat()
sales = Sales(diwali)
sales.process()
sales.set_discount(holi)
sales.process()
