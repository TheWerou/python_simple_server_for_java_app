from Order_classes.basic_classes.order_class import Order


class CoffeeOrder(Order):
    def __init__(self, json_):
        super().__init__(json_)
        self.with_milk = json_["with_milk"]

    def change_milk(self, milk):
        self.with_milk = milk

    def get_milk(self):
        return self.with_milk
