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
        self.send = self.sendLine
        self.com = Comends(users, orders,self.send )

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
            self.send_line(self.handle_COMANDS(self.com.rec_comand(line)))

    def send_line(self, thing_to_send):
        if isinstance(thing_to_send, list):
            for i in thing_to_send:
                self.send_line(i)
        else:
            self.send_line(thing_to_send)


class ChatFactory(Factory):
    def __init__(self):
        self.users = {}
        self.orders = [["MACIEK", "ASK", "MICHAL"], ["MACIEK", "NOO", "TOMEK"]]

    def buildProtocol(self, addr):
        return Chat(self.users, self.orders)


reactor.listenTCP(8123, ChatFactory())
reactor.run()

#192.168.49.41 ip serve