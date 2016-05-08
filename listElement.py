import sys
from enum import Enum

class stat(Enum)
	unstarted = 0
	started = 1
	complete = 2

class ListElement():
	def __init__(self, text, state=stat.unstarted, ):
		self.summary = text
		self.status = state
	
		 
