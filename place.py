#Placement model 
from ComponentModule import *
from BreadboardModule import *
def placingCD(list_of_components):
	for i in range(len(list_of_components)):
		if list_of_components[i].connections == '':
			place_first_component(list_of_components[i],i,i)
		else:
			for j in list_of_components[i].connections: 
				for k in list_of_components[i].connections[j]:

def place_first_component(component,x,y):
	component.x[1] = x
	component.y[1] = y
	for l in range(component.number_of_pins):
		if l % 2 == 0:
			if component.orientation == 'v':
				component.x[l] = component.x[l-1]
				component.y[l] = component.y[l-1]+list_of_components[i].pin_gap
			else:
				component.x[l] = component.x[l-1]+list_of_components[i].pin_gap
				component.y[l] = component.y[l-1]
		else:
			component.x[l] = component.x[1]+component.pin_gap
			component.y[l] = component.y[1]+1


if __name__ == '__main__':
	breadboard = createBreadboard()
	vs = power(5)
	ground = power(0)
	resistor1 = resistor(10,0,0,{1:'',2:capacitor1})
	capacitor1 = capacitor(10,1,1,{1:resistor1,2:ground},2)

