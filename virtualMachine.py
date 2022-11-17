from collections import deque
import sys

class virtualMachine():
    def __init__(self, programID, quadruplesList, variablesTable, constantsTable, numTemps) -> None:
        self.programID = programID
        self.quadruplesList = quadruplesList
        self.variablesTable = variablesTable
        self.constansTable = constantsTable
        self.numTemps = numTemps

    def __str__(self) -> str:
        return f'Progran Name: {self.programID}\nNum of quadruples: {len(self.quadruplesList)}'

    def loadMemory(self, gMemory, lMemory, cMemory, tMemory):
        self.gMemory = gMemory
        self.lMemory = lMemory
        self.cMemory = cMemory
        self.tMemory = tMemory

        self.temp_ints = []
        self.temp_ints_s = []

        self.local_ints = []
        self.local_ints_s = []

        self.const_ints = []

        # Initializing Constant Memory
        for el in self.constansTable:
            for x in self.constansTable[el]:
                if el == 'int':
                    self.const_ints.append(x)

        # Initializing Temp Memory
        # Int Temp Memory DIM-1
        for i in range(0, self.numTemps[0]):
            self.temp_ints.append(None)

    def getValue(self, pos):
        # Local Int Variables
        if(5000 <= pos < 6000):
            if(self.local_ints_s[-1][pos - 5000] == None):
                print("No value")
                sys.exit()
            return self.local_ints_s[-1][pos - 5000]
        # Constant Int
        elif(9000 <= pos < 10000):
            if(self.const_ints[pos - 9000] == None):
                print("No value")
                sys.exit()
            return self.const_ints[pos - 9000]
        # Temp Int
        elif(13000 <= pos < 14000):
            if(self.temp_ints_s[-1][pos - 13000] == None):
                print("No value")
                sys.exit()
            return self.temp_ints_s[-1][pos - 13000]

    def exec(self):
        quadCont = 0
        print(self.const_ints)
        while(quadCont < len(self.quadruplesList)):
            oper = self.quadruplesList[quadCont].operator
            operand1 = self.quadruplesList[quadCont].operand1
            operand2 = self.quadruplesList[quadCont].operand2
            temp = self.quadruplesList[quadCont].temp

            if(oper == 'GOTO'):
                quadCont = temp
                continue
            elif(oper == '+'):
                if 5000 <= temp < 6000:
                   print('SUMA')
            elif(oper == '='):
                if 5000 <= temp < 6000:
                    print(self.getValue(temp))
            quadCont += 1
