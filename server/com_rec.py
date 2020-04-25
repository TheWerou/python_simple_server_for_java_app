import os


class Comends:
    def __init__(self, users, orders,send):
        self.line_list = []
        self.type = ""
        self.users = users
        self.orders = orders
        self.sendline = send
        self.name = "none"

        self.in_comands = {
            "ASK": 1,  # client query {user} (true)
            "CHK": 2,  # Client ask for his invitions (false)
            "NOO": 3,  # 2 client send no (true)
            "AKC": 4,  # invitation aproved  (true)
            "RCV": 5,  # MSG recived ready to be removed
        }
        self.out_comands = {
            "ASK": 1,  # ask other user
            "NOO": 2,  # give back informations
            "AKC": 3,  # Client said yes and gives u what
            "LST": 4,  # Gives nr of invitations
            "WRG": 5,  # Somethink goes wrong
            "SND": 6,  # Send informations

        }

    def rec_comand(self, line):  # method splits string array to single word and saves it to list
        line = line.decode("utf-8")
        list_of_line = line.split()
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

    def check_in_commands(self, line):  # method chcek if commend exist in dictionary and handles it
        if line[0] in self.in_comands:
            self.line_list = line

            if self.in_comands.get(line[0]) is 1:
                self.type = "ASK"

            elif self.in_comands.get(line[0]) is 2:
                self.type = "CHK"

            elif self.in_comands.get(line[0]) is 3:
                self.type = "NOO"

            elif self.in_comands.get(line[0]) is 4:
                self.type = "AKC"

            elif self.in_comands.get(line[0]) is 5:
                self.type = "RCV"

            else:
                self.type = "WRG"

    def handle_COMANDS(self, rec_com):
        print("handle_com" + str(rec_com))

        if rec_com[0] is "ASK":
            self.ask_comand(rec_com)

        elif rec_com[0] is "NOO":
            self.noo_comand(rec_com)

        elif rec_com[0] is "AKC":
            self.akc_command(rec_com)

        elif rec_com[0] is "CHK":  # bład tuuuuu
            self.chk_command(rec_com)

        elif rec_com[0] is "RCV":
            self.wrg_command(rec_com)

        elif rec_com[0] is "WRG":
            self.wrg_command(rec_com)
        else:
            self.wrg_command(rec_com)

    def handle_GETNAME(self, name):
        if name in self.users:
            return b"sorry name taken"

        self.name = name
        self.users[name] = self
        self.state = "COM"
        return b"WELCOME"

    def ask_comand(self, rec_com):
        self.orders.append([rec_com[1], "ASK", self.name.decode('utf-8')])
        return b"END"

    def noo_comand(self, rec_com):
        helper = [self.name.decode('utf-8'), "ASK", rec_com[1]]
        try:
            helper = self.orders.index(helper)
            self.orders[helper] = [self.name.decode('utf-8'), "NOO", rec_com[1]]
            return b"END"
        except ValueError:
            return b"ERR"

    def akc_command(self, rec_com):
        helper = [self.name.decode('utf-8'), "ASK", rec_com[1]]
        try:
            helper = self.orders.index(helper)
            self.orders[helper] = [self.name.decode('utf-8'), "AKC", rec_com[1]]
            return b"END"
        except ValueError:
            return b"ERR"

    def chk_command(self, rec_com):
        return_list = []
        list_to_send = []

        if len(self.orders) != 0:

            for x in range(len(self.orders)):
                if self.orders[x][0] == self.name.decode('utf-8'):
                    list_to_send.append(self.orders[x])

            helper = "LST " + str(len(list_to_send))
            print("helper " + helper)
            return_list.append(helper.encode('utf-8'))

            for y in range(len(list_to_send)):
                help_list = list_to_send[y]

                list_to_send[y] = str(list_to_send[y]).strip('[]')
                list_to_send[y] = list_to_send[y].replace(", ", " ")
                list_to_send[y] = list_to_send[y].replace("'", "")
                helper = "SND " + list_to_send[y]
                print(helper)
                return_list.append(helper.encode('utf-8'))

                if help_list[1] != "ASK":
                    print("Usuwam " + str(list_to_send[y]))
                    self.rcv_command(help_list)
            return_list.append(b"END")
            return return_list
        else:
            return b"NOT"

    def rcv_command(self, rec_com):

        try:
            helper = self.orders.index(rec_com)
            del self.orders[helper]
            return b"END"
        except ValueError:
             return b"END"

    def wrg_command(self, rec_com):
        a = str(self.name)
        new = a + " " + rec_com[0] + " SERVER"
        return new.encode('utf-8')








