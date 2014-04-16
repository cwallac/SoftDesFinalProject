from ComponentModule import *
from BreadboardModule import *

#BREADBOARD[2] = left, [3] = right

def placeFirstComponent(component,breadboard):

	
	for i in range(component.number_of_pins):
		if i % 2 == 1:
			component.x[i] = 8
		else:
			component.x[i] = component.x[1] + component.pin_gap

		component.y[1] = 0
		
		component.y[2] = 0
		

	for i in range(component.number_of_pins/2):
		component.y[i*2] = i
		component.y[i*2+1] = i
		breadboard[2][i].Occupied[4] = True
		for j in range(5):
			if -3+component.pin_gap >= j:
				breadboard[3][i].Occupied[j] = True
	
	
	
			
	

	

	
def leftOrRight(component,pin):
	if pin % 2 == 0:
		if component.x[pin] <= 8:
			return 'LEFT'
		else: 
			return 'RIGHT'

	else :
		if component.x[pin] <= 8:
			return 'LEFT'
		else: 
			return 'RIGHT'


if __name__ == '__main__':

	board = createBreadboard()

	Resistor1 = resistor(45000,4,5,{})
	DIP = dip(4,5,{},'dip',number_of_pins = 8, pin_gap = 3)
	component = Resistor1



	pinOnerail = board[2][0]
	pinTworail = board[3][0]
	
	placeFirstComponent(DIP,board)

	
	
print DIP.y
print Resistor1.y



	
	