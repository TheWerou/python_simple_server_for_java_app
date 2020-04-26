from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

from com_rec import Comends


class Comunication(LineReceiver):
    def __init__(self, users, orders):       # constructor
        self.users = users                  # list of users
        self.name = None                    # list name of connected and handled client
        self.state = "GETNAME"              # this method check if client have name
        self.orders = orders                # list of all clients invitations

    def connectionMade(self):                   # method activate it self when new client made connection
        self.sendLine(b"What s your name ?")    # line that user gets at connection

    def connectionLost(self, reason):           # method activate it self when connection is lost
        print(self.orders)
        if self.name in self.users:             # this line look for user in user list
            del self.users[self.name]           # if user is on user list then user is deleted from list

    def lineReceived(self, line):               # method activate it self when receive line
        print(line)
        if self.state == "GETNAME":             # check if user have assigned name
            self.handle_GETNAME(line)           # if not this method give it

        else:                                   # If user have name line is passed to special method in class Comends

            com = Comends(self.users, self.orders, self.name)
            print(type(self.name))
            self.send_line_m((com.handle_COMANDS(com.rec_comand(line))))   # method below send reply to client

    def send_line_m(self, thing_to_send):                                # method send line or lines to client
        if isinstance(thing_to_send, list):                              # check if thing to send is list
            for i in thing_to_send:                                      # if thing_to_send is list then send singly
                self.sendLine(i)
        else:
            self.sendLine(thing_to_send)

    def handle_GETNAME(self, name):             # method gives user name (when user connect he send his name)
        if name in self.users:
            self.sendLine(b"sorry name taken")  # send line "sorry name taken"

        self.name = name                        # save user name
        self.users[name] = self                 # add user to list
        self.state = "COM"                      # user name was given
        self.sendLine(b"WELCOME")               # send hello and start normal comunication


class ProgramFactory(Factory):                  # base factory class (handles multy connections at once )
    def __init__(self):
        self.users = {}
        self.orders = [["MACIEK", "ASK", "TOMEK"], ["MACIEK", "NOO", "BOGDAN"], ["TOMEK", "ASK", "IGA"]]

    def buildProtocol(self, addr):
        return Comunication(self.users, self.orders)


reactor.listenTCP(8123, ProgramFactory())       # this object run Twisted code
reactor.run()

#192.168.49.41 ip serve