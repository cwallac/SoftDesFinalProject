#Model of Program
# v.1 created 4/2/2014 8:52 pm. 



#COMPONENT

class Component(object):
	"""A component to be placed on the breadboard or in the circuit schematic"""

	def __init__ (self,value,x1,y1,pinValues,number_of_pins,pin_gap,name):
		self.name = name
		self.number_of_pins = number_of_pins
		
		self.PinValues = pinValues
		self.pin_gap = pin_gap
		self.value = value
		self.x1 = x1

	def __str__ (self):
		return '%s of %s' % (self.name,self.value)

	def placement(self,orientation = 'v'):
		if orientation == 'h':
			self.x2 = x1+pin_gap
			self.y2 = y1
		else:
			self.y2 = y1+pin_gap
			self.x2 = x1


class resistor(Component):
	"""A component to be placed on the breadboard. Has a resistance and a size."""
	def __init__(self,value,x1,y1,pinValues,number_of_pins = 2,pin_gap = 3,name = 'resistor'):
		super(resistor,self).__init__(value,x1,y1,pinValues,number_of_pins,pin_gap,name)

#BREADBOARD RELATED CLASSES
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

# Breadboard construction

if __name__ == '__main__':

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

    Resistor1 = resistor(45000,4,5,{1:'Vref',2:'GND'})
# DO SOME TESTING 


    leftBuildZone[0].Occupied[1] = True
    print leftBuildZone[0].Occupied
    
    leftBuildZone[0].value = 'Vref'
    
    print leftBuildZone[0]
    print Resistor1.PinValues
