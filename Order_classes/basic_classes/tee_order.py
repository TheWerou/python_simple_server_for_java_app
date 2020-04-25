from Order_classes.basic_classes.order_class import Order


class TeeOrder(Order):
    def __init__(self, json_):
        super().__init__(json_)
        self.with_honey = json_["with_honey"]

    def change_honey(self, honey):
        self.with_honey = honey

    def get_honey(self):
        return self.with_honey


