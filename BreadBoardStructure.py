from ComponentModule import *
from BreadboardModule import *

#BREADBOARD[2] = left, [3] = right

def placeFirstComponent(component,breadboard):

	
	for i in range(component.number_of_pins+1):
		if i == 0:
			pass
		elif i % 2 == 1:
			component.x[i] = 8
		else:
			component.x[i] = component.x[1] + component.pin_gap

		
		

	for i in range(component.number_of_pins/2):

		component.y[i*2+1] = i
		component.y[i*2+2] = i
		breadboard[2][i].Occupied[4] = component
		for j in range(5):
			if -3+component.pin_gap >= j:
				breadboard[3][i].Occupied[j] = component

def firstPinMatch(component,breadboard):
	"""POTENTIAL ERRORS INCLUDE THE IDENTIFYING TAKE FOR THE RESISTOR BEING JUST ITS PRINT STRING, POSSIBLE OVERLAP HOW DO WE START THIS PROBABLY WANT TO ONLY RUN THIS ALGORITHM FOR FIRST PIN """
	print "RUNNING CONNECTION"
	for i in component.connections:
		Connect = component.connections[i] 
		
		for j in Connect.connections:
			
			if Connect.connections[j] == component:
				component.y[i] = Connect.y[i]
				 
				row = component.y[i]
				if leftOrRight(Connect,j) == 'LEFT':
					for k in range(4,-1,-1):
						if breadboard[2][component.y[i]].Occupied[k] != False:
							pass
						else:
							
							component.x[1] = breadboard[2][0].xpos + k
							breadboard[2][row].Occupied[k] = component
							
							return "PLACED"
				


				else: 
					for k in range(5):
						if breadboard[3][component.y[i]].Occupied[k] != False:
							pass
						else:
							
							component.x[1] = breadboard[3][0].xpos + k
							breadboard[3][row].Occupied[k] = component
							
							return "PLACED"

def componentPlacement(component,breadboard):
	for i in component.connections:
		ConnectList = component.connections[i]
		for index in range(len(ConnectList)):
			connectedComponent = ConnectList[index] 
			for side in range(6):
				if 2 <= side <= 3:
					for row in range(breadboard[0].length):
						for space in range(5):
							if breadboard[side][row].Occupied[space] == connectedComponent:
								#WRITE FUNCTION TO FIND WHAT ROW THIS MATCHES AND CHENGE POSITION AND OCCUPIED VALUES GRAB INDEX
								
								changePosition(component,connectedComponent,[i,index],breadboard)
								return "PLACED"

def changePosition(matchComponent,placedComponent,componentPin,breadboard):
	#pin, index
	pin = componentPin[0]
	index = componentPin[1]
	for connect in placedComponent.connections:
		
		for indices in range(len(placedComponent.connections[connect])):
			if matchComponent == placedComponent.connections[connect][indices]:
				print "MATCH"
				
				matchComponent.y[pin] = placedComponent.y[connect]
				

				if leftOrRight(placedComponent,connect) == 'LEFT':
					for k in range(4,-1,-1):
						if breadboard[2][placedComponent.y[connect]].Occupied[k] != False:
							pass
						else:
							
							matchComponent.x[1] = breadboard[2][0].xpos + k
							breadboard[2][placedComponent.y[connect]].Occupied[k] = matchComponent
							
							return "PLACED"

				else: 
					for k in range(5):
						if breadboard[3][placedComponent.y[connect]].Occupied[k] != False:
							pass
						else:
							
							component.x[1] = breadboard[3][0].xpos + k
							breadboard[3][placedComponent.y[connect]].Occupied[k] = matchComponent
							
							return "PLACED"
				

def placeSecondPin:




	
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
	DIP = dip(4,5,{4:[Resistor1]},'dip',number_of_pins = 8, pin_gap = 3)
	Resistor1.connections[1] = [DIP]
	component = Resistor1



	pinOnerail = board[2][0]
	pinTworail = board[3][0]
	
	placeFirstComponent(DIP,board)
	componentPlacement(Resistor1,board)

	
	


print DIP.y
print Resistor1.y
print Resistor1.x
print board[3][1].Occupied

	
	