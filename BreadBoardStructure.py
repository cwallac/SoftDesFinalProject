from ComponentModule import *
from BreadboardModule import *

#BREADBOARD[2] = left, [3] = right

'''I need to add all conditions for everything only left has been done for them, some not even all possible scenarios '''

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

								placeSecondPin(component,breadboard)
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
							breadboard[3][placedComponent.y[connect]].Occupied[k] = component
							
							return "PLACED"
				

def placeSecondPin(component,breadboard):
	# CHANGE TO CHECK WHERE A CONNECTION IS FIRST
	connect = component.connections[2]
	print connect
	for index in range(len(connect)+1):
		print index
		if component.x[1] <= breadboard[2][0].xpos+4 :

			closestConnection = whereDaConnectionAt(breadboard[2],component)

			direction = (closestConnection - component.y[1])/abs(closestConnection - component.y[1])
			for tile in range(5):
				if breadboard[2][component.y[1]+component.pin_gap*direction].Occupied[tile] == component: #POTENTIAL ISSUE IF WRONG PIN OF COMPONENT
					component.y[2] = component.y[1]+component.pin_gap*direction
					for k in range(4,-1,-1):
						if breadboard[2][component.y[2]].Occupied[k] != False:
							pass
						else:
							
							component.x[2] = breadboard[2][0].xpos + k
							breadboard[2][component.y[2]].Occupied[k] = component
							
							return "PLACED"

			

			

			
def whereDaConnectionAt(breadboardSide,component):
	returnList = []
	for row in range(30): # CHANGE TO LENGTH
		for tile in breadboardSide[row].Occupied:
			if breadboardSide[row].Occupied[tile] == component:
				if row == component.y[1]:
					
					pass
				else:
					returnList.append(row)
	if len(returnList) == 0:
		return False
	interList = []
	for distance in returnList:
		if abs(distance - component.y[1]) >= component.pin_gap and distance not in interList:
			interList.append(distance)

	distances = []

	for i in interList:
		distances.append(abs(i-component.y[1]))
	if len(distances) == 0:
		return False
	index = interList.index(min(distances))
	
	return interList[index]









	
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

	Resistor1 = resistor(45000,4,5,{1:[],2:[]})
	DIP = dip(4,5,{1:[Resistor1]},'dip',number_of_pins = 8, pin_gap = 3)
	Resistor1.connections[1] = [DIP]
	component = Resistor1
	Resistor2 = resistor(5,4,4,{1:[Resistor1],2:[]})
	Resistor1.connections[2].append(Resistor2)


	pinOnerail = board[2][0]
	pinTworail = board[3][0]
	board[2][3].Occupied[0] = Resistor1

	placeFirstComponent(DIP,board)
	componentPlacement(Resistor1,board)
	componentPlacement(Resistor2,board)

	



print DIP.y
print Resistor1.y
print Resistor1.x
print Resistor2.y
print Resistor2.x
print board[2][3].Occupied

	
	