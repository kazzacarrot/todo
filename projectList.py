import listElement
import sys

class project():
	def __init__(self, n="today"):
		self.name = n
		self.dos = []  #things to do

	def add_list_element(self, e, s=listElement.stat.unstarted):
		if type(e)==Str:
			listElement.ListElement(e, s)
		elif type(e) ==ListElement:
			self.dos.append(e)

    def incorporate_project(self, p):
    	## for each to-do in p, add it to self.dos
    	for e in p.dos:
    		if e not in self.dos:
    			self.dos.append(e)
    	