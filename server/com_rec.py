import os
from server.com_handle import ComHandle


class Comends:
    def __init__(self, users, orders, name):
        self.line_list = []         # line changed to list
        self.type = ""              # type of recived comand
        self.users = users          # list of users
        self.orders = orders        # list of all clients invitations
        self.name = name            # user name

        self.in_comands = {
            "ASK": 1,               # client query {user} (true)
            "CHK": 2,               # Client ask for his invitions (false)
            "NOO": 3,               # 2 client send no (true)
            "AKC": 4,               # invitation aproved  (true)
            "RCV": 5,               # MSG recived ready to be removed
        }
        self.out_comands = {
            "ASK": 1,               # ask other user
            "NOO": 2,               # give back informations
            "AKC": 3,               # Client said yes and gives u what
            "LST": 4,               # Gives nr of invitations
            "WRG": 5,               # Somethink goes wrong
            "SND": 6,               # Send informations

        }

    def rec_comand(self, line):             # method splits string array to single word and saves it to list
        line = line.decode("utf-8")         # decode binary coded line
        list_of_line = line.split()         # from convert string to list
        if len(list_of_line) > 2:
            self.type = "WRG"
            return self.type
        else:
            if len(list_of_line) == 2:
                print("list entry " + str(list_of_line))
                self.check_in_commands(list_of_line)

                return [self.type, list_of_line[1]]

            elif len(list_of_line) == 1:
                print("list entry v2 " + str(list_of_line))
                self.check_in_commands(list_of_line)

                return [self.type]
            else:
                self.type = "WRG"
                return self.type

    def check_in_commands(self, line):      # method check if commend exist in dictionary and handles it
        com_hand = self.object_com_handle()
        if line[0] in self.in_comands:
            self.line_list = line

            if self.in_comands.get(line[0]) is 1:
                self.type = "ASK"
                return com_hand.ask_comand(line)

            elif self.in_comands.get(line[0]) is 2:
                self.type = "CHK"
                return com_hand.chk_command(line)

            elif self.in_comands.get(line[0]) is 3:
                self.type = "NOO"
                return com_hand.noo_comand(line)

            elif self.in_comands.get(line[0]) is 4:
                self.type = "AKC"
                return com_hand.akc_command(line)

            elif self.in_comands.get(line[0]) is 5:
                self.type = "RCV"
                return com_hand.wrg_command(line)
            else:
                self.type = "WRG"
                return com_hand.wrg_command(line)

    def object_com_handle(self):                # method creates object of ComHandle
        comhandl = ComHandle(self.orders, self.name)
        return comhandl

