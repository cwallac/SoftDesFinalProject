from ComponentModule import *
from BreadboardModule import *

#BREADBOARD[2] = left, [3] = right

"""
MAJOR REFACTORING IN PROGRESS
I need to add all conditions for everything only left has been done for them, some not even all possible scenarios 
IE:
-THere isn't teh connection value pin_gap away from a component in placeSecodnpin
-whereDaConnectionAt returns False
-FUTURE: BLOCKED, FILLED AREAS, BETTER DIP PLACEMENT, POWER RAILS"""

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






#################################################################################################


def identifyConnections(component,breadboard):
	'''Returns a tuple of rail connection found at,row connection found at and assoaicated tile it was found at '''
	returnRail = []
	returnRow = []
	returnTile = []
	for rail in range(len(breadboard)):
		if 1 < rail < 4:
				for row in range(breadboard[0].length):
					for tile in range(5):
						if breadboard[rail][row].Occupied[tile] == component:
							returnRail.append(rail)
							returnRow.append(row)
							returnTile.append(tile)



		else:
			for tile in range(breadboard[rail].length):
						if breadboard[rail].Occupied[tile] == component:
							returnRail.append(rail)
							returnRow.append(row)
							returnTile.append(0)
	return (returnRail,returnRow,returnTile)

def closestConnections(component,breadboard):
	
	if component.x[1] < 10:
		compSide = 2
	else:
		compSide = 3
	connectionList = []
	#FIRST CHECK FOR SAME PANEL
	for panel in range(len(breadboard)):
		if 1 < panel < 4:
			for row in range(len(breadboard[panel])):
				for tile in range(5):
					if compSide == panel and component.y[1] == row:
						pass
					else:
						if breadboard[panel][row].Occupied[tile] == component:
							connectionList.append((panel,row))
						

		else:
			pass

	if len(connectionList) == 0:
			return False
		
	distanceList = []
	for index in range(len(connectionList)):
		distance = 0
		if connectionList[index][0] != compSide:
			distance += 3
			distance += abs(component.y[1] - connectionList[index][1]) 
		else:
			distance += abs(component.y[1] - connectionList[index][1])
		distanceList.append(distance)
	


	space = distanceList.index(min(distanceList))
	return (connectionList[space],distanceList[space])

def SetPosValues(placedComponent,componentToPlace,placedPin,ToPlacePin,breadboard):
	if breadboard[1].xpos < placedComponent.x[placedPin] < breadboard[4].xpos:
		componentToPlace.y[ToPlacePin] = placedComponent.y[placedPin]
		if  1 < placedComponent.x[placedPin] <= breadboard[2][0].xpos+4:
			for k in range(4,-1,-1):
				if breadboard[2][componentToPlace.y[ToPlacePin]].Occupied[k] != False:
					pass
				else:
							
					componentToPlace.x[ToPlacePin] = breadboard[2][0].xpos + k
					breadboard[2][componentToPlace.y[ToPlacePin]].Occupied[k] = componentToPlace
							
					return "PLACED"



		elif breadboard[2][0].xpos+4 < placedComponent.x[placedPin] <= breadboard[4].xpos:
			for k in range(5):
				if breadboard[3][componentToPlace.y[ToPlacePin]].Occupied[k] != False:
					pass
				else:
							
					componentToPlace.x[ToPlacePin] = breadboard[3][0].xpos + k
					breadboard[3][componentToPlace.y[ToPlacePin]].Occupied[k] = componentToPlace
							
					return "PLACED"

		else:
			pass
			#POWER RAIL

	else:
		pass
		#POWER RAIL
def findOpenSpace(component,breadboard,side):
	closest = []
	poop = []
	found = 0
	if side == 2 or side == 3:
		for i in range(component.y[1],breadboard[0].length-component.pin_gap):
			empty = 0
			bad = 0
			for j in range(5):
			
				if breadboard[side][i].Occupied[j] != False or breadboard[side][i+component.pin_gap].Occupied[j] != False:
					bad += 1

				else:
					empty += 1
			if empty == 5 and found == 0:
				closest.append(i)
		found = 0

		for i in range(component.pin_gap,component.y[1]):
			empty = 0
			bad = 0
			for j in range(5):
			
				if breadboard[side][i].Occupied[j] != False or breadboard[side][i+component.pin_gap].Occupied[j] != False:
					bad += 1

				else:
					empty += 1
			if empty == 5 and found == 0:
				closest.append(i)
		poop[:] = [abs(x - component.y[1]) for x in closest]
		
		
		minimum = min(poop)
		for j in range(len(poop)):
			if poop[j] == minimum:
				
				return closest[j]

	else:
		pass

def defaultSecondPlacementFailed(breadboard,component,side):
	occupiedFlag = 0
	if component.y[1] < component.pin_gap:
		pass
		#FIND NEXT OPEN SPOT TO PLACE COMPONENT THEN DRAW TRACE DO DRAW TRACE FUNCTION
	else:
		if side == 'LEFT':
			for k in range(5):
				if breadboard[2][component.y[1]-component.pin_gap].Occupied[k] != False:
					occupiedFlag = 1
					print "FOUND IT CHRIS"
					#DO MORE STUFF

			if occupiedFlag == 0:	
				component.y[2] = breadboard[2][component.y[1]-component.pin_gap].ypos
					
				component.x[2] = component.x[1]
				breadboard[2][component.y[1]-component.pin_gap].Occupied[component.x[2]-breadboard[2][0].xpos] = component
				return 'PLACED'
			else: 
				
				print 'NO PLACE'
				openSpot =findOpenSpace(component,breadboard,2)
				oldCord = (component.x[1],component.y[1])
				component.y[1] = openSpot
				component.y[2] = openSpot+component.pin_gap
				component.x[1] = breadboard[2][0].xpos+4 
				component.x[2] = breadboard[2][0].xpos+4 
				breadboard[2][openSpot].Occupied[4] = component
				breadboard[2][openSpot+component.pin_gap].Occupied[4] = component
				trace(component.x[1],component.y[1],component.x[1],component.y[2],[component.connections[1]],[component.connections[1]])
				breadboard[2][component.y[2]].Occupied[component.x[1]] = component
		
		elif side == 'RIGHT':
			for k in range(5):
				if breadboard[3][component.y[1]-component.pin_gap].Occupied[k] != False:
					occupiedFlag = 1
					print "FOUND IT CHRIS"
					#DO MORE STUFF

			if occupiedFlag == 0:
				component.y[2] = breadboard[3][component.y[1]-component.pin_gap].ypos
					
				component.x[2] = component.x[1]
				breadboard[3][component.y[1]-component.pin_gap].Occupied[component.x[2]-breadboard[3][0].xpos] = component
				return 'PLACED'

			else:
				openSpot = findOpenSpace(component,breadboard,3)
				oldCord = (component.x[1],component.y[1])
				component.y[1] = openSpot
				component.y[2] = openSpot+component.pin_gap
				component.x[1] = breadboard[3][0].xpos+4 
				component.x[2] = breadboard[3][0].xpos+4 
				breadboard[3][openSpot].Occupied[0] = component
				breadboard[3][openSpot+component.pin_gap].Occupied[0] = component
				trace(component.x[1],component.y[1],component.x[1],component.y[2],[component.connections[1]],[component.connections[1]])
				breadboard[3][component.y[2]].Occupied[component.x[1]] = component


		else:
			#THIS MEANS POWER-RAIL
			print 'NO PLACE'
			#findOpenSpace(component,breadboard,side)


def placeSecondPin(coordinate,distance,component,breadboard):
	side = leftOrRight(component,1)

	print side
	
	occupiedFlag = 0
	print coordinate
	if coordinate == False:
		#THERE IS NO OTHER CONNECTION ON THE BOARD
		if side == 'LEFT':
			for k in range(5):
				if breadboard[2][component.y[1]+component.pin_gap].Occupied[k] != False:
					occupiedFlag = 1
					print "FOUND IT CHRIS"
					#DO MORE STUFF

			if occupiedFlag == 0:	
				component.y[2] = breadboard[2][component.y[1]+component.pin_gap].ypos
					
				component.x[2] = component.x[1]
				breadboard[2][component.y[1]+component.pin_gap].Occupied[component.x[2]-breadboard[2][0].xpos] = component
				return 'PLACED'
			else: 
				
				print 'NO PLACE'
				defaultSecondPlacementFailed(breadboard,component,side)
				#OCCUPIED BY SOMETHING ELSE, TRY THE REVERSE DIRECTION, IF FAIL DRAW A TRACE Up TO PIN GAP AWAY FROM EMPTY SPACE
		
		if side == 'RIGHT':
			for k in range(5):
				if breadboard[3][component.y[1]+component.pin_gap].Occupied[k] != False:
					occupiedFlag = 1
					print "FOUND IT CHRIS"
					#DO MORE STUFF

			if occupiedFlag == 0:
				component.y[2] = breadboard[3][component.y[1]+component.pin_gap].ypos
					
				component.x[2] = component.x[1]
				breadboard[3][component.y[1]+component.pin_gap].Occupied[component.x[2]-breadboard[3][0].xpos] = component
				return 'PLACED'

			else: 
				
				print 'NO PLACE'
				defaultSecondPlacementFailed(breadboard,component,side)

		else:
			#THIS MEANS POWER RAIL
			print 'NO PLACE'
			


	else:
		pass
		# FOUND A CONNECTION SOMEWHERE
def dipStartingPoint(breadboard,placeDip):
	for i in range(30):
		empty = 0
		bad = 0
		for j in range(5):
			for plus in range(placeDip.number_of_pins/2):
				if breadboard[3][i+plus].Occupied[j] != False or breadboard[2][i+plus].Occupied[j] != False:
					bad += 1

				else:
					empty += 1
		if empty == 5*placeDip.number_of_pins/2 :
			return i+2

def placeComponent(component,breadboard):
	#CURRENTLY NOT DEALING WIHT POWER RAILS
	if component.name == 'dip':
		#DIP PLACEMENT
		offset = dipStartingPoint(breadboard,component)
		for i in range(component.number_of_pins+1):
			if i == 0:
				pass
			elif i % 2 == 1:
				component.x[i] = 8
			else:
				component.x[i] = component.x[1] + component.pin_gap
		#ConnectToDIP()

		
		

		for i in range(component.number_of_pins/2):

			component.y[i*2+1] = i+offset
			component.y[i*2+2] = i+offset
			breadboard[2][i+offset].Occupied[4] = component
			breadboard[3][i+offset].Occupied[0] = component
			
		

	else:
		matchingComponent = component.connections[1][0]
		identifyingTuple = identifyConnections(matchingComponent,breadboard)
		rail = identifyingTuple[0][0]
		Row = identifyingTuple[1][0]
		Tile = identifyingTuple[2][0]
		print rail, Row, Tile
		for i in breadboard[rail][Row].Occupied[Tile].connections:
			print breadboard[rail][Row].Occupied[Tile].connections[i]
			print component
			if breadboard[rail][Row].Occupied[Tile].connections[i][0] == component:
				print 'MATCh'
				SetPosValues(breadboard[rail][Row].Occupied[Tile],component,i,1,breadboard)
				values = closestConnections(component,breadboard)
				if values == False:
					distance = False
					coordinate = False
				else:
					distance = values[1]
					coordinate = values[0]
				placeSecondPin(coordinate,distance,component,breadboard)
				

			
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

	Resistor1 = resistor(45000,4,5,'h',{1:[],2:[]})
	Resistor2 = resistor(4500,4,5,'h',{1:[],2:[]},4)
	Resistor3 = resistor(400,4,5,'h',{1:[],2:[]})
	DIP = dip(4,5,'h',{12:[Resistor1]},'dip',number_of_pins = 12, pin_gap = 3)
	DIP2 = dip(4,5,'h',{3:[Resistor2]},'dip',number_of_pins = 8, pin_gap = 3)
	Resistor1.connections[1] = [DIP]
	Resistor2.connections[1] = [Resistor1]
	Resistor1.connections[2] = [Resistor2]
	Resistor3.connections[1] = [Resistor2]
	Resistor2.connections[2] = [Resistor3]
	board[3][15].Occupied[0] = True
	board[3][9].Occupied[0] = True
	placeFirstComponent(DIP,board)
	placeComponent(Resistor1,board)
	placeComponent(Resistor2,board)
	placeComponent(Resistor3,board)
	#placeComponent(DIP2,board)
	#board[2][8].Occupied[1] = DIP
	print board[2][8].Occupied.values()
	print Resistor1.x
	print Resistor1.y
	print Resistor2.x
	print Resistor2.y
	print Resistor3.x
	print Resistor3.y
	
	print board[3][13].Occupied
	print board[3][13].Occupied
	#print DIP2.x
	#print DIP2.y
#	if isinstance(DIP,dip):
#		print "FUCLK CRHIS"
#	component = Resistor1
#	Resistor2 = resistor(5,4,4,'h',{1:[Resistor1],2:[]})
#	Resistor1.connections[2].append(Resistor2)


#	pinOnerail = board[2][0]
#	pinTworail = board[3][0]
#	board[2][4].Occupied[0] = Resistor1

#	
#	placedComponent(Resistor1,board)
	#componentPlacement(Resistor1,board)
	#componentPlacement(Resistor2,board)
#	whereDaConnectionAt(board,DIP,2)

#print identifyConnections(DIP,board)	

#print board[2][0].Occupied
#print 'Dips x pos is' + str(DIP.x) 
#print 'Dips y pos is' + str(DIP.y)
#print 'First resistor y position is' + str(Resistor1.y)
#print 'First resistor x position is' + str(Resistor1.x)
#print Resistor2.y
#print Resistor2.x
#print board[2][3].Occupied

	
	