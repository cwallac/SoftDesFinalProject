#Placement model 
from ComponentModule import *
from BreadboardModule import *
def placingCD(list_of_components):
	for i in range(len(list_of_components)):
		if list_of_components[i].connections == {}:
			place_component(list_of_components[i],list_of_components[i].x1,list_of_components[i].y1)
		else: 
		 	for j in list_of_components[i].connections: 
				k = list_of_components[i].connections[j]
				place_component(list_of_components[i],k.x[2],k.y[2])


def place_component(component,x=0,y=0):
	component.x[1] = x
	component.y[1] = y
	for l in range(2,component.number_of_pins+1):
		if l % 2 == 0:
			if component.orientation == 'v':
				component.x[l] = component.x[l-1]
				component.y[l] = component.y[l-1]+component.pin_gap
			else:
				component.x[l] = component.x[l-1]+component.pin_gap
				component.y[l] = component.y[l-1]
		else:
			component.x[l] = component.x[1]
			component.y[l] = component.y[l-1]+1
	print component.x 
	print component.y


if __name__ == '__main__':
	breadboard = createBreadboard()
	resistor1 = resistor(10,0,0,'h',{})
	capacitor1 = capacitor(10,5,5,'v',{1:resistor1})
 	placingCD([resistor1,capacitor1])