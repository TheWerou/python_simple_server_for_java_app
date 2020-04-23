from Data_base.Order_classes.basic_classes.order_class import Order


class CoffeeOrder(Order):
    def __init__(self, reciver, who_ordered, what_orderd, when_is_meeting, with_sugar=False, with_milk=False):
        super().__init__(reciver, who_ordered, what_orderd, when_is_meeting, with_sugar)
        self.with_milk = with_milk

    def change_milk(self, milk):
        self.with_milk = milk

    def get_milk(self):
        return self.with_milk
