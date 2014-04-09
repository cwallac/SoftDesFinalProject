#Component Related Classes

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
	def __init__(self,value,x1,y1,pinValues,pin_gap = 3,number_of_pins = 2,name = 'resistor'):
		super(resistor,self).__init__(value,x1,y1,pinValues,number_of_pins,pin_gap,name)

class capacitor(Component):
	"""A component to be placed on the breadboard. Has a capacitance and a size.""" 
	def __init__(self,value,x1,y1,pinValues,pin_gap = 3,number_of_pins = 2,name = 'capacitor'):
		super(resistor,self).__init__(value,x1,y1,pinValues,number_of_pins,pin_gap,name)

class dip(Component):
	"""A component for the breadboard, representative of a variety of devices with multiple pins. Always oriented horrizontally.""" 
	def __init__(self,x1,y1,pinValues,name,number_of_pins = 8, pin_gap = 3):
		super(dip,self).__init__('none',x1,y1,pinValues,number_of_pins,pin_gap,name)
		self.pinlist = {}

	def dip_placement(self):
		for i in range(1,self.number_of_pins):
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

RES = resistor(45,1,1,{1:'GRD',2:'VSS'},5)
print RES.pin_gap
DIP = dip(1,1,{1:'VREF'},'POOP')
print DIP.name
print DIP.number_of_pins
