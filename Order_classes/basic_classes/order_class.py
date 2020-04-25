import json


class Order:
    def __init__(self, dict_to_give):  # reciver, who_ordered, what_orderd, when_is_meeting, with_sugar
        self.reciver = dict_to_give["reciver"]
        self.from_who = dict_to_give["from_who"]
        self.what = dict_to_give["what"]
        self.when = dict_to_give["when"]
        self.with_sugar = dict_to_give["with_sugar"]

    def change_what_orderd(self, new_order):
        self.what = new_order

    def change_time(self, new_time):
        self.check_if_time_good(new_time)

    def check_if_time_good(self, time_to_check):
        if time_to_check[0] < 24 and time_to_check[1] < 60:
            self.when = time_to_check
            return True
        else:
            return False

    def change_sugar(self, sugar):
        self.with_sugar = sugar
