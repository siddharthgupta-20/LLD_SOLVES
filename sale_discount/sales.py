from discountstrategy import DiscountStategy
class Sales:
    def __init__(self,cur_discount:DiscountStategy):
        self.cur_discount = cur_discount
    def set_discount(self,new_discounttype: DiscountStategy):
        self.cur_discount = new_discounttype

    def process(self):
        self.cur_discount.get_discount()