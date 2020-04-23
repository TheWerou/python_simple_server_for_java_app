

class Order:
    def __init__(self, reciver, who_ordered, what_orderd, when_is_meeting, with_sugar):
        self.__reciver = reciver
        self.__who = who_ordered
        self.what = what_orderd
        self.with_sugar = with_sugar

        if self.check_if_time_good(when_is_meeting):
            self.when = [when_is_meeting[0], when_is_meeting[1]]  # hour , min
        else:
            raise Exception("when is meeting is not corect number")

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
