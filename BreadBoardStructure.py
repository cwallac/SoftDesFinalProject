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
	print "RUNNING IDENTIFY CONNECTIONS"
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

def closestConnections(component,breadboard,componentToPlace):
	print "RUNNING CLOSESTCONNECTIONS"
	
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
							print breadboard[panel][row].Occupied[tile], component, "THIS IS BREADBOARD NAME AND COMPONENT"
						

		else:
	#		for tile in range(len(breadboard[0].length)):
	#			if breadboard[panel].Occupied[tile] ==
			pass 
	print connectionList, "CONNECTION LIST"
	if len(connectionList) == 0:
			return False
		
	distanceList = []
	for index in range(len(connectionList)):
		distance = 0
		if connectionList[index][0] != compSide:
			distance += 3
			distance += abs(componentToPlace.y[1] - connectionList[index][1]) 
		else:
			distance += abs(componentToPlace.y[1] - connectionList[index][1])
		distanceList.append(distance)
	


	space = distanceList.index(min(distanceList))
	return (connectionList[space],distanceList[space])

def SetPosValues(placedComponent,componentToPlace,placedPin,ToPlacePin,breadboard):
	print "RUNNING SET POS VALUES"
	print componentToPlace, "component to place", ToPlacePin, "IS THE PIN We are palcing"
	print  placedComponent, "and component it amtched with is", placedPin, "IS THE PIN IT MATCHED WITH"
	if breadboard[1].xpos < placedComponent.x[placedPin] < breadboard[4].xpos:
		componentToPlace.y[ToPlacePin] = placedComponent.y[placedPin]
		if  1 < placedComponent.x[placedPin] <= breadboard[2][0].xpos+4:
			print "THE PIN IS WITHIN THE LEFT BREADBOARD SPACE"
			for k in range(4,-1,-1):
				if breadboard[2][componentToPlace.y[ToPlacePin]].Occupied[k] != False:
					pass
				else:
							
					componentToPlace.x[ToPlacePin] = breadboard[2][0].xpos + k
					breadboard[2][componentToPlace.y[ToPlacePin]].Occupied[k] = componentToPlace
					print 	componentToPlace.x[ToPlacePin], "IS THE X POSITION OF THIS PIN"
					return "PLACED"



		elif breadboard[2][0].xpos+4 < placedComponent.x[placedPin] <= breadboard[4].xpos:
			print "THE PIN IS WITHIN THE RIGHT BREADBOARD SPACE"
			for k in range(5):
				if breadboard[3][componentToPlace.y[ToPlacePin]].Occupied[k] != False:
					pass
				else:
							
					componentToPlace.x[ToPlacePin] = breadboard[3][0].xpos + k
					breadboard[3][componentToPlace.y[ToPlacePin]].Occupied[k] = componentToPlace
					print 	componentToPlace.x[ToPlacePin], "IS THE X POSITION OF THIS PIN"		
					return "PLACED"

		else:
			pass
			#POWER RAIL

	else:
		pass
		#POWER RAIL
def findOpenSpace(component,breadboard,side):
	print "RUNNING FIND OPEN SPACE"
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
	print "RUNNING DEFAULT SECOND PLACEMENT FAILED"
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
				breadboard[3][component.y[2]].Occupied[component.x[1]-breadboard[3][0].xpos] = component


		else:
			#THIS MEANS POWER-RAIL
			print 'NO PLACE'
			#findOpenSpace(component,breadboard,side)


def placeSecondPin(coordinate,distance,component,breadboard,rail):
	print "RUNNING PLACE SECOND PIN"
	side = leftOrRight(component,1)

	print side
	
	occupiedFlag = 0
	goodToPlace = 0
	print coordinate, "IS THE COORDINATE"
	if coordinate == False:
		print "ITS FALSE" + str(component)
		#THERE IS NO OTHER CONNECTION ON THE BOARD
		if side == 'LEFT':
			print "OPERATING IN THE LEFT SIDE IN THE LOCATION", breadboard[2][component.y[1]+component.pin_gap]
			print breadboard[2][component.y[1]+component.pin_gap].Occupied, " THIS IS THIS ROWS OCCUPIED STATUS"
			for k in range(5):
				if breadboard[2][component.y[1]+component.pin_gap].Occupied[k] in component.connections[2]: # FIX THIS TO CREATE A TRIGGER TO AUTOMATICALLY PLACE IT
					goodToPlace = 1
					print "THERE IS A CONNCTION FOR THIS PIN HERE, YOU NEED TO ADD SOMETHING TO DO THIS"

				elif breadboard[2][component.y[1]+component.pin_gap].Occupied[k] != False: #FIX THIS TO ALSO BE APPROVED IF ITS VALUE IS THE
					occupiedFlag = 1
					print "THIS SPACE IS OCCUPIED"
					#DO MORE STUFF
				


			if occupiedFlag == 0 or goodToPlace == 1:	
				print "THE ROW IS UNOCCUPIED"
				component.y[2] = breadboard[2][component.y[1]+component.pin_gap].ypos
				
				
				component.x[2] = component.x[1]
				
				breadboard[2][component.y[1]+component.pin_gap].Occupied[component.x[2]-breadboard[2][0].xpos] = component # MIGHT CAUSE STACKING ISSUE
				return None
			else: 
				
				print 'NO PLACE'
				defaultSecondPlacementFailed(breadboard,component,side)
				#OCCUPIED BY SOMETHING ELSE, TRY THE REVERSE DIRECTION, IF FAIL DRAW A TRACE Up TO PIN GAP AWAY FROM EMPTY SPACE
		
		elif side == 'RIGHT':
			print breadboard[3][component.y[1]+component.pin_gap].Occupied, "THIS IS THE OCCUPIED IT SHOULD HAVE SOMETHING THAT AMTCHES TO 3"
			for k in range(5):
				if breadboard[3][component.y[1]+component.pin_gap].Occupied[k] in component.connections[2]: #FIX THIS
					goodToPlace = 1
					print "THERE IS A CONNCTION FOR THIS PIN HERE, YOU NEED TO ADD SOMETHING TO DO THIS"

				elif breadboard[3][component.y[1]+component.pin_gap].Occupied[k] != False:
					occupiedFlag = 1
					print "FOUND IT CHRIS"

				
					#DO MORE STUFF
				

			if occupiedFlag == 0 or goodToPlace == 1:
				component.y[2] = breadboard[3][component.y[1]+component.pin_gap].ypos
					
				component.x[2] = component.x[1]
				breadboard[3][component.y[1]+component.pin_gap].Occupied[component.x[2]-breadboard[3][0].xpos] = component #POTENTIAL STACKING ERROR.
				return 'PLACED'

			else: 
				
				print 'NO PLACE'
				defaultSecondPlacementFailed(breadboard,component,side)

		else:
			#THIS MEANS POWER RAIL
			print 'NO PLACE'
			


	else:
		if distance == component.pin_gap:
			print "THIS IS GOING TO PLACE NICELY"
			if rail == coordinate[0]:
				direction = (coordinate[1] - component.y[1])/distance
				print "SAME SIDE AND IT IS IN THE DIRECTION", direction
				component.y[2] = component.y[1]+component.pin_gap*direction
				if breadboard[rail][component.y[2]].Occupied[component.x[1]- breadboard[rail][0].xpos] == False:
					print breadboard[rail][component.y[2]].Occupied, "FOR SOME REASON EVERYTHING WAS WEIRD WITH THIS"
					breadboard[rail][component.y[2]].Occupied[component.x[1]- breadboard[rail][0].xpos] = component
					component.x[2] = component.x[1]
					print "THE VERTICAL COMPONENT OF THE BREADBOARD IS UNOCCUPIED, WE ARE PLACING"
				else:
					print "IDEAL SPACE IS OCCUPIED, MODIFY X VALUE TO GO TO AN EMPTY SPACE"
			else:
				print "DIFFERENT SIDE"

		else:
			print "DISTANCE IS NOT EQUAL TO PIN GAP"
def dipStartingPoint(breadboard,placeDip):
	print "RUNNING DIPSTARTINGPOINT"
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
	print "RUNNNING PLACE COMPONENT"
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
		flag = 0
		CorrectIndex = 0
		matchingComponent = component.connections[1][0]
		identifyingTuple = identifyConnections(matchingComponent,breadboard)
		print "BACK IN PLACE COMPONENT"
		for Connections in matchingComponent.connections:
			for comp in matchingComponent.connections[Connections]:
				if comp == component:
					CorrectIndex = Connections-1
					print CorrectIndex, "IS THE CORRECT INDEX"

			print Connections, "THESE ARE THE MATCHED CONNECTIONS"
		# FIND PIN IN EACH SPOT, CHECK ITS CONNECTION, RAIL ROW AND TILE BECOME THE TUPLE THAT MATCHES IT
		rail = identifyingTuple[0][CorrectIndex]#THIS IS THE PROBLEM
		Row = identifyingTuple[1][CorrectIndex]
		Tile = identifyingTuple[2][CorrectIndex]
		print rail, Row, Tile
		print identifyingTuple[0],identifyingTuple[1],identifyingTuple[2]
		
		for i in breadboard[rail][Row].Occupied[Tile].connections:
			print breadboard[rail][Row].Occupied[Tile].connections[i], "IS ITS CONNECTIONS"
			print component
			for test in range(len(breadboard[rail][Row].Occupied[Tile].connections[i])):
				if breadboard[rail][Row].Occupied[Tile].connections[i][test] == component: 
					print "FLAG RAISED" #THIS WORKS
					flag = 1
			if flag ==1:	
				
				SetPosValues(breadboard[rail][Row].Occupied[Tile],component,i,1,breadboard)
				print "BACK IN PLACE COMPONENT"
				if len(component.connections[2]) != 0:
					values = closestConnections(component.connections[2][0],breadboard,component) #SHOULD THIS BE THE CONNECTION WE ARE MATCHING TO?
				else:
					values = False
				print "BACK IN PLACE COMPONENT"
				if values == False:
					distance = False
					coordinate = False
				else:
					print values, "THESE ARE THE CLOSEST REFERENCE OF RESISTOR 2"
					distance = values[1]
					coordinate = values[0]
				print component, "Trying to place second pin"
				placeSecondPin(coordinate,distance,component,breadboard,rail)
				print "BACK IN PLACE COMPONENT"
				print component.x[1]
				return None
				

			
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

	Resistor1 = resistor(1,4,5,'h',{1:[],2:[]})
	Resistor2 = resistor(2,4,7,'h',{1:[],2:[]})
	Resistor3 = resistor(3,4,5,'h',{1:[],2:[]})
	DIP = dip(4,5,'h',{},'dip',number_of_pins = 12, pin_gap = 3)
	#DIP2 = dip(4,5,'h',{3:[Resistor2]},'dip',number_of_pins = 8, pin_gap = 3)
	

	board[3][14].Occupied[0] = True
	board[3][9].Occupied[0] = True
	

	placeFirstComponent(DIP,board)
	DIP.connections[12] = [Resistor1]
	Resistor1.connections[1] = [DIP]
	
	placeComponent(Resistor1,board)
	print "FIRST COMPONENT PLACED"
	
	Resistor1.connections[2] = [Resistor2]
	Resistor2.connections[1] = [Resistor1]
	DIP.connections[12].append(Resistor2)
	placeComponent(Resistor2,board)

	print "SECOND COMPONENT PLACED"
	''' IN PARALLEL
	#Resistor3.connections[1] = [Resistor1,Resistor2]
	#Resistor3.connections[2] = [Resistor2]
	#Resistor1.connections[2].append(Resistor3)
	#Resistor2.connections[2].append(Resistor3)
	#Resistor2.connections[1] = [Resistor1]
	'''
	Resistor3.connections[1] = [Resistor2]
	Resistor2.connections[2].append(Resistor3)

	placeComponent(Resistor3,board)
	print "THIRD COMPONENT PLACED"
	

	#placeComponent(Resistor3,board)
	#placeComponent(Resistor3,board)
	#placeComponent(DIP2,board)
	#board[2][8].Occupied[1] = DIP
	print DIP.x
	print DIP.y
	print Resistor1.x
	print Resistor1.y
	print Resistor2.x
	print Resistor2.y
	print Resistor3.x
	print Resistor3.y
	print board[3][12].Occupied
	print board[3][15].Occupied
	print board[3][11].Occupied
	
	
	#print board[3][13].Occupied
	#print board[3][13].Occupied
	
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

	
	