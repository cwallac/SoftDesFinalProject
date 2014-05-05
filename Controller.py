from BreadBoardStructure import *
from ComponentModule import *
from BreadboardModule import *
from random import randint


from place import *

class Model():
    def __init__(self):
        print "MODEL INITIALIZED"
        self.board = createBreadboard()
        self.compList = []

    def placeCompOnBreadBoard(self,component,board,compList):
        if len(compList) == 0:
            placeFirstComponent(component,board,compList)
        else:
            placeComponent(component,board,compList)

    def placeCompOnSchema(self,component,compList):
        placingCD(component,compList)

class Controller():

    def __init__(self,model):
        print "Controller INITIALIZED"
        self.rawList = []
        self.objectList = []
        self.model = model

    def componentAdded(self,rawData):
         self.rawList.append(rawData)
         if rawData[3] == 'bb':
             self.rawToBread(rawData)
             self.checkBBConnections(self.objectList)
             self.model.placeCompOnSchema(self.objectList[-1],self.model.compList)
             return self.SCtoGUI(self.model.compList)

         else:
             self.rawToSchema(rawData)
             self.checkConnections(self.objectList)
             self.model.placeCompOnBreadBoard(self.objectList[-1],self.model.board,self.model.compList)
             return self.BBtoGUI(self.model.compList)

            
    

             

    def BBtoGUI(self,componentList):
        exportList = []
        exportData = []
        for comp in componentList:
            exportData = []
            print comp.x, "X COMPS"
            print comp.y, "Y COMPS"
            
            exportData.append((self.convertBBtoRawCoordinate(comp.x[1]),comp.y[1]+1))
            exportData.append((self.convertBBtoRawCoordinate(comp.x[len(comp.x)]),comp.y[len(comp.y)]+1))
            if isinstance(comp,resistor):
                exportData.append('r')
            elif isinstance(comp,capacitor):
                exportData.append('c')
            elif isinstance(comp,dip):
                exportData.append('d')
            elif isinstance(comp,trace):
                exportData.append('t')
            exportData.append('bb')
            exportList.append(exportData)
        return exportList

    def SCtoGUI(self,componentList):
        exportList = []
        exportData = []
        for comp in componentList:
            exportData = []
            exportData.append((comp.cx[1]+1,comp.cy[1]+1))
            exportData.append((comp.cx[2]+1,comp.cy[2]+1))
            if isinstance(comp,resistor):
                exportData.append('r')
            elif isinstance(comp,capacitor):
                exportData.append('c')
            elif isinstance(comp,dip):
                exportData.append('d')
            elif isinstance(comp,trace):
                exportData.append('t')
            exportData.append('sc')
            exportList.append(exportData)
        return exportList


    def rawToSchema(self,rawData):
        print "RAW DATA IS", rawData
        if rawData[2] == 'r':
            Res = resistor(randint(1,1000),0,0,0,0,'h',{})
            Res.cx[1] = rawData[0][0]
            Res.cx[2] = rawData[1][0]
            Res.cy[1] = rawData[0][1]
            Res.cy[2] = rawData[1][1]
            print "ADDED CX"
            self.objectList.append(Res)
        elif rawData[2] == 'w':
            Trace = trace(randint(1,1000),0,0,0,0,0)
            Trace.cx[1] = rawData[0][0]
            Trace.cx[2] = rawData[1][0]
            Trace.cy[1] = rawData[0][1]
            Trace.cy[2] = rawData[1][1]
            self.objectList.append(Trace)
        elif rawData[2] == 'd':
            numberOfPins = (rawData[1][1]-rawData[0][1])*2+2

            direction = (rawData[1][0]-rawData[0][0])/abs(rawData[1][0]-rawData[0][0])
            component = dip(0,0,0,0,'h',{},'dip',numberOfPins, pin_gap = 2)
            for i in range(numberOfPins):
                if direction > 0:

                    if (i +1)%2 == 0:
                        component.cx[i+1]=rawData[1][0]
                        component.cy[i+1] = rawData[0][1]+i/2
                    else:
                        component.cx[i+1]=rawData[0][0]
                        component.cy[i+1] = rawData[0][1]+i/2

                else:
                    if (i +1)%2 == 0:
                        component.cx[i+1]=rawData[0][0]
                        component.cy[i+1] = rawData[0][1]+i/2
                    else:
                        component.cx[i+1]=rawData[1][0]
                        component.cy[i+1] = rawData[0][1]+i/2
            print component.cx, "DIPS XPOS"
            self.objectList.append(component)




        else:
            Res = capacitor(randint(1,1000),0,0,0,0,'h',{})
            Res.cx[1] = rawData[0][0]
            Res.cx[2] = rawData[1][0]
            Res.cy[1] = rawData[0][1]
            Res.cy[2] = rawData[1][1]
            self.objectList.append(Res)

    def rawToBread(self,rawData):
        xori = self.convertToBreadCoordinate(rawData[0][0])
        xend = self.convertToBreadCoordinate(rawData[1][0])
        yori = rawData[0][1] + 1
        yend = rawData[1][1] + 1
        if rawData[2] == 'r':
            Res = resistor(randint(1,1000),0,0,0,0,'h',{})
            Res.x[1] = xori
            Res.x[2] = xend
            Res.y[1] = yori
            Res.y[2] = yend
            print "ADDED CX"
            self.objectList.append(Res)
        elif rawData[2] == 'w':
            Trace = trace(randint(1,1000),0,0,0,0,0)
            Trace.x[1] = xori
            Trace.x[2] = xend
            Trace.y[1] = yori
            Trace.y[2] = yend
            self.objectList.append(Trace)
        elif rawData[2] == 'd':
            pass
        else:
            Res = capacitor(randint(1,1000),0,0,0,0,'h',{})
            Res.cx[1] = xori
            Res.cx[2] = xend
            Res.cy[1] = yori
            Res.cy[2] = yend
            self.objectList.append(Res)

    def convertBBtoRawCoordinate(self,point):

        if point <=1:
            return point + 1
        
        else:
            return point



    def convertToBreadCoordinate(self,point):
        if point <= 2:
            return point-1
        
        else:
            return point

    def checkConnections(self,objects):

        for comp in objects:
            for index in comp.connections:
                comp.connections[index] = []
        #STILL NEED TO HANDLE DIPS

        for component in objects:

            print component.connections, "THIS IS THE CONNECTIONS"
            for testComp in objects:
                if component == testComp:
                    pass
                else:

                    for pins in component.cx:
                        print pins
                        for TestPins in testComp.cx:

                            if component.cx[pins] == testComp.cx[TestPins] and component.cy[pins] == testComp.cy[TestPins]:
                                print "APPENDING TO CONNECTIONS", pins, TestPins, component
                                component.connections[pins].append(testComp)
            print component.connections, "THIS IS THE COMPONENTS CONNECTIONS"

    def checkBBConnections(self,objects):
                for comp1 in objects:
                        for comp2 in objects:
                                if comp2 == comp1:
                                        pass
                                else:
                                        for pins1 in comp1.cx:
                                                for pins2 in comp2.cx:
                                                        if comp1.cx[pins1] == 0 or comp1.cx[pins1] == 1:
                                                                        if comp2.cx[pins2] !=0 or comp2.cx[pins2]!=1:
                                                                                pass
                                                                        else:
                                                                                comp1.connections[pins1].append(comp2)
                                                        elif comp1.cx[pins1] == 16 or comp1.cx[pins1] == 17:
                                                                if comp2.cx[pins2] != 16 or comp2.cx[pins2] != 17:
                                                                        pass
                                                                else:
                                                                        comp1.connections[pins1].append(comp2)
                                                        elif comp1.cy[pins1] == comp2.cy[pins2]:
                                                                if comp1.cx[pins1] <=8 and comp1.cx[pins1] >=4:
                                                                        if comp2.cx[pins2] <=8 and comp2.cx[pins2] >=4:
                                                                                comp1.connections[pins1].append(comp2)
                                                                elif comp1.cx[pins1] <=15 and comp1.cx[pins1] >=10:
                                                                        if comp2.cx[pins2] <=15 and comp2.cx[pins2] >=10:
                                                                                comp1.connections[pins1].append(comp2)










if __name__ == '__main__':

    TestData = [(0,0),(0,1),'r','sc']
    TestData2 = [(0,0),(1,0),'r','sc']
    Test = Model()
    Cont = Controller(Test)
    """
    print Test.board[3][0].Occupied
    Resistor1 = resistor(1,0,0,4,5,'h',{1:[],2:[]})
    Test.placeCompOnBreadBoard(Resistor1,Test.board,Test.compList)
    print Test.compList[0].x
    Test.placeCompOnSchema(Resistor1,Test.compList)
    print Test.compList[0].cx
    """
    Cont.componentAdded(TestData)
    #Test.placeCompOnBreadBoard(Cont.objectList[-1],Test.board,Test.compList)
    Cont.componentAdded(TestData2)
    #Test.placeCompOnBreadBoard(Cont.objectList[-1],Test.board,Test.compList)
    print Cont.objectList, "THIS IS THE CONTROLLERS LIST OF OBJECTS"
    print Test.compList, "THIS IS THE MODELS"
    print Cont.BBtoGUI(Test.compList)
    print Cont.objectList[1].connections
    print Test.compList[0].x