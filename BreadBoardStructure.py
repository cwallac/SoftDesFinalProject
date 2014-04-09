from ComponentModule import *
from BreadboardModule import *

#BREADBOARD[2] = left, [3] = right


if __name__ == '__main__':

	breadboard = createBreadboard()

	Resistor1 = resistor(45000,4,5,{1:'Vref',2:'GND'})
	component = Resistor1
	
	value1 = component.PinValues[1]
	print value1

	breadboard[2][1].value = 'Vreff'

	breadboard[2][1].Occupied[0] = True
	breadboard[2][1].Occupied[1] = True
	breadboard[2][1].Occupied[2] = True
	breadboard[2][1].Occupied[3] = True
	breadboard[2][1].Occupied[4] = True


	placed = False
	valueFound = False
	occupiedRow = 'NONE'
	for space in range(len(breadboard)):
		#ITERATE THROUGH BREADBOARD LISTS/OBJECTS
		if type(breadboard[space]) == list:
			#IN ROW SPACES
			for index in range(len(breadboard[space])):
				#ITERATE THROUGH THE ROW SPACE
				if breadboard[space][index].value == value1:
					#MATCHING VALUE
					valueFound = True
					print 'VALUE FOUND'

					

					print component.y1
					print str(len(breadboard[space][index].Occupied)) + 'lg'
					
					for xValue in range(len(breadboard[space][index].Occupied)):
						#ITERATE THROUGH PINHOLES
						if breadboard[space][index].Occupied[xValue] == False:
							#OPEN PINHOLES
							placed = True
							component.x1 = breadboard[space][index].xpos + xValue
							component.y1 = breadboard[space][index].ypos
							print component.x1
							#ADD CONDITIONALS TO CHECK OTHER Neighboring rows for conflicts
							break
						else:
							occupiedRow = breadboard[space][index]
							#NO OPEN PINHOLES
							#print 'This row has no open pinholes'

							#sOMETHING RELATED TO REOSLVING THSI WITH A TRACE
							pass
				else:
					#NO MATCHING VALUE
					#print 'No value matches within the row spaces'
					pass
					
		else:
			#WE ARE ON A POWER RAIL
			if breadboard[space].value == value1:
				# MATCHING VALUE
				valueFound = True
				component.x1 = breadboard[space].xpos
				print 'VALUE FOUND'
				for yValue in range(len(breadboard[space].Occupied)):
					if breadboard[space].Occupied[yValue] == False:
						#OPEN PINHOLES
						placed = True
						component.y1 = yValue
						print component.y1
						break
					else:
						#NO OPEN PINHOLES
						# print 'This rail has no open pinholes'
						pass
			else:
				#NOT MATCHING VALUE
				pass

	print placed
	print valueFound
	
				
	if valueFound == False:
		#Pin Value Not found
		for unOccupied in range(len(breadboard[2])):
			#ITerate through left side
			if breadboard[2][unOccupied].value == '':
				#THE ROW IS UNOCCUPIED
				placed = True
				component.x1 = breadboard[2][unOccupied].xpos
				component.y1 = breadboard[2][unOccupied].ypos

				breadboard[2][unOccupied].value = component.PinValues[1] 
				breadboard[2][unOccupied].Occupied[0] = True
				print breadboard[2][unOccupied].value

				break
			else:
				# THE ROW IS OCCUPIED
				pass
		if placed == False:
			#PLACEMENT ON LEFT SIDE FAILED
			for unOccupied in range(len(breadboard[3])):
				#ITERATE THROUGH RIGHT SIDE
				if breadboard[3][unOccupied].value == '':
					#THE ROW IS UNOCCUPIED
					placed = True
					component.x1 = breadboard[3][unOccupied].xpos
					component.y1 = breadboard[3][unOccupied].ypos

					breadboard[3][unOccupied].value = component.PinValues[1] 
					breadboard[3][unOccupied].Occupied[0] = True


					break
				else:
					#ROW IS OCCUPIED
					pass


	print component.y1