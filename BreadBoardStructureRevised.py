from ComponentModule import *
from BreadboardModule import *

def placeFirstComponent(component,breadboard,compList):
	compList.append(component)
	print component.number_of_pins
	for i in range(component.number_of_pins+1):
		if i == 0:
			pass
		elif i % 2 == 1:
			component.x[i] = 7

		else:
			component.x[i] = 9

	for i in range(component.number_of_pins/2):

		component.y[i*2+1] = i
		component.y[i*2+2] = i


		breadboard[2][i].Occupied[4] = [component, 2*i+1]

		breadboard[3][i].Occupied[0] = [component, 2*i + 2]

def drawTrace(startSpot,endSpot,breadboard,component,compPin,compList):
	""" TEH LOWER VALUED ONE SHOT BE THE FIRST ONE"""
	print "RUNNING DRAW TRACE"
	count = 0
	vdir = (endSpot[1]-startSpot[1])/abs(endSpot[1]-startSpot[1])
	if vdir == 0:
		return False
	if startSpot[0] == endSpot[0]:
		print "DRAWING TRACE ON SAME SIDE"
		for k in range(5):
			count = 0
			for tile in range(startSpot[1],endSpot[1],1*vdir):
				if breadboard[startSpot[0]][tile].Occupied[k][0] == False:
					count += 1 
			print count, endSpot[1] - startSpot[1], "IF THIS IS EQUAL WE WILL DRAW A TRACE"
			if count == abs(endSpot[1] - startSpot[1]):
				Trace = trace(0,0,0,0,0,'h',{1:component,2:component},abs(endSpot[1]-startSpot[1]))
				Trace.x[1] = k + breadboard[startSpot[0]][0].xpos
				Trace.x[2] = k + breadboard[startSpot[0]][0].xpos
				Trace.y[1] = startSpot[1]
				Trace.y[2] = endSpot[1]
				breadboard[startSpot[0]][startSpot[1]].Occupied[k] = [component,compPin]
				breadboard[endSpot[0]][endSpot[1]].Occupied[k] = [component,compPin]
				for i in range(Trace.pin_gap-1):
					breadboard[startSpot[0]][startSpot[1]+i*vdir+1*vdir].Occupied[k] = [True]

				compList.append(Trace)
				print breadboard[startSpot[0]][startSpot[1]].Occupied[k]
				print breadboard[endSpot[0]][endSpot[1]].Occupied[k]
				return None





def findOpenSpace(start,breadboard,side):
	print "RUNNING FIND OPEN SPACE"
	closest = []
	badness = 0
	found = 0
	if side == 2 or side == 3:
		for i in range(start,breadboard[0].length-2):
			
			for k in range(5):
				if len(breadboard[side][i].Occupied[k]) == 2 or len(breadboard[side][i+2].Occupied[k]) == 2:
					badness = 1
					
			if badness == 0:
				for l in range(5):
					if breadboard[side][i].Occupied[l][0] == False and breadboard[side][i+1].Occupied[l][0] == False and breadboard[side][i+2].Occupied[l][0] == False:
						print "WE HAVE A MATCH"
						return (side,i,l)
			badness = 0
		return False


	else:
		pass

def pinFinder(component,matchedComp,PlacePin = False):
	if PlacePin == False:
		for number in matchedComp.connections:
			for index in matchedComp.connections[number]:
				if index == component:
					return number
	else:
		if component.x[PlacePin] < 8:
			side = 2

		else:
			side = 3

		for number in matchedComp.connections:
			if matchedComp.x[number] < 8:
				Compside = 2
			else:
				Compside = 3

			print side, Compside
			for index in matchedComp.connections[number]:

				if index == component and (matchedComp.y[number] != component.y[PlacePin] or side != Compside):
					return number


def identifyConnections(component,breadboard,pin):
	""" RETURNS list of (x,y) and rail of the pins position, pin is the pin of the component you are fingin the location of"""
	returnRail = []
	returnRow = []
	returnTile = []
	for rail in range(6):
		if rail == 2 or rail == 3:
			for row in range(30):
				for tile in range(5):
					if breadboard[rail][row].Occupied[tile][0] == component:
						if breadboard[rail][row].Occupied[tile][1] == pin:
							returnRail.append(rail)
							returnRow.append(row)
							returnTile.append(tile)

					else:
						pass



		else:
			for row in range(30):
				if breadboard[rail].Occupied[row] == component:
					return (returnRail)
	return (returnRail,returnRow,returnTile)



def findConnections(component,pinCheck = False):
	""" pinCHeck is flase if this is the first pin we are finding connections to toehrwise, pinCHeck is the pin we are trying to find its connections to"""
	if pinCheck == False:
		for pin in component.connections:
			if component.connections[pin] == []:
				pass
			else:
				return [component.connections[pin][-1],pin]
		return False
	else:
		if component.connections[pinCheck] == []:
			return False
		else: 
			return [component.connections[pinCheck][-1],pinCheck] 



def PlaceComponent(component,breadboard,compList):
	matchedComp = findConnections(component)
	print matchedComp
	if matchedComp[0] == False:
		#THERE IS NO MATCHED CONNECTION ON THE BOARD
		pass

	else:
		#THERE IS A MATCHED CONNECTION ON THE BOARD
		matchedPin = pinFinder(component,matchedComp[0])
		print "MATCHED PIN IS", matchedPin
		location = identifyConnections(matchedComp[0],breadboard,matchedPin)
		print "location we are palcing is", location
		PlaceFirstPin(component,breadboard,location,matchedComp[1])
		print "FIRST PIN PLACE AT", component.x, component.y
		print matchedComp, "THIS IS THE COMPONENT WE MATCHED TO."

		#NEED TO INSERT PROTOCOL FOR DEALING WITH FULL ROW HERE, PLACE FIRST PIN RETURNS FALSE

		if matchedComp[1] == 1:
			pinTwo = 2
		else:
			pinTwo = 1
		print "WEVE ALREADY PLACED", matchedComp[1], "WE ARE NOW PLACING", pinTwo
		PlaceSecondPin(component,breadboard,pinTwo,matchedComp[1],compList)
		compList.append(component)


def PlaceSecondPin(component,breadboard,pinToPlace,PlacedPin,compList):
	#THERE SHOUDL BE SOEMTHING IN THIS TO USE TEH CLOSEST RAIL ROW ADN TILE VALUES
	print "RUNNING PLACESECONDPIN"
	matchedComp = findConnections(component,pinToPlace)
	print matchedComp, "FIRST MATCHED COMP"
	compLocation = identifyConnections(component,breadboard,PlacedPin)
	count = 0
	rail = compLocation[0][-1]
	row = compLocation[1][-1]
	tile = compLocation[2][-1]
	print rail, row, tile, "THESE ARE RAIL ROW AND TILE"
	if matchedComp == False:
		flag = 0

		for i in range(5):
			if len(breadboard[rail][row+2].Occupied[i]) == 2:
				flag = 1


		#NO COMPONENT CONNECTED TO SECOND PIN PLACE VERTICALLY
		for tiles in range(component.pin_gap):
			print breadboard[rail][row+2].Occupied[tile]
			if breadboard[rail][row+tiles+1].Occupied[tile][0] == False:
				count += 1

			
			else:
				pass
		if count == component.pin_gap and flag == 0:
			print "WE AVE FOUND AN OPEN SPOT TO PUT THE COMPONENT"
			component.x[pinToPlace] = component.x[PlacedPin]
			component.y[pinToPlace] = component.y[PlacedPin] + 2
			breadboard[rail][row+2].Occupied[tile] = [component,pinToPlace]
			breadboard[rail][row+1].Occupied[tile] = [True]
			return None

			#PLACE PIN HERE
		elif flag == 1:
			print "ANOTHER COMPONENT IS IN THIS SPACE SORRY"
			#MUST FIND NEW SPACE THIS SPACE IS OCCUPIED MY ANOTHER COMPONENT
			openSpace = findOpenSpace(component.y[PlacedPin],breadboard,rail)
			if openSpace != False:
				breadboard[rail][row].Occupied[tile] = [False]
				component.x[PlacedPin] = openSpace[2]+ breadboard[rail][0].xpos
				component.x[pinToPlace] = component.x[PlacedPin]
				component.y[PlacedPin] = openSpace[1]
				component.y[pinToPlace] = openSpace[1]+2
				breadboard[openSpace[0]][openSpace[1]].Occupied[openSpace[2]] = [component,PlacedPin]
				breadboard[openSpace[0]][openSpace[1]+1].Occupied[openSpace[2]] = [True]
				breadboard[openSpace[0]][openSpace[1]+2].Occupied[openSpace[2]] = [component,pinToPlace]
				drawTrace((rail,row),(rail,component.y[PlacedPin]),breadboard,component,PlacedPin,compList)

			else:
				print "THERE ARE NO OPEN SPOTS ON TEH BREADBOARD.LOL"
				pass
		else:
			print "COMPONENT IN SPOT WE ARE MOVING OVER"
			for k in range(5):
				if breadboard[rail][row].Occupied[k][0] == False and breadboard[rail][row+1].Occupied[k][0] == False and breadboard[rail][row+ 2].Occupied[k][0] == False:

					breadboard[rail][row].Occupied[tile] = [False]
					component.x[pinToPlace] = breadboard[rail][row].xpos + k
					component.x[PlacedPin] = breadboard[rail][row].xpos + k 
					breadboard[rail][row].Occupied[k] = [component,PlacedPin]
					breadboard[rail][row+2].Occupied[k] = [component,pinToPlace]
					breadboard[rail][row+1].Occupied[k] = [True]

					component.y[pinToPlace] = component.y[PlacedPin] + 2
					return None

			




	else:
		print "THERE IS A CONNECTION TO ANOTHER COMPONENT"
		# CONNECTION TO SECOND PIN DETERMINE DIRECTIONS AND PLACE TOWARDS IT
		print matchedComp[0], "THIS IS MATCHED COMP"
		print PlacedPin
		pin = pinFinder(component,matchedComp[0],PlacedPin)
		print pin, "THIS IS THE PIN OF THE COMPONENT WE MATCHED WITH"
		matchLocation = identifyConnections(matchedComp[0],breadboard,pin)
		print matchLocation, "IS MATCHLOCATION"
		print compLocation, "IS COMPLOCATION"
		if matchLocation[0][0] - compLocation[0][0] == 0:
			Hordirection = 0
		else:
			Hordirection = (matchLocation[0][0] - compLocation[0][0])/abs(matchLocation[0][0] - compLocation[0][0])
		VerDistance = (matchLocation[1][0] - compLocation[1][0])
		if (matchLocation[1][0] - compLocation[1][0]) == 0:
			Verdirection = 0
		else:
			Verdirection = (matchLocation[1][0] - compLocation[1][0])/abs(matchLocation[1][0] - compLocation[1][0])
		side = rail
		if Hordirection == 0:
			print "WE ARE ON THE SAME SIDE OF THE BOARD"
			print VerDistance, "IS THE VERTICAL DISTANCE", component.pin_gap, "IS THE PIN GAP"
			#THIS MEASN SAME SIDE IF ITS NOT WELL HAVE TO DO OTHER THINGS
			if abs(VerDistance) == component.pin_gap:
				print "COMPONENT IS THE CORRECT DISTANCE AWAY"
				#COMPONENT IS THE RIGHT DISTANCE AWAY, INCLUDES LOGIC FOR UP AND DOWN 
				for l in range(5):
					if breadboard[side][component.y[PlacedPin]].Occupied[l][0] == False and breadboard[side][component.y[PlacedPin]+1*Verdirection].Occupied[l][0] == False and breadboard[side][component.y[PlacedPin]+2*Verdirection].Occupied[l][0] == False:
						breadboard[component.y[PlacedPin]].Occupied[component.x[PlacedPin]-breadboard[side][0].xpos] = [False]
						component.x[PlacedPin] = breadboard[side][0].xpos + l
						component.x[pinToPlace] = breadboard[side][0].xpos + l
						component.y[pinToPlace] = matchLocation[1][0]
						breadboard[rail][component.y[PlacedPin]+1*Verdirection].Occupied[l] = [True]
						breadboard[rail][component.y[PlacedPin]].Occupied[l] = [component,PlacedPin]
						breadboard[rail][component.y[PlacedPin]+2*Verdirection].Occupied[l] = [component,pinToPlace]
						print "PIN TWO PLACED"
						return None
			else:
				
				#COMPONENT IS WRONG DISTANCE AWAY
				flag = 0
				for k in range(5):
					if len(breadboard[side][component.y[PlacedPin]+2*Verdirection].Occupied[k]) == 2:
						flag = 1

				if flag == 0:

					for l in range(5):
						if breadboard[side][component.y[PlacedPin]].Occupied[l][0] == False and breadboard[side][component.y[PlacedPin]+1*Verdirection].Occupied[l][0] == False and breadboard[side][component.y[PlacedPin]+2*Verdirection].Occupied[l][0] == False:
							#DO PLACE STUFF THEN DRAW TRACE TO CONNECTION
							breadboard[component.y[PlacedPin]].Occupied[component.x[PlacedPin]-breadboard[side][0].xpos] = [False]
							component.x[PlacedPin] = breadboard[side][0].xpos + l
							component.x[pinToPlace] = breadboard[side][0].xpos + l
							component.y[pinToPlace] = component.y[PlacedPin]+2*Verdirection
							breadboard[rail][component.y[PlacedPin]+1*Verdirection].Occupied[l] = [True]
							breadboard[rail][component.y[PlacedPin]].Occupied[l] = [component,PlacedPin]
							breadboard[rail][component.y[PlacedPin]+2*Verdirection].Occupied[l] = [component,pinToPlace]
							startPoint = [side,component.y[pinToPlace]]
							endPoint = [side,matchLocation[1][0]]
							print startPoint, endPoint, "THESE ARE START AND END POINTS OF THE TRACE"
							Trace = drawTrace(startPoint,endPoint,breadboard,component,pinToPlace,compList)

							return None


					
						else:
							pass
							#THE SPACES ARE FULL

				else:
					print "WE HAVE A COMPONENT CLASH..."
					openSpot = findOpenSpace(component.y[PlacedPin],breadboard,side)
					#THERE IS A COMPONENT IN THE IDEAL LOCATION RESOLVE BY: FINDING OPEN SPACE, TRACE FROM PLACED PIN TO ITS ORIGINAL LOCATION, TRACE FROM TOPLACE PIN TO CONNECTION
					print openSpot
					origX = component.x[PlacedPin]
					origY = component.y[PlacedPin]
					breadboard[side][origY].Occupied[origX-breadboard[side][0].xpos] = [False]
					component.y[PlacedPin] = openSpot[1]
					component.x[PlacedPin] = openSpot[2]+breadboard[side][0].xpos
					component.x[pinToPlace] = openSpot[2]+breadboard[side][0].xpos
					component.y[pinToPlace] = openSpot[1]+2
					breadboard[side][component.y[PlacedPin]].Occupied[openSpot[2]] = [component,PlacedPin]
					breadboard[side][component.y[PlacedPin]+1*Verdirection].Occupied[openSpot[2]] = [True]
					breadboard[side][component.y[pinToPlace]].Occupied[openSpot[2]] = [component,pinToPlace]


		else:
			pass
			#COMPONENT IS ON OTHER SIDE OF BREADBOARD
			Hordirection
			placeSide = side +Hordirection
			if placeSide == 2:
				print matchLocation, "MATCH IS ON THE LEFT IN THIS LOCATION"
				print Verdirection, VerDistance, "Component is vertical this direction away"
				FindCrossSpaceOpenAndPlace(component,breadboard,component.y[PlacedPin],Verdirection,PlacedPin,side,compList,matchLocation[1][0])
				
			elif placeSide == 3:
				print matchLocation, "MATCH IS ON THE RIGHT IN THIS LOCATION"
				print Verdirection, VerDistance, "Component is vertical this direction away"
				FindCrossSpaceOpenAndPlace(component,breadboard,component.y[PlacedPin],Verdirection,PlacedPin,side,compList,matchLocation[1][0])

			else:
				pass



def FindCrossSpaceOpenAndPlace(component,breadboard,startY,direction,placedPin,OrigSide,compList,finalY):
	print "RUNNING FIND CROSS OPEN AND PALCE"
	if direction == 0 or direction == 1 or direction == -1: #EVENTUALLY WILL ADD SUPPORT FOR GOING BACKWARD
		for row in range (startY,30):
			leftFlag = 0
			rightFlag = 0
			leftOccupied = 0
			rightOccupied = 0
			LeftSpaceFlag = 0 
			RightSpaceFlag = 0 
			if placedPin == 2:
				pinToPlace = 1
			else:
				pinToPlace = 2
			for k in range(5):
				if breadboard[2][row].Occupied[k][0] == component:
					leftFlag = 1
				elif breadboard[3][row].Occupied[k][0] == component:
					rightFlag = 1
				else:
					pass

				if len(breadboard[2][row].Occupied[k]) == 2: 
					leftOccupied = 1

				elif len(breadboard[3][row].Occupied[k]) == 2:
					rightOccupied = 1
				else:
					pass

				if (leftFlag == 1 or leftOccupied == 0) and (rightFlag == 1 or rightOccupied == 0):
					

					if breadboard[2][row].Occupied[4][0] != False:
						LeftSpaceFlag = 1

					if breadboard[3][row].Occupied[0][0] != False:
						RightSpaceFlag = 1

					if breadboard[2][row].Occupied[4] == [False] and breadboard[3][row].Occupied[0] == [False]:
						print "WE ARE ABLE TO PLACE IN ROW", row
						#PLACE STUFF HERE
						origX = component.x[placedPin]
						origY = component.y[placedPin]
						if OrigSide == 2:
							component.x[placedPin] = 9
							component.y[placedPin] = row
							component.y[pinToPlace] = row
							component.x[pinToPlace] = 7
							breadboard[2][row].Occupied[4] = [component,placedPin]
							breadboard[3][row].Occupied[0] = [component,pinToPlace]

							#STILL NEED TO DO TRACE STUFF
							drawTrace([OrigSide,origY],[OrigSide,row],breadboard,component,placedPin,compList)
							drawTrace((3,row),(3,finalY),breadboard,component,placedPin,compList)
							return None
						else:
							component.x[placedPin] = 7
							component.y[placedPin] = row
							component.y[pinToPlace] = row
							component.x[pinToPlace] = 9
							breadboard[3][row].Occupied[0] = [component,placedPin]
							breadboard[2][row].Occupied[4] = [component,pinToPlace]
							drawTrace([OrigSide,origY],[OrigSide,row],breadboard,component,placedPin,compList)
							drawTrace((2,row),[2,finalY],breadboard,component,placedPin,compList)
							#STILL NEED TO DO TRACE STUFF
							return None



						pass

					else:
						status = moveComponent(breadboard,row,LeftSpaceFlag,RightSpaceFlag)

						if status == False:
							pass
						else:
							#place it draw traces
							if OrigSide == 2:
								component.x[placedPin] = 9
								component.y[placedPin] = row
								component.y[pinToPlace] = row
								component.x[pinToPlace] = 7
								breadboard[2][row].Occupied[4] = [component,placedPin]
								breadboard[3][row].Occupied[0] = [component,pinToPlace]

								#STILL NEED TO DO TRACE STUFF
								drawTrace([OrigSide,origY],[OrigSide,row],breadboard,component,placedPin,compList)
								drawTrace((3,row),(3,finalY),breadboard,component,placedPin,compList)
								#STILL NEED TO DO TRACE STUFF
								return None
							else:
								component.x[placedPin] = 7
								component.y[placedPin] = row
								component.y[pinToPlace] = row
								component.x[pinToPlace] = 9
								breadboard[3][row].Occupied[0] = [component,placedPin]
								breadboard[2][row].Occupied[4] = [component,pinToPlace]
								drawTrace([OrigSide,origY],[OrigSide,row],breadboard,component,placedPin,compList)
								drawTrace((2,row),[2,finalY],breadboard,component,placedPin,compList)
								return None

	else:


					

def moveComponent(breadboard,row,leftFlag,rightFlag):
	if leftFlag == 1 and rightFlag == 1:
		return False
	elif leftFlag == 1:
		component = breadboard[2][row].Occupied[4][0]
		if component == True:
			return False
		
		row1 = component.y[1]
		row2 = component.y[2]
		direction = (row2 - row1)/abs(row2-row1)
		for k in range(5):
			if breadboard[2][row1].Occupied[k][0] == False and breadboard[2][row2].Occupied[k][0] == False:
				breadboard[2][row1].Occupied[4] == [False]
				breadboard[2][row2].Occupied[4] == [False]
				breadboard[2][row1+direction].Occupied[4] == [False]
				breadboard[2][row1].Occupied[k] == [component,1]
				breadboard[2][row2].Occupied[k] == [component,2]
				breadboard[2][row1+direction].Occupied[k] == [True]
				component.x[1] = 3 + k
				component.x[2] = 3 + k
				return None
	elif rightFlag ==1:
		component = breadboard[3][row].Occupied[0][0]
		if component == True:
			return False
		
		row1 = component.y[1]
		row2 = component.y[2]
		direction = (row2 - row1)/abs(row2-row1)
		for k in range(5):
			if breadboard[3][row1].Occupied[k][0] == False and breadboard[3][row2].Occupied[k][0] == False:
				breadboard[3][row1].Occupied[0] == [False]
				breadboard[3][row2].Occupied[0] == [False]
				breadboard[3][row1+direction].Occupied[0] == [False]
				breadboard[3][row1].Occupied[k] == [component,1]
				breadboard[3][row2].Occupied[k] == [component,2]
				breadboard[3][row1+direction].Occupied[k] == [True]
				component.x[1] = 9 + k
				component.x[2] = 9 + k
				return None


def PlaceFirstPin(component,breadboard,location,pin):

	""" WILL RETURN FALSE IF ROW IS FULL """
	print "RUNNING PLACEFIRSTPIN"
	for index in range(len(location[0])):
		rail = location[0][index]
		row = location[1][index]

		if location[0][index] == 2:
			for k in range(4,-1,-1):
				if breadboard[rail][row].Occupied[k][0] == False:
					breadboard[rail][row].Occupied[k] = [component,pin]
					component.x[pin] = breadboard[rail][row].xpos + k
					component.y[pin] = row
					return None



		elif location[0][index] == 3:
			for k in range(5):
				if breadboard[rail][row].Occupied[k][0] == False:
					breadboard[rail][row].Occupied[k] = [component,pin]
					component.x[pin] = breadboard[rail][row].xpos + k
					component.y[pin] = row
					return None
		else:
			pass
	return False

		




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

	compList = []
	Resistor1 = resistor(1,0,0,4,5,'h',{1:[],2:[]})
	Resistor2 = resistor(2,0,0,4,7,'h',{1:[],2:[]})
	Resistor3 = resistor(3,0,0,4,5,'h',{1:[],2:[]})
	Resistor4 = resistor(4,0,0,4,5,'h',{1:[],2:[]})
	Resistor5 = resistor(5,0,0,4,5,'h',{1:[],2:[]})
	Resistor6 = resistor(6,0,0,4,5,'h',{1:[],2:[]})
	DIP = dip(0,0,4,5,'h',{},'dip',number_of_pins = 8, pin_gap = 2)
	board[2][3].Occupied[3] = [True]

	placeFirstComponent(DIP,board,compList)

	#board[3][3].Occupied[1]=[True,True]
	Resistor1.connections[1].append(DIP)
	Resistor1.connections[2].append(DIP)
	#Resistor1.connections[2].append(DIP)
	#DIP.connections[].append(Resistor1)
	DIP.connections[8].append(Resistor1)
	DIP.connections[7].append(Resistor1)
	PlaceComponent(Resistor1,board,compList)

	

	print DIP.x
	print DIP.y
	print Resistor1.x
	print Resistor1.y
	print Resistor2.x
	print Resistor2.y
	print Resistor3.x
	print Resistor3.y


	print board[3][1].Occupied
	print board[3][2].Occupied
	print board[3][3].Occupied
	print board[3][4].Occupied
	print board[3][5].Occupied
	print board[3][6].Occupied
	print board[3][7].Occupied
	print board[3][8].Occupied
	print compList
	#print compList[1].x
	#print compList[1].y
	
	