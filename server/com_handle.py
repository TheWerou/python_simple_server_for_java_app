

class ComHandle:
    def __init__(self, orders, name):
        self.orders = orders
        self.name = name

    def ask_comand(self, rec_com):      # method saves invitation to order
        self.orders.append([rec_com[1], "ASK", self.name.decode('utf-8')])
        return b"END"

    def noo_comand(self, rec_com):      # method check if invitation exist if exist change it to answer
        helper = [self.name.decode('utf-8'), "ASK", rec_com[1]]
        try:
            helper = self.orders.index(helper)
            self.orders[helper] = [self.name.decode('utf-8'), "NOO", rec_com[1]]
            return b"END"
        except ValueError:
            return b"ERR"

    def akc_command(self, rec_com):     # method handles AKC command
        helper = [self.name.decode('utf-8'), "ASK", rec_com[1]]
        try:
            helper = self.orders.index(helper)
            self.orders[helper] = [self.name.decode('utf-8'), "AKC", rec_com[1]]
            return b"END"
        except ValueError:
            return b"ERR"

    def chk_command(self, rec_com):             # 1 method look for occurrence of name in order save it to list
        return_list = []                        # 2 and then preper to send it to the client
        list_to_send = []

        if len(self.orders) != 0:

            for x in range(len(self.orders)):
                if self.orders[x][0] == self.name.decode('utf-8'):
                    list_to_send.append(self.orders[x])

            helper = "LST " + str(len(list_to_send))
            print("helper " + helper)
            return_list.append(helper.encode('utf-8'))

            for y in range(len(list_to_send)):                          # list to string convert--------
                help_list = list_to_send[y]

                list_to_send[y] = str(list_to_send[y]).strip('[]')
                list_to_send[y] = list_to_send[y].replace(", ", " ")
                list_to_send[y] = list_to_send[y].replace("'", "")
                helper = "SND " + list_to_send[y]
                print(helper)
                return_list.append(helper.encode('utf-8'))              # --------------

                if help_list[1] != "ASK":                               # deleting AKC and NOO commands
                    print("Usuwam " + str(list_to_send[y]))
                    self.rcv_command(help_list)

            return_list.append(b"END")                                  # lst thing add thant need to be send
            return return_list
        else:
            return b"NOT"

    def rcv_command(self, rec_com):         # remove order from list

        try:
            helper = self.orders.index(rec_com)
            del self.orders[helper]
            return True
        except ValueError:
            return False

    def wrg_command(self, rec_com):         # method send wrong to client
        a = str(self.name)
        new = a + " " + rec_com[0] + " SERVER"
        return new.encode('utf-8')