#Placement model 
from ComponentModule import *
from BreadboardModule import *
def placingCD(list_of_components):
	for i in range(len(list_of_components)):
		if list_of_components[i].connections == {}:
			place_component(list_of_components[i],list_of_components[i].cx1,list_of_components[i].cy1)
		else: 
		 	for j in list_of_components[i].connections:
		 		if j == 1: 
					k = list_of_components[i].connections[j]
					for b in range(len(k)):
						place_component(list_of_components[i],k[b].cx[2],k[b].cy[2])
				if j > 1:
					k = list_of_components[i].connections[j]
					for b in range(len(k)):
						update_connections(k[b],1,list_of_components[i])
						print k[b].connections
						place_component(k[b],list_of_components[i].cx[2],list_of_components[i].cy[2])
		 		



def place_component(component,x=0,y=0):
	component.cx[1] = x
	component.cy[1] = y
	for l in range(2,component.number_of_pins+1):
		if l % 2 == 0:
			if component.orientation == 'v':
				component.cx[l] = component.cx[l-1]
				component.cy[l] = component.cy[l-1]+component.pin_gap
			else:
				component.cx[l] = component.cx[l-1]+component.pin_gap
				component.cy[l] = component.cy[l-1]
		else:
			component.cx[l] = component.cx[1]
			component.cy[l] = component.cy[l-1]+1
	print component.cx 
	print component.cy

def update_connections(component1,pnum,component2):
	if pnum not in component1.connections:
		component1.connections[pnum] = (component2)
	else:
		component1.connections[pnum].append(component2)

def place_power():



if __name__ == '__main__':
	breadboard = createBreadboard()
	resistor1 = resistor(10,0,0,0,0,'h',{})
	resistor2 = resistor(10,10,10,0,0,'h',{})
	resistor3 = resistor(10,15,15,0,0,'h',{1:[resistor1],2:[]})
	capacitor1 = capacitor(10,5,5,0,0,'v',{1:[resistor1], 2:[resistor2]})
	five_volts = power(5,{1:[resistor1]})
	
 	placingCD([resistor1,resistor2,resistor3,capacitor1])
