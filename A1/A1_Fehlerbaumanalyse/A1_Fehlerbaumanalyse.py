from graphviz import Digraph

digr = Digraph(node_attr = {'shape' : 'rectangle'}, edge_attr = {'dir':'none', 'splines' : 'ortho'})

class ANDNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        digr.node(name = self.name, label = self.name + " (&)")
    def add(self, node):
        self.nodes.append(node)
        digr.edge(self.name, node.name)
        return
    def availability(self):
        self.avail = 1
        for i in range(len(self.nodes)):
            self.avail = self.avail * ( 1 - self.nodes[i].availability() )
        return (1 - self.avail)


class ORNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        digr.node(name = self.name, label = self.name + " (≥1)")  
    def add(self, node):
        self.nodes.append(node)
        digr.edge(self.name, node.name)
        return
    def availability(self):
        self.avail = 1
        for i in range( len( self.nodes )):
            self.avail = self.avail * ( self.nodes[i].availability() ) 
        return self.avail


class NOTNODE:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        digr.node(name = self.name, label = self.name + " (NOT)")
    def add(self, node):
        self.nodes.append(node)
        digr.edge(self.name, node.name)
        return
    def availability(self):
        return ( 1 - self.nodes[0].availability() )

class EVENT:
    def __init__(self, name, lambd, my):
        self.name = name
        self.lambd = lambd
        self.my = my
        digr.node(self.name, shape = 'circle')
    #def add(self, node):
        #self.nodes.append(node)
        #return
    def availability(self):
        self.avail = self.lambd / (self.lambd + self.my)
        return (1 - self.avail)


class main:
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

    print( "Verfügbarkeit: ", TOP.availability() )
    digr.render()

# Aufgabe a)
# Ganz oben ist eine AND-Node 'TOP'. Diese hat als Eingänge die OR-Node 'A' und den Standardeingang 'E1'

# E1: 0,99602/0,00398   E2: 0,98039/0,01961     E3: 0,99010/0,00990     E4: 0,99602/0,00398
# C: 0,00398    A: 0,99610   B: 0,01384
# TOP: 0,98621