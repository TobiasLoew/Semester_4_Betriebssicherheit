import os
import graphviz


class ANDNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)
        return

    def availability(self):
        self.avail = 1
        for i in range(len(self.nodes)):
            self.avail = self.avail * (1 - self.nodes[i].availability())
        self.avail = 1 - self.avail
        return self.avail


class ORNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)
        return

    def availability(self):
        self.avail = 1
        for i in range(len(self.nodes)):
            self.avail = self.avail * self.nodes[i].availability()
        return self.avail


class NOTNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []

    def add(self, node):
        self.nodes.append(node)
        return

    def availability(self):
        self.avail = 1 - self.nodes[0].availability()
        return self.avail

class EVENT:
    def __init__(self, name, lambd, my):
        self.name = name
        self.lambd = lambd
        self.my = my
    def add(self, node):
        self.nodes.append(node)
        return
    def availability(self):
        self.avail = 1 - (self.lambd / (self.lambd + self.my))
        return self.avail




TOP = ANDNODE("TOP")
A = ORNODE("A")
B = ORNODE("B")
C = NOTNODE("C")
E1 = EVENT("1", 1/1000, 1/4)
E2 = EVENT("2", 1/100, 1/2)
E3 = EVENT("3", 1/500, 1/5)
E4 = EVENT("4", 1/2500, 1/10)

TOP.add(A)
TOP.add(B)
A.add(C)
A.add(E2)
B.add(E3)
B.add(E4)
C.add(E1)

avail = TOP.availability()
print(avail)
