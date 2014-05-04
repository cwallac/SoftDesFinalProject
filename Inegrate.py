from BreadBoardStructure import *
from ComponentModule import *
from BreadboardModule import *

from place import *

class Model():
	def __init__(self):
		print "MODEL INITIALIZED"
		self.board = createBreadboard()
		self.compList = []

	def placeCompOnBreadBoard(self,component,board,compList):
		if len(compList) == 0:
			placeFirstComponent(component,board,compList)
		else:
			placeComponent(component,board,compList)

	def placeCompOnSchema(self,compList):
		placingCD(compList)

class Controller():
	pass

class View():
	pass

if __name__ == '__main__':
	
	Test = Model()
	print Test.board[3][0].Occupied
	Resistor1 = resistor(1,0,0,4,5,'h',{1:[],2:[]})
	Test.placeCompOnBreadBoard(Resistor1,Test.board,Test.compList)
	print Test.compList[0].x
	Test.placeCompOnSchema(Test.compList)
	print Test.compList[0].cx
