#Model of Program
# v.1 created 4/2/2014 8:52 pm. 

class Component(object):
	"""A component to be placed on the breadboard or in the circuit schematic"""

	def __init__ (self,name,value,number_of_pins,pin_gap,x1,y1):
		self.name = name
		self.number_of_pins = number_of_pins
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
	def __init__(self,name = 'resistor',value,number_of_pins = 2,pin_gap = 3,x1,y1):
		super(resistor,self).__init__(name,value,number_of_pins,pin_gap,x1,y1)

class capacitor(Component):
	"""A component to be placed on the breadboard. Has a capacitance and a size.""" 
	def __init__(self,name = 'capacitor',value,number_of_pins = 2,pin_gap = 3, x1,y1):
		super(capacitor,self).__init__(name,value,number_of_pins,pin_gap,x1,y1)

class dip(Component):
	"""A component for the breadboard, representative of a variety of devices with multiple pins. Always oriented horrizontally.""" 
	def __init__(self,name,number_of_pins = 8, pin_gap = 3, x1,y1):
		super(dip,self).__init__(name,'none',number_of_pins,pin_gap,x1,y1)
		self.pinlist = {}

	def dip_placement(self):
		for i in range(1,self.number_of_pins,2)
			self.pinlist[i] = (x1,y1+(i-1))
			self.pinlist[i+1] = (x1+pin_gap,y1+(i-1))

class trace(object): 
	def __init__(self,x1,y1,x2,y2,value1,value2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.value1 = value1
		self.value2 = value2
