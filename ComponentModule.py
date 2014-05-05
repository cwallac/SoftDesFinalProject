#Component Related Classes

class Component(object):
	"""A component to be placed on the breadboard or in the circuit schematic"""

	def __init__ (self,value,cx1,cy1,x1,y1,orientation,connections,number_of_pins,pin_gap,name):
		self.name = name
		self.number_of_pins = number_of_pins
		self.cx1 = cx1
		self.cy1 = cy1
		self.connections = connections
		for i in range(self.number_of_pins):
			self.connections[i+1] = []
		
		self.orientation = orientation
		self.pin_gap = pin_gap
		self.value = value
		self.x = {}
		self.y = {}
		self.cx = {}
		self.cy = {}
		self.x1 = x1
		self.y1 = y1

		

	def __str__ (self):
		return '%s of %s' % (self.name,self.value)

	def placingSc(self,X1,Y1): 
		self.cx[1] = X1
		self.cy[1] = Y1
		if self.orientation == 'h':
			self.cy[2] = Y1
			self.cx[2] = X1+1
		else:
			self.cx[2] = X1
			self.cy[2] = Y1+1

class resistor(Component):
	"""A component to be placed on the breadboard. Has a resistance and a size."""
	def __init__(self,value,cx1,cy1,x1,y1,orientation,connections,pin_gap = 2,number_of_pins = 2,name = 'resistor'):
		super(resistor,self).__init__(value,cx1,cy1,x1,y1,orientation,connections,number_of_pins,pin_gap,name)

class capacitor(Component):
	"""A component to be placed on the breadboard. Has a capacitance and a size.""" 
	def __init__(self,value,cx1,cy1,x1,y1,orientation,connections,pin_gap = 2,number_of_pins = 2,name = 'capacitor'):
		super(capacitor,self).__init__(value,cx1,cy1,x1,y1,orientation,connections,number_of_pins,pin_gap,name)

class dip(Component):
	"""A component for the breadboard, representative of a variety of device with multiple pins. Always oriented horrizontally.""" 
	def __init__(self,cx1,cy1,x1,y1,orientation,connections,name,number_of_pins = 8, pin_gap = 2):
		super(dip,self).__init__('none',cx1,cy1,x1,y1,orientation,connections,number_of_pins,pin_gap,name)
		self.pinlist = {}

class potentiometer(Component):
	"""A component for the breadboard, representative of a device that has a variable resistance"""
	def __init__(self,value,cx1,cy1,x1,y1,orientation,connections,name,number_of_pins = 3, pin_gap = 2):
		super(potentiometer,self).__init__(value,x1,y1,orientation,connections,name,number_of_pins,pin_gap)

class trace(object): 
	def __init__(self,x1,y1,x2,y2,value1,value2):
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.x = {}
		self.y = {}
		self.cx = {}
		self.cy = {}
		self.x[1] = x1
		self.x[2] = x2
		self.y[1] = y1
		self.y[2] = y2
		self.name = 'trace'
		self.connections = {1:[],2:[]}
		self.value1 = value1
		self.value2 = value2

class power(object):
	def __init__(self,value,connections):
		self.value = value
		self.cx = {}
		self.cy = {}
		self.x = {}
		self.y = {}
		self.connections = connections
		self.name = 'power'

class ground(power):
	def __init__(self,value,connections):
		super(ground,self).__init__(value,connections)
		self.name = 'ground'


    
		
if __name__ == '__main__':
	TRA = trace(1,1,2,2,0,0)
	#RES = resistor(45,1,1,{1:'GRD',2:'VSS'},5)
	#print RES.pin_gap
	#DIP = dip(1,1,{1:'VREF'},'POOP')
	#print DIP.name
	#print DIP.number_of_pins
	print TRA.connections
