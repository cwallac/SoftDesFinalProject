#Placement model 
from ComponentModule import *
from BreadboardModule import *
def placingCD(new_component,list_of_components):
	list_of_components.append(new_component)
	for i in range(len(list_of_components)):
		if i == 1:
			if list_of_components[i].connections == {}:
				place_component(list_of_components[i],5,5)
		else: 
			for j in list_of_components[i].connections:
		 		if j == 1: 
					k = list_of_components[i].connections[j]
					if k == []:
						place_component(list_of_components[i],list_of_components[i].cx1,list_of_components[i].cy1)
					elif k[0].name == 'power':
						place_power(k[0],list_of_components[i])
						place_component(list_of_components[i],list_of_components[i].cx1,list_of_components[i].cy1)
					else:
						for b in range(len(k)):
							print k[b]
							place_component(list_of_components[i],k[b].cx[2],k[b].cy[2])
				if j > 1:
					k = list_of_components[i].connections[j]
					if k == []:
						place_component(list_of_components[i],list_of_components[i].cx1,list_of_components[i].cy1)
					elif k[0].name == 'power':
						place_power(k[0],list_of_components[i])
						place_component(list_of_components[i],list_of_components[i].cx1,list_of_components[i].cy1)
					else:
						for b in range(len(k)):
							update_connections(k[b],1,list_of_components[i])
							print k[b].connections
							place_component(k[b],list_of_components[i].cx[2],list_of_components[i].cy[2])

	 		



def place_component(component,x,y):
	component.placingSc(x,y)
	print component.cx
	print component.cy
	

def update_connections(component1,pnum,component2):
	if pnum not in component1.connections:
		component1.connections[pnum] = (component2)
	else:
		component1.connections[pnum].append(component2)

def place_power(power,component):
	power.connections[1].append(component)


if __name__ == '__main__':
	breadboard = createBreadboard()
	five_volts = power(5,{1:[]})
	resistor1 = resistor(10,0,0,0,0,'h',{1:[five_volts],2:[]})
	resistor2 = resistor(10,10,10,0,0,'h',{})
	resistor3 = resistor(10,15,15,0,0,'h',{1:[resistor1],2:[]})
	capacitor1 = capacitor(10,5,5,0,0,'v',{1:[resistor1], 2:[resistor2]})
	resistor4 = resistor(20,20,20,0,0,'v',{1:[resistor2]})
	
 	placingCD(resistor4,[resistor1,resistor2,resistor3,capacitor1])
