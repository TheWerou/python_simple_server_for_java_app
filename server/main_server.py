from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

from com_rec import Comends


class Chat(LineReceiver):
    def __init__(self, users, orders):
        self.users = users
        self.name = None
        self.state = "GETNAME"
        self.orders = orders
        self.com = Comends()

    def connectionMade(self):
        self.sendLine(b"What s your name ?")

    def connectionLost(self, reason):
        print(self.orders)
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        print(line)
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            print(type(self.name))
            self.handle_COMANDS(self.com.rec_comand(line))

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
            self.sendLine(b"sorry name taken")
            return
        self.sendLine(b"WELCOME")
        self.name = name
        self.users[name] = self
        self.state = "COM"

    def ask_comand(self, rec_com):
        self.orders.append([rec_com[1], "ASK", self.name.decode('utf-8')])
        self.sendLine(b"END")

    def noo_comand(self, rec_com):
        helper = [self.name.decode('utf-8'), "ASK", rec_com[1]]
        try:
            helper = self.orders.index(helper)
            self.orders[helper] = [self.name.decode('utf-8'), "NOO", rec_com[1]]
            self.sendLine(b"END")
        except ValueError:
            self.sendLine(b"ERR")

    def akc_command(self, rec_com):
        helper = [self.name.decode('utf-8'), "ASK", rec_com[1]]
        try:
            helper = self.orders.index(helper)
            self.orders[helper] = [self.name.decode('utf-8'), "AKC", rec_com[1]]
            self.sendLine(b"END")
        except ValueError:
            self.sendLine(b"ERR")

    def chk_command(self, rec_com):
        list_to_send = []

        if len(self.orders) != 0:

            for x in range(len(self.orders)):
                if self.orders[x][0] == self.name.decode('utf-8'):
                    list_to_send.append(self.orders[x])

            helper = "LST " + str(len(list_to_send))
            print("helper " + helper)
            self.sendLine(helper.encode('utf-8'))

            for y in range(len(list_to_send)):
                help_list = list_to_send[y]

                list_to_send[y] = str(list_to_send[y]).strip('[]')
                list_to_send[y] = list_to_send[y].replace(", ", " ")
                list_to_send[y] = list_to_send[y].replace("'", "")
                helper = "SND " + list_to_send[y]
                print(helper)
                self.sendLine(helper.encode('utf-8'))

                if help_list[1] != "ASK":
                    print("Usuwam " + str(list_to_send[y]))
                    self.rcv_command(help_list)

            self.sendLine(b"END")
        else:
            self.sendLine(b"NOT")

    def rcv_command(self, rec_com):

        try:
            helper = self.orders.index(rec_com)
            del self.orders[helper]
            self.sendLine(b"END")
        except ValueError:
            self.sendLine(b"END")

    def wrg_command(self, rec_com):
        a = str(self.name)
        new = a + " " + rec_com[0] + " SERVER"
        self.sendLine(new.encode('utf-8'))


class ChatFactory(Factory):
    def __init__(self):
        self.users = {}
        self.orders = [["MACIEK", "ASK", "MICHAL"], ["MACIEK", "NOO", "TOMEK"]]

    def buildProtocol(self, addr):
        return Chat(self.users, self.orders)


reactor.listenTCP(8123, ChatFactory())
reactor.run()

#192.168.49.41 ip serve