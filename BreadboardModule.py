#BREADBOARD STRUCTURE CLASSES

class rails(object):
	"""A component of the breadboard with 2 pins and a pin gap of zero"""

	def __init__(self,x1):
		self.name = 'rails'
		self.number_of_pins = 1
		self.length = 30 
		self.xpos = x1
		pinDictionary = {}
		for i in range(self.length):
			
			pinDictionary[i] = False 
		self.Occupied = pinDictionary
		self.pin_gap = 0
		self.value = ''

	def __str__ (self):
		return 'Power Rail with value of  %s' % (self.value)

class rows(object):
	"""The rows of the middle of the breadboard with 5 pins and pin gap of 0"""

	def __init__(self, y1 ,x1, side, name = 'row'):
		self.name = name
		self.number_of_pins = 5
		self.length = 1
		self.pin_gap = 0
		self.xpos = x1
		self.ypos = y1
		self.side = side
		pinDictionary = {}
		for i in range(self.number_of_pins):
			
			pinDictionary[i] = False
		
		self.Occupied = pinDictionary
		self.value = ''

	def __str__ (self):
		return ' Row %s on the %s side with value of  %s' % (self.ypos,self.side,self.value)


def createBreadboard():

	leftRail1 =  rails(0)
	leftRail2 = rails(1)
	rightRail1 = rails(17)
	rightRail2 = rails(18)

	leftBuildZone = []

	for i in range(leftRail1.length):
		leftBuildZone.append(rows((i),4,'left', 'leftrow' + str(i)))

	rightBuildZone = []

	for i in range(leftRail1.length):
		rightBuildZone.append(rows((i),11,'right', 'rightrow' + str(i)))

	breadboard = [leftRail1,leftRail2,leftBuildZone,rightBuildZone,rightRail1,rightRail2]

	return breadboard