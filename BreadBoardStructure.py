from ComponentModule import *
from BreadboardModule import *

if __name__ == '__main__':

    leftRail1 =  rails(0)
    leftRail2 = rails(1)
    rightRail1 = rails(17)
    rightRail2 = rails(18)

    leftBuildZone = []

    for i in range(leftRail1.length):
        leftBuildZone.append(rows((i),4,'left', 'leftrow' + str(i)))

    rightBuildZone = []

    for i in range(leftRail1.length):
        rightBuildZone.append(rows((i),11,'right', 'rightrow' + str(i)))

    breadboard = [leftRail1,leftRail2,leftBuildZone,rightBuildZone,rightRail1,rightRail2]

    Resistor1 = resistor(45000,4,5,{1:'Vref',2:'GND'})
# DO SOME TESTING 


    leftBuildZone[0].Occupied[1] = True
    print leftBuildZone[0].Occupied
    
    leftBuildZone[0].value = 'Vref'
    
    print leftBuildZone[0]
    print Resistor1.PinValues
