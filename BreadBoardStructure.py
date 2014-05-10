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

def placeFirstComponent(component,breadboard,compList):
	compList.append(component)
	print component.number_of_pins
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
	print "WITHIN IDENTIFY CONNECTIONS COMP IS",component
	print breadboard[4].Occupied
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
							print 'THERE IS A FRICKEN CONNECTION'
							returnRail.append(rail)
							returnRow.append(tile)
							returnTile.append(0)
	return (returnRail,returnRow,returnTile)

def closestConnections(component,breadboard,componentToPlace):
	print "RUNNING CLOSESTCONNECTIONS"
	print "COMPONENT IS", component
	print "WHAT WE ARE PLACING IS", componentToPlace
	if 1 < component.x[1] < 10:
		compSide = 2
	elif 10 < component.x[1] < 17:
		compSide = 3

	elif component.x[1] < 2:
		compSide = component.x[1]
	else:
		compSide = component.x[1] -13
	print "OUR COMPONENT IS ON WHAT COMPSIDE (3)", compSide
	connectionList = []
	#FIRST CHECK FOR SAME PANEL
	for panel in range(len(breadboard)):
		if 1 < panel < 4:
			for row in range(len(breadboard[panel])):

				for tile in range(5):

				#	if compSide == panel and component.y[1] == row:
				#		pass
				#	else:
					if breadboard[panel][row].Occupied[tile] == component:
						connectionList.append((panel,row))
						print breadboard[panel][row].Occupied[tile], component, "THIS IS BREADBOARD NAME AND COMPONENT"
						

		else:
			for tile in range(breadboard[0].length):
				if breadboard[panel].Occupied[tile] == component:
					connectionList.append((panel,component.y[1]))

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

def defaultSecondPlacementFailed(breadboard,component,side,compList):
	print "RUNNING DEFAULT SECOND PLACEMENT FAILED"
	occupiedFlag = 0
	if component.y[1] < component.pin_gap:
		if component.x[1] < 10:
			openSpot =findOpenSpace(component,breadboard,2)
			print "NEXT OPEN SPOT IS", openSpot
			xpos = component.x[1]
			ypos = component.y[1]
			Trace = trace(xpos,ypos,xpos,openSpot,component.connections[1][-1],component.connections[1][-1])
			compList.append(Trace)
			print "ADDED TRACE LINE 223"
			breadboard[2][ypos].Occupied[xpos-breadboard[2][0].xpos] = Trace
			breadboard[2][openSpot].Occupied[xpos-breadboard[2][0].xpos] = Trace
			print "WE PLACED A TRACE"
			for k in range(4,1,-1):
				if breadboard[2][openSpot].Occupied[k] == False:

					component.x[1] = breadboard[2][0].xpos + k
					component.y[1] = openSpot
					component.x[2] = component.x[1]
					component.y[2] = openSpot + component.pin_gap
					breadboard[2][openSpot].Occupied[k] = component
					breadboard[2][component.y[2]].Occupied[k] = component
					return None


		else:
			openSpot =findOpenSpace(component,breadboard,3)
			print "NEXT OPEN SPOT IS", openSpot
			xpos = component.x[1]
			ypos = component.y[1]
			Trace = trace(xpos,ypos,xpos,openSpot,component.connections[1][-1],component.connections[1][-1])
			compList.append(Trace)
			print "ADDED TRACE LINE 246"
			breadboard[3][ypos].Occupied[xpos-breadboard[2][0].xpos] = Trace
			breadboard[3][openSpot].Occupied[xpos-breadboard[2][0].xpos] = Trace
			print "WE PLACED A TRACE"
			for k in range(5):
				if breadboard[3][openSpot].Occupied[k] == False:

					component.x[1] = breadboard[2][0].xpos + k
					component.y[1] = openSpot
					component.x[2] = component.x[1]
					component.y[2] = openSpot + component.pin_gap
					breadboard[3][openSpot].Occupied[k] = component
					breadboard[3][component.y[2]].Occupied[k] = component
					return None
		#FIND NEXT OPEN SPOT TO PLACE COMPONENT THEN DRAW TRACE DO DRAW TRACE FUNCTION
	else:
		if side == 'LEFT':
			print "WE ARE ON THE LEFT"
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
				Tracer = trace(component.x[1],component.y[1],component.x[1],component.y[2],[component.connections[1]],[component.connections[1]])
				compList.append(Tracer)
				print "ADDED TRACE LINE 288"
				breadboard[2][component.y[2]].Occupied[component.x[1]] = component
		
		elif side == 'RIGHT':
			print "WE ARE ON THE RIGHT"
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
				Trace = trace(component.x[1],component.y[1],component.x[1],component.y[2],[component.connections[1]],[component.connections[1]])
				compList.append(Trace)
				print "ADDED TRACE LINE 315"
				breadboard[3][component.y[2]].Occupied[component.x[1]-breadboard[3][0].xpos] = component


		else:
			#THIS MEANS POWER-RAIL
			print 'NO PLACE'
			#findOpenSpace(component,breadboard,side)


def placeSecondPin(coordinate,distance,component,breadboard,rail,compList):
	print "RUNNING PLACE SECOND PIN"
	side = leftOrRight(component,1)
	if side == 'LEFT':
		sideNumber = 2
	else:
		sideNumber = 3

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
				defaultSecondPlacementFailed(breadboard,component,side,compList)
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
				defaultSecondPlacementFailed(breadboard,component,side,compList)

		else:
			#THIS MEANS POWER RAIL
			print 'NO PLACE'
			

	elif 2 > coordinate[0] or coordinate[0] > 3:
		print "WE ON A RAIL BROSKI" 
		direction = (coordinate[0] - component.x[1])/abs(coordinate[0] - component.x[1])
		print abs(coordinate[0] - component.x[1])
		if abs(coordinate[0] - component.x[1]) > 9:
			spaces = 2
			
		else:
			spaces = 1

		if spaces == 1:
			print "ONE GAP BROSKI"
			if component.x[1] < 10:
				#LEFT

				if component.x[1] > component.connections[2][-1].x[1]: # FIX THIS IT SWAPS WRONG COMPONENET
					print "COMPONENT IS FARTHER RIGHT THAN ITS CONNECTION"
					if breadboard[2][component.y[1]].Occupied[0]  != False:
						moveComponentOneFromEdge(component,breadboard,sideNumber,-1)
					else:
						pass


					breadboard[2][component.y[1]].Occupied[component.x[1]-breadboard[2][0].xpos] = False
					component.x[1] = breadboard[2][0].xpos
					breadboard[2][component.y[1]].Occupied[0] = component

					component.x[2] = component.connections[2][-1].x[1]
					component.y[2] = component.y[1]

					breadboard[component.connections[2][-1].x[1]].Occupied[component.y[1]] = True

				



				
			else:
				#right
				if breadboard[3][component.y[1]].Occupied[4]  != False:
					print "RUNNING MOVECOMPONENTFROMEDGE"
					moveComponentOneFromEdge(component,breadboard,sideNumber,-1)
				else:
					pass
				breadboard[3][component.y[1]].Occupied[component.x[1]-breadboard[3][0].xpos] = False
				component.x[1] = breadboard[3][0].xpos+4
				breadboard[3][component.y[1]].Occupied[4] = component

				component.x[2] = component.connections[2][-1].x[1]
				component.y[2] = component.y[1]

				breadboard[component.connections[2][-1].x[1]-13].Occupied[component.y[1]] = True

		else:
			print "THIS IS THE COMPONENTS X1 POSITION", component.x[1]
			if component.x[1] < 10:
				if breadboard[2][component.y[1]].Occupied[4] == False and breadboard[3][component.y[1]].Occupied[0] == False:
					pass
				
					
				elif breadboard[3][component.y[1]].Occupied[0] == False:
					moveComponentOneFromEdge(component,breadboard,sideNumber,1)
				else: 
					if breadboard[2][component.y[1]+1].Occupied[component.x[1]- breadboard[2][4].xpos] == False:
						Trace = trace(component.x[1],component.y[1],component.x[1],component.y[1]+1,component,component)
						compList.append(Trace)
						print "ADDED TRACE LINE 469"
						component.y[1] = component.y[1] + 1 # ADD MORE HERE
						breadboard[2][component.y[1]+1].Occupied[component.x[1]-breadboard[2][0].xpos] = component					

				component.x[1] = breadboard[2][4].xpos + 4
				breadboard[2][component.y[1]].Occupied[4] = component
				component.x[2] = component.x[1] + component.pin_gap
				component.y[2] = component.y[1]
				breadboard[3][component.y[1]].Occupied[component.x[2]-breadboard[2][0].xpos] = component
				#DETERMINE CORRECT INDEX
				index = indexFinder(component,component.connections[2][-1])
				
				finalTrace = trace(breadboard[3][0].xpos,component.y[1],component.connections[2][-1].x[1],component.y[1],component.connections[2][-1],component.connections[2][-1])
				compList.append(finalTrace)
				print "ADDED TRACE LINE 481"
				breadboard[3][component.y[1]].Occupied[4] = component.connections[2][-1]
			
			else:
				if breadboard[3][component.y[1]].Occupied[0] == False and breadboard[2][component.y[1]].Occupied[4] == False:
					print "WERE GONNA DO TRACE REALTED STUFF HERE"

				elif breadboard[2][component.y[1]].Occupied[4] == False:
					print "RUNNING MOVE COMPONENT"
					moveComponentOneFromEdge(component,breadboard,sideNumber,1)

				else: 
					print "IN THE ELSE CONDITION OF 2 SPACE"
					if breadboard[3][component.y[1]+1].Occupied[component.x[1] - breadboard[3][0].xpos] == False:
						print "THE NEXT SPACE IS UNOCCUPIED"
						Trace = trace(component.x[1],component.y[1],component.x[1],component.y[1]+1,component,component)
						compList.append(Trace)
						print "ADDED TRACE LINE 498"
						print "THIS IS THE COMPONENTS INITIAL Y VALUE", component.y[1]
						component.y[1] = component.y[1] + 1 # ADD MORE HERE
						breadboard[3][component.y[1]+1].Occupied[component.x[1]-breadboard[3][0].xpos] = component
					
				component.x[1] = breadboard[3][0].xpos
				breadboard[3][component.y[1]].Occupied[0] = component
				component.x[2] = component.x[1] - component.pin_gap
				component.y[2] = component.y[1]
				breadboard[2][component.y[1]].Occupied[component.x[2]-breadboard[2][0].xpos] = component
				finalTrace = trace(breadboard[2][0].xpos,component.y[1],component.connections[2][-1].x[1],component.y[1],component.connections[2][-1],component.connections[2][-1])
				compList.append(finalTrace)
				print "ADDED TRACE LINE 509"
				breadboard[2][component.y[1]].Occupied[0] = component.connections[2][-1]

						# MAKE IT GO ACROSS GAP AND TRACE TO ITS CONNECTION


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
			if rail != coordinate[0]:
				print "ITS ON A DIFFERENT SIDE"
				if component.x[1] < 10:
					direction = 1
				else:
					direction = -1
				
				print "WE NEED TO GO IN THE DIRECTION", direction
				

				if direction == 1:
					if (breadboard[2][component.y[1]].Occupied[4]  == False or breadboard[2][component.y[1]].Occupied[4] == component) and breadboard[3][component.y[1]].Occupied[0] == False:
						pass
					elif breadboard[3][component.y[1]].Occupied[0] == False:
						moveComponentOneFromEdge(component,breadboard,sideNumber,1) 
					else:
						for k in range(10):
							if breadboard[2][component.y[1]+k].Occupied[component.x[1]- breadboard[2][4].xpos] == False and breadboard[3][component.y[1]+k].Occupied[0] == False:
								Trace = trace(component.x[1],component.y[1],component.x[1],component.y[1]+k,component,component)
								compList.append(Trace)
								print "ADDED TRACE LINE 554"
								component.y[1] = component.y[1] + k # ADD MORE HERE
								breadboard[2][component.y[1]+k].Occupied[component.x[1]-breadboard[2][0].xpos] = component
								break

						
					print component.y[1], "THIS SHOULD BE 4"
					breadboard[2][component.y[1]].Occupied[component.x[1]-breadboard[2][0].xpos] = False
					component.x[1] = breadboard[2][0].xpos+4
					breadboard[2][component.y[1]].Occupied[4] = component

					component.x[2] = breadboard[3][0].xpos
					component.y[2] = component.y[1]

					breadboard[3][component.y[1]].Occupied[0] = component

					index = indexFinder(component,component.connections[2][-1])

					
				else:
					if (breadboard[3][component.y[1]].Occupied[0]  == False or breadboard[3][component.y[1]].Occupied[0] == component) and breadboard[2][component.y[1]].Occupied[4] == False:
						pass
					elif breadboard[2][component.y[1]].Occupied[4] == False:
						moveComponentOneFromEdge(component,breadboard,sideNumber,1) 
					else:
						for k in range(10):
							if breadboard[3][component.y[1]+k].Occupied[component.x[1]- breadboard[3][0].xpos] == False and breadboard[2][component.y[1]+k].Occupied[4] == False:
								Trace = trace(component.x[1],component.y[1],component.x[1],component.y[1]+k,component,component)
								compList.append(Trace)
								print "ADDED TRACE LINE 581"
								component.y[1] = component.y[1] + k # ADD MORE HERE
								breadboard[3][component.y[1]+k].Occupied[component.x[1]-breadboard[3][0].xpos] = component
								break

					print component.y[1], "THIS SHOULD BE 4"
					breadboard[3][component.y[1]].Occupied[component.x[1]-breadboard[3][0].xpos] = False
					component.x[1] = breadboard[3][0].xpos
					breadboard[3][component.y[1]].Occupied[0] = component

					component.x[2] = breadboard[2][0].xpos+4
					component.y[2] = component.y[1]

					breadboard[2][component.y[1]].Occupied[4] = component
					
				conComp = component.connections[2][-1]
				for number in conComp.connections:
					for index in conComp.connections[number]:
						if index == component:
							value = number
					
				upOrDown = conComp.y[value] - component.y[2]
				print "CONNECTION IS EITHER UP OR DOWN", upOrDown
				if upOrDown != 0:
					for k in range(5):
						if breadboard[rail][component.y[2]].Occupied[k] == False and breadboard[rail][component.y[2]+upOrDown].Occupied[k] == False:
							Trace = trace(breadboard[rail][0].xpos + k, component.y[2], breadboard[rail][0].xpos + k, component.y[2]+upOrDown,component,component)
							compList.append(Trace)
							print "ADDED RACE LINE 618"
							breadboard[rail][component.y[2]].Occupied[k] = component
							breadboard[rail][component.y[2]+upOrDown].Occupied[k] = component
							return None


				

				else:
					return None

			else:
				print "WE ARE ON THE SAME SIDE"
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

def placeComponent(component,breadboard,compList):
	compList.append(component)
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
		matchingComponent = component.connections[1][-1]
		print matchingComponent , "IS THE MATCHING COMPONENT WHY DO WE HAVE AN ERROR"
		identifyingTuple = identifyConnections(matchingComponent,breadboard)
		print "BACK IN PLACE COMPONENT", identifyingTuple
		for Connections in matchingComponent.connections:
			print matchingComponent.connections, "THESE ARE TEH CONNECTIONS WHY IS THERE AN ERROR"
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
		if rail ==2 or rail ==3:
			pass
		else:
			matchingComponent = component.connections[2][0]
			print matchingComponent
			identifyingTuple = identifyConnections(matchingComponent,breadboard)
			print identifyingTuple, "This is teh spot of the connection"
			rail = identifyingTuple[0][CorrectIndex]#THIS IS THE PROBLEM
			Row = identifyingTuple[1][CorrectIndex]
			Tile = identifyingTuple[2][CorrectIndex]
			current1 = component.connections[1]
			current2 = component.connections[2]
			component.connections[1] = current2
			component.connections[2] = current1
			for Connections in matchingComponent.connections:
				for comp in matchingComponent.connections[Connections]:
					if comp == component:
						CorrectIndex = Connections-1
						print CorrectIndex, "IS THE CORRECT INDEX"


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
					values = closestConnections(component.connections[2][-1],breadboard,component) #SHOULD THIS BE THE CONNECTION WE ARE MATCHING TO?
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
				placeSecondPin(coordinate,distance,component,breadboard,rail,compList)
				print "BACK IN PLACE COMPONENT"
				print component.x[1]
				return None
				

			
def leftOrRight(component,pin):
	
	if 1 < component.x[pin] <= 8:
		return 'LEFT'
	elif 10 <component.x[pin] < 17: 
		return 'RIGHT'

	else :
		return "RAIL"


def moveComponentOneFromEdge(component,breadboard,side,tile):
	print "RUNNING MOVE COMPONENT ONE FROM EDGE"
	if component.name == 'dip':
		return component.number_of_pins
	if side == 2:
		if tile == 1:
			componentToMove = breadboard[side][component.y[1]].Occupied[4]
			InitialTile = 4
		else:
			componentToMove = breadboard[side][component.y[1]].Occupied[0]
			InitialTile = 0
	else:

		if tile == 1:
			componentToMove = breadboard[side][component.y[1]].Occupied[0]
			InitialTile = 0
		else:
			componentToMove = breadboard[side][component.y[1]].Occupied[4]
			InitialTile = 4



	for tile in range(5):
		print componentToMove
		if breadboard[side][componentToMove.y[1]].Occupied[tile] == False and breadboard[side][componentToMove.y[2]].Occupied[tile] == False:
			breadboard[side][componentToMove.y[1]].Occupied[tile] = componentToMove
			breadboard[side][componentToMove.y[2]].Occupied[tile] = componentToMove
			breadboard[side][componentToMove.y[1]].Occupied[InitialTile] = False
			breadboard[side][componentToMove.y[2]].Occupied[InitialTile] = False
			componentToMove.x[1] = breadboard[side][0].xpos + tile
			componentToMove.x[2] = breadboard[side][0].xpos + tile
			print "SUCCESSFULLY SWAPPED POSITIONS"
			return None
		else:
			pass

def indexFinder(component,matchedComp):
	for number in matchedComp.connections:
		for index in matchedComp.connections[number]:
			if index == component:
				return number

if __name__ == '__main__':

	board = createBreadboard()

	#SET RAIL VALUES INITIALLY DO THAT
	GND = power('GROUND',[])
	V5 = power('5 volts',[])
	V2 = power('2 volts',[])
	board[0].Occupied[0] = GND
	GND.x[1] = 0
	GND.y[1] = 0
	board[1].Occupied[0] = V2
	board[4].Occupied[0] = V2
	board[5].Occupied[0] = V5


	Resistor1 = resistor(1,0,0,4,5,'h',{1:[],2:[]})
	Resistor2 = resistor(2,0,0,4,7,'h',{1:[],2:[]})
	Resistor3 = resistor(3,0,0,4,5,'h',{1:[],2:[]})
	Resistor4 = resistor(4,0,0,4,5,'h',{1:[],2:[]})
	Resistor5 = resistor(5,0,0,4,5,'h',{1:[],2:[]})
	Resistor6 = resistor(6,0,0,4,5,'h',{1:[],2:[]})
	DIP = dip(0,0,4,5,'h',{},'dip',number_of_pins = 8, pin_gap = 2)
	#DIP2 = dip(4,5,'h',{3:[Resistor2]},'dip',number_of_pins = 8, pin_gap = 3)
	

	board[3][14].Occupied[0] = True
	board[3][9].Occupied[0] = True
	
	""" TEST CASE TO DATE
	placeFirstComponent(DIP,board)
	DIP.connections[8] = [Resistor1]
	Resistor1.connections[1] = [DIP]
	
	placeComponent(Resistor1,board)
	print "FIRST COMPONENT PLACED"
	
	Resistor1.connections[2] = [Resistor2]
	Resistor2.connections[1] = [Resistor1]
	DIP.connections[8].append(Resistor2)
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

	Resistor4.connections[1] = [GND]
	Resistor4.connections[2] = [Resistor3]
	Resistor3.connections[2].append(Resistor4)
	GND.connections[1].append(Resistor4)
	placeComponent(Resistor4,board)
	print "FOURTH COMPONENT PALCED"
	Resistor5 = resistor(5,0,0,4,5,'h',{1:[],2:[]})
	DIP.connections[3] = []
	DIP.connections[3].append(Resistor5)
	Resistor5.connections[1].append(DIP)
	placeComponent(Resistor5,board)

	Resistor6.connections[1].append(Resistor5)
	Resistor5.connections[2].append(Resistor6)
	Resistor6.connections[2].append(Resistor4)
	Resistor4.connections[2].append(Resistor6)
	print "PLACING COMPONENT SIX"
	placeComponent(Resistor6,board)

	#placeComponent(Resistor3,board)
	#placeComponent(Resistor3,board)
	#placeComponent(DIP2,board)
	#board[2][8].Occupied[1] = DIP

	"""


	compList = []
	#placeFirstComponent(Resistor1,board,compList)
	"""
	Resistor1.connections[2].append(Resistor2)
	Resistor2.connections[1].append(Resistor1)
	Resistor2.connections[2].append(GND)
	print "PLACIGN COMPONENT TWO"
	placeComponent(Resistor2,board,compList)

	Resistor3.connections[1].append(Resistor2)
	Resistor2.connections[1].append(Resistor3)
	placeComponent(Resistor3,board,compList)

	Resistor4.connections[1].append(Resistor3)
	Resistor3.connections[2].append(Resistor4)
	placeComponent(Resistor4,board,compList)

	Resistor4.connections[2].append(GND)

	placeComponent(Resistor4,board,compList)
	"""
	placeFirstComponent(DIP,board,compList)
	for i in range(DIP.number_of_pins+1):
		DIP.connections[i] = []
	Resistor1.connections[1].append(DIP)
	Resistor1.connections[2].append(DIP)
	DIP.connections[5].append(Resistor1)
	DIP.connections[8].append(Resistor1)
	placeComponent(Resistor1,board,compList)
	print DIP.x
	print DIP.y
	print Resistor1.x
	print Resistor1.y
	print "RESISTOR 2 STUFF"
	print Resistor2.x
	print Resistor2.y
	print "RESISTOR 3 STUFF"
	print Resistor3.x
	print Resistor3.y
	print "RESISTOR 4 STUFF"
	print Resistor4.x
	print Resistor4.y
	print "RESISTOR 5 STUFF"
	print Resistor5.x
	print Resistor5.y
	print "RESISTOR 6 STUFF"
	print Resistor6.x
	print Resistor6.y
	print board[3][12].Occupied
	print board[2][1].Occupied
	print compList
	
	
	#IF OCCUPIED DRAW TRACE TO NEXT? THEN TO UNOCCUPIED 
	
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

	
	