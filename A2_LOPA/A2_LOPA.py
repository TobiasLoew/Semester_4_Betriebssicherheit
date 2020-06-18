from graphviz import Digraph
from math import log

digr = Digraph(node_attr = {'shape':'rectangle', 'fontsize':'5', 'fontname':'Arial'}, graph_attr = {'nodesep':'0'})
class USE:
	def __init__(self, name, prop):
		self.name = name
		self.next = None
		self.pre = None
		self.prop = prop
	def __repr__(self):
		return f'{self.__class__.__name__}({self.name}, {self.prop})'
	def setSuccessor(self, node):
		self.next = node
		node.pre = self
	def draw(self):
		# USE als node mit fester Größe zum Graph hinzufügen,
		digr.node(self.name, self.name, xlabel=str( self.prop ), height='1.5', width='0.5')
		# Wenn ein Event folgt, dessen draw-Funktion aufrufen
		if(self.next):
			self.next.draw()
	def frequency(self):
		# Rekursion bis zum ersten Event aufbauen
		self.pre.frequency()
		if(self.next):
			# Wenn ein Event folgt, dessen Frequency berechnen
			self.next.freq = self.pre.freq * self.prop
		else:
			# Wenn letzte USE auf Graph, Ausfallrate ausgeben
			return self.pre.freq * self.prop


class EVENT:
	def __init__(self, name, impact, freq):
		self.name = name
		self.next = None
		self.pre = None
		self.impact = impact
		self.freq = freq
	def __repr__(self):
		return f'{self.__class__.__name__}({self.name}, {self.impact}, {self.freq})'	
	def setSuccessor(self, node):
		self.next = node
		node.pre = self
	def draw(self):
		print(self.name, "Impact:", self.impact, "	Frequency:", self.freq, "	Länge in Graph:", (10 * (-1) / log(self.freq)) )
		# Event als node zum Graph hinzufügen
		digr.node(self.name, self.name, shape="rarrow", width=str( self.impact ), height=str( 10 * (-1) / (log(self.freq)) ) )
		self.next.draw()
	def frequency(self):
		if(self.pre):
			self.pre.frequency()
		return



class main:
	f0 = EVENT("f0", 0.25, 1/(365*24))
	f1 = EVENT("f1", 0.5, None)
	f2 = EVENT("f2", 0.75, None)
	f3 = EVENT("f3", 1, None)
	f4 = EVENT("f4", 1.25, None)

	u1 = USE("USE1", 0.1)
	u2 = USE("USE2", 0.2)
	u3 = USE("USE3", 0.15)
	u4 = USE("USE4", 0.2)
	u5 = USE("USE5", 0.15)

	f0.setSuccessor(u1)
	f1.setSuccessor(u2)
	f2.setSuccessor(u3)
	f3.setSuccessor(u4)
	f4.setSuccessor(u5)

	u1.setSuccessor(f1)
	u2.setSuccessor(f2)
	u3.setSuccessor(f3)
	u4.setSuccessor(f4)

	print("Ausfallrate des Gesamtsystems:", u5.frequency(), "1/h\n")
	f0.draw()
	digr.render()
