from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

from com_rec import Comends


class Comunication(LineReceiver):
    def __init__(self, users, orders):
        self.users = users
        self.name = None
        self.state = "GETNAME"
        self.orders = orders

    def connectionMade(self):
        self.sendLine(b"What s your name ?")

    def connectionLost(self, reason):
        print(self.orders)
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        com = Comends(self.users, self.orders, self.state, self.name)
        print(line)
        if self.state == "GETNAME":
            self.handle_GETNAME(line)
        else:
            print(type(self.name))
            self.send_line_m(com.handle_COMANDS(com.rec_comand(line)))

    def send_line_m(self, thing_to_send):
        if isinstance(thing_to_send, list):
            for i in thing_to_send:
                self.sendLine(i)
        else:
            self.sendLine(thing_to_send)

    def handle_GETNAME(self, name):
        if name in self.users:
            self.sendLine(b"sorry name taken")

        self.name = name
        self.users[name] = self
        self.state = "COM"
        self.sendLine(b"WELCOME")


class ProgramFactory(Factory):
    def __init__(self):
        self.users = {}
        self.orders = []

    def buildProtocol(self, addr):
        return Comunication(self.users, self.orders)


reactor.listenTCP(8123, ProgramFactory())
reactor.run()

#192.168.49.41 ip serve