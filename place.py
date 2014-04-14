#Placement model 
from ComponentModule import *
from BreadboardModule import *
def placingCD(list_of_components):
	list_of_components[0].x1 = 0
	list_of_components[1].y1 = 0
	for i in range(len(list_of_components)):
		for j in list_of_components[i].connections: 
			if list_of_components[i].connections[j] == '':
				if list_of_components[i].orientation == 'v':
					list_of_components[i].x2 = list_of_components[i].x1
					list_of_components[i].y2 = list_of_components[i].y1+


if __name__ == '__main__':
	breadboard = createBreadboard()
	vs = power(5)
	ground = power(0)
	resistor1 = resistor(10,0,0,{1:'',2:capacitor1})
	capacitor1 = capacitor(10,1,1,{1:resistor1,2:ground},2)

