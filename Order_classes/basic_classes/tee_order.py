from Data_base.Order_classes.basic_classes.order_class import Order


class TeeOrder(Order):
    def __init__(self, reciver, who_ordered, what_orderd, when_is_meeting, with_sugar=False, with_honey=False, pamper_on=False):
        super().__init__(reciver, who_ordered, what_orderd, when_is_meeting, with_sugar)
        self.with_honey = with_honey
        self.pampers_on = pamper_on

    def change_honey(self, honey):
        self.with_honey = honey

    def change_pampers(self,pampers):
        self.pampers_on = pampers

    def get_honey(self):
        return self.with_honey

    def get_pampers(self):
        return self.pampers_on
