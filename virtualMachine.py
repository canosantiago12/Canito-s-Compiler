import sys

class virtualMachine():
    def __init__(self, programID, quadruplesList, variablesTable, constantsTable, numTemps) -> None:
        self.programID = programID
        self.quadruplesList = quadruplesList
        self.variablesTable = variablesTable
        self.constansTable = constantsTable
        self.numTemps = numTemps
        self.currFunc = 'mainStage'
        self.quadCont = 0

    def __str__(self) -> str:
        return f'Progran Name: {self.programID}\nNum of quadruples: {len(self.quadruplesList)}'

    def loadMemory(self, gMemory, lMemory, cMemory, tMemory):
        self.gMemory = gMemory
        self.lMemory = lMemory
        self.cMemory = cMemory
        self.tMemory = tMemory

        # Initializing Global Memory
        for var in self.variablesTable[self.programID]['vars']:
            if(self.variablesTable[self.programID]['vars'][var]['type'] == 'int'):
                self.gMemory.global_ints.append(None)
            elif(self.variablesTable[self.programID]['vars'][var]['type'] == 'float'):
                self.gMemory.global_floats.append(None)
            elif(self.variablesTable[self.programID]['vars'][var]['type'] == 'bool'):
                self.gMemory.global_bools.append(None)
            elif(self.variablesTable[self.programID]['vars'][var]['type'] == 'string'):
                self.gMemory.global_strings.append(None)

        # Initializing Constant Memory
        for el in self.constansTable:
            for x in self.constansTable[el]:
                if el == 'int':
                    self.cMemory.const_ints.append(x)
                elif el == 'float':
                    self.cMemory.const_floats.append(x)
                elif el == 'bool':
                    self.cMemory.const_bools.append(x)
                elif el == 'string':
                    self.cMemory.const_strings.append(x)

        # Initializing Temp Memory
        # Int Temp Memory (First Value)
        for i in range(0, self.numTemps[0]):
            self.tMemory.temp_ints.append(None)
        # Float Temp Memory (Second Value) 
        for i in range(0, self.numTemps[1]):
            self.tMemory.temp_floats.append(None)
        # Bool Temp Memory (Third Value)
        for i in range(0, self.numTemps[2]):
            self.tMemory.temp_bools.append(None)
        # Strings Temp Memory (Fourth Value)
        for i in range(0, self.numTemps[3]):
            self.tMemory.temp_strings.append(None)
        self.tMemory.reset()

    def getVarID(self, pos, isGlobal):
        if isGlobal:
            varNames = self.variablesTable[self.programID]['vars']
            for key, value in varNames.items():
                if pos == value['memoryPos']:
                    return key
        else:
            varNames = self.variablesTable[self.currFunc]['vars']
            for key, value in varNames.items():
                if pos == value['memoryPos']:
                    return key

    def getVarType(self, pos, isGlobal):
        if isGlobal:
            varNames = self.variablesTable[self.programID]['vars']
            for key, value in varNames.items():
                if pos == value['memoryPos']:
                    return value['type']
        else:
            varNames = self.variablesTable[self.currFunc]['vars']
            for key, value in varNames.items():
                if pos == value['memoryPos']:
                    return value['type']

    def getValue(self, pos):
        if(1000 <= pos < 2000):
            if(self.gMemory.global_ints[pos - 1000] == None):
                print(f"Variable [ {self.getVarID(pos, True)} ] has no value !!!")
                sys.exit()
            return self.gMemory.global_ints[pos - 1000]
        # Local Int
        if(5000 <= pos < 6000):
            if(self.lMemory.local_ints_s[-1][pos - 5000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.lMemory.local_ints_s[-1][pos - 5000]
        # Local Float
        elif(6000 <= pos < 7000):
            if(self.lMemory.local_floats_s[-1][pos - 6000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.lMemory.local_floats_s[-1][pos - 6000]
        # Local Bool
        elif(7000 <= pos < 8000):
            if(self.lMemory.local_bools_s[-1][pos - 7000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.lMemory.local_bools_s[-1][pos - 7000]
        # Local Strings
        elif(8000 <= pos < 9000):
            if(self.lMemory.local_strings_s[-1][pos - 8000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.lMemory.local_strings_s[-1][pos - 8000]
        # Constant Int
        elif(9000 <= pos < 10000):
            if(self.cMemory.const_ints[pos - 9000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.cMemory.const_ints[pos - 9000]
        # Constant Float
        elif(10000 <= pos < 11000):
            if(self.cMemory.const_floats[pos - 10000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.cMemory.const_floats[pos - 10000]
        # Constant Bool
        elif(11000 <= pos < 12000):
            if(self.cMemory.const_bools[pos - 11000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.cMemory.const_bools[pos - 11000]
        # Constant String
        elif(12000 <= pos < 13000):
            if(self.cMemory.const_strings[pos - 12000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.cMemory.const_strings[pos - 12000]
        # Temp Int
        elif(13000 <= pos < 14000):
            if(self.tMemory.temp_ints_s[-1][pos - 13000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.tMemory.temp_ints_s[-1][pos - 13000]
        # Temp Float
        elif(14000 <= pos < 15000):
            if(self.tMemory.temp_floats_s[-1][pos - 14000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.tMemory.temp_floats_s[-1][pos - 14000]
        # Temp Bool
        elif(15000 <= pos < 16000):
            if(self.tMemory.temp_bools_s[-1][pos - 15000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.tMemory.temp_bools_s[-1][pos - 15000]
        # Temp String
        elif(16000 <= pos < 17000):
            if(self.tMemory.temp_strings_s[-1][pos - 16000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.tMemory.temp_strings_s[-1][pos - 16000]

    def exec(self):
        # Loading Local Memory For Main Function
        for i in range(0, self.variablesTable[self.currFunc]['numVars'][0]):
            self.lMemory.local_ints.append(None)
        for i in range(0, self.variablesTable[self.currFunc]['numVars'][1]):
            self.lMemory.local_floats.append(None)
        for i in range(0, self.variablesTable[self.currFunc]['numVars'][2]):
            self.lMemory.local_bools.append(None)
        for i in range(0, self.variablesTable[self.currFunc]['numVars'][3]):
            self.lMemory.local_strings.append(None)
        self.lMemory.reset()

        while(self.quadCont < len(self.quadruplesList)):
            oper = self.quadruplesList[self.quadCont].operator
            operand1 = self.quadruplesList[self.quadCont].operand1
            operand2 = self.quadruplesList[self.quadCont].operand2
            temp = self.quadruplesList[self.quadCont].temp

            if(oper == 'GOTO'):
                self.quadCont = temp
                continue
            elif(oper == 'GOTOF'):
                if(self.getValue(operand1) == False):
                    self.quadCont = temp
                    continue
            elif(oper == '+'):
                # if(1000 <= temp < 2000):
                #     self.gMemory.global_ints[temp - 1000] = self.getValue(operand1) + self.getValue(operand2)
                # elif(2000 <= temp < 3000):
                #     self.gMemory.global_floats[temp - 2000] = self.getValue(operand1) + self.getValue(operand2)
                # elif(5000 <= temp < 6000):
                #     self.lMemory.local_ints_s[-1][temp - 5000] = self.getValue(operand1) + self.getValue(operand2)
                # elif(6000 <= temp < 7000):
                #     self.lMemory.local_floats_s[-1][temp - 6000] = self.getValue(operand1) + self.getValue(operand2)
                # el
                if(13000 <= temp < 14000):
                    self.tMemory.temp_ints_s[-1][temp - 13000] = self.getValue(operand1) + self.getValue(operand2)
                elif(14000 <= temp < 15000):
                    self.tMemory.temp_floats_s[-1][temp - 14000] = self.getValue(operand1) + self.getValue(operand2)
            elif(oper == '-'):
                if(13000 <= temp < 14000):
                    self.tMemory.temp_ints_s[-1][temp - 13000] = self.getValue(operand1) - self.getValue(operand2)
                elif(14000 <= temp < 15000):
                    self.tMemory.temp_floats_s[-1][temp - 14000] = self.getValue(operand1) - self.getValue(operand2)
            elif(oper == '*'):
                if(13000 <= temp < 14000):
                    self.tMemory.temp_ints_s[-1][temp - 13000] = self.getValue(operand1) * self.getValue(operand2)
                elif(14000 <= temp < 15000):
                    self.tMemory.temp_floats_s[-1][temp - 14000] = self.getValue(operand1) * self.getValue(operand2)
            elif(oper == '/'):
                if(self.getValue(operand2) == 0):
                    print(f"You can't divide by 0 !!!")
                    sys.exit()
                if(13000 <= temp < 14000):
                    self.tMemory.temp_ints_s[-1][temp - 13000] = self.getValue(operand1) / self.getValue(operand2)
                elif(14000 <= temp < 15000):
                    self.tMemory.temp_floats_s[-1][temp - 14000] = self.getValue(operand1) / self.getValue(operand2)
            elif(oper == '%'):
                if(self.getValue(operand2) == 0):
                    print(f"You can't divide by 0 !!!")
                    sys.exit()
                if(13000 <= temp < 14000):
                    self.tMemory.temp_ints_s[-1][temp - 13000] = self.getValue(operand1) % self.getValue(operand2)
                elif(14000 <= temp < 15000):
                    self.tMemory.temp_floats_s[-1][temp - 14000] = self.getValue(operand1) % self.getValue(operand2)
            elif(oper == '^'):
                if(13000 <= temp < 14000):
                    self.tMemory.temp_ints_s[-1][temp - 13000] = self.getValue(operand1) ** self.getValue(operand2)
                elif(14000 <= temp < 15000):
                    self.tMemory.temp_floats_s[-1][temp - 14000] = self.getValue(operand1) ** self.getValue(operand2)
            elif(oper == '<'):
                # if(13000 <= temp < 14000):
                #     self.tMemory.temp_ints_s[-1][temp - 13000] = self.getValue(operand1) < self.getValue(operand2)
                # elif(14000 <= temp < 15000):
                #     self.tMemory.temp_floats_s[-1][temp - 14000] = self.getValue(operand1) < self.getValue(operand2)
                if(15000 <= temp < 16000):
                    self.tMemory.temp_bools_s[-1][temp - 15000] = self.getValue(operand1) < self.getValue(operand2)
            elif(oper == '<='):
                if(15000 <= temp < 16000):
                    self.tMemory.temp_bools_s[-1][temp - 15000] = self.getValue(operand1) <= self.getValue(operand2)
            elif(oper == '>'):
                if(15000 <= temp < 16000):
                    self.tMemory.temp_bools_s[-1][temp - 15000] = self.getValue(operand1) > self.getValue(operand2)
            elif(oper == '>='):
                if(15000 <= temp < 16000):
                    self.tMemory.temp_bools_s[-1][temp - 15000] = self.getValue(operand1) >= self.getValue(operand2)
            elif(oper == '=='):
                if(operand1 == operand2):
                    self.tMemory.temp_bools_s[-1][temp - 15000] = True
                else:
                    if(15000 <= temp < 16000):
                        self.tMemory.temp_bools_s[-1][temp - 15000] = self.getValue(operand1) == self.getValue(operand2)
            elif(oper == '!='):
                if(operand1 == operand2):
                    self.tMemory.temp_bools_s[-1][temp - 15000] = False
                else:
                    if(15000 <= temp < 16000):
                        self.tMemory.temp_bools_s[-1][temp - 15000] = self.getValue(operand1) != self.getValue(operand2)
            elif(oper == '&&'):
                aux1 = False
                aux2 = False

                if(self.getValue(operand1) == 'true' or self.getValue(operand1) == True):
                    aux1 = True
                if(self.getValue(operand2) == 'true' or self.getValue(operand2) == True):
                    aux2 = True

                if(15000 <= temp < 16000):
                    self.tMemory.temp_bools_s[-1][temp - 15000] = aux1 and aux2
            elif(oper == '||'):
                aux1 = False
                aux2 = False

                if(self.getValue(operand1) == 'true' or self.getValue(operand1) == True):
                    aux1 = True
                if(self.getValue(operand2) == 'true' or self.getValue(operand2) == True):
                    aux2 = True

                if(15000 <= temp < 16000):
                    self.tMemory.temp_bools_s[-1][temp - 15000] = aux1 or aux2
            elif(oper == '='):
                if(1000 <= temp < 2000):
                    self.gMemory.global_ints[temp - 1000] = self.getValue(operand1)
                elif(2000 <= temp < 3000):
                    self.gMemory.global_float[temp - 2000] = self.getValue(operand1)
                elif(3000 <= temp < 4000):
                    self.gMemory.global_bools[temp - 3000] = self.getValue(operand1)
                elif(4000 <= temp < 5000):
                    self.gMemory.global_strings[temp - 4000] = self.getValue(operand1)
                elif(5000 <= temp < 6000):
                    self.lMemory.local_ints_s[-1][temp - 5000] = self.getValue(operand1)
                elif(6000 <= temp < 7000):
                    self.lMemory.local_floats_s[-1][temp - 6000] = self.getValue(operand1)
                elif(7000 <= temp < 8000):
                    self.lMemory.local_bools_s[-1][temp - 7000] = self.getValue(operand1)
                elif(8000 <= temp < 9000):
                    self.lMemory.local_strings_s[-1][temp - 8000] = self.getValue(operand1)
            elif(oper == 'print'):
                print(self.getValue(temp))
            elif(oper == 'listen'):
                aux = ''

                if((1000 <= temp < 2000) or (2000 <= temp < 3000) or (3000 <= temp < 4000) or (4000 <= temp < 5000)):
                    aux = input(f">> ({self.getVarType(temp, 1)}) ")
                elif((5000 <= temp < 6000) or (6000 <= temp < 7000) or (7000 <= temp < 8000) or (8000 <= temp < 9000)):
                    aux = input(f">> ({self.getVarType(temp, 0)}) ")

                if((1000 <= temp < 2000) or (5000 <= temp < 6000)):
                    try:
                        val = int(aux)
                        if(1000 <= temp < 2000):
                            self.gMemory.global_ints[temp - 1000] = val
                        elif(5000 <= temp < 6000):
                            self.lMemory.local_ints_s[-1][temp - 5000] = val
                    except ValueError:
                        if(1000 <= temp < 2000):
                            print(f"Input is not [ {self.getVarType(temp, 1)} ] and variable [ {self.getVarID(temp, 1)} ] must be [ {self.getVarType(temp, 1)} ] !!!")
                        elif(5000 <= temp < 6000):
                            print(f"Input is not [ {self.getVarType(temp, 0)} ] and variable [ {self.getVarID(temp, 0)} ] must be [ {self.getVarType(temp, 0)} ] !!!")
                        sys.exit()
                elif((2000 <= temp < 3000) or (6000 <= temp < 7000)):
                    try:
                        val = float(aux)
                        if(2000 <= temp < 3000):
                            self.gMemory.global_floats[temp - 2000] = val
                        elif(6000 <= temp < 7000):
                            self.lMemory.local_floats_s[-1][temp - 6000] = val
                    except ValueError:
                        if(2000 <= temp < 3000):
                            print(f"Input is not [ {self.getVarType(temp, 1)} ] and variable [ {self.getVarID(temp, 1)} ] must be [ {self.getVarType(temp, 1)} ] !!!")
                        elif(6000 <= temp < 7000):
                            print(f"Input is not [ {self.getVarType(temp, 0)} ] and variable [ {self.getVarID(temp, 0)} ] must be [ {self.getVarType(temp, 0)} ] !!!")
                        sys.exit()
                elif((3000 <= temp < 4000) or (7000 <= temp < 8000)):
                    if(aux == 'true' or aux == 'false'):
                        if(3000 <= temp < 4000):
                            self.gMemory.global_bools[temp - 3000] = aux
                        elif(7000 <= temp < 8000):
                            self.lMemory.local_bools_s[-1][temp - 7000] = aux
                    else:
                        if(3000 <= temp < 4000):
                            print(f"Input is not [ {self.getVarType(temp, 1)} ] and variable [ {self.getVarID(temp, 1)} ] must be [ {self.getVarType(temp, 1)} ] !!!")
                        elif(7000 <= temp < 8000):
                            print(f"Input is not [ {self.getVarType(temp, 0)} ] and variable [ {self.getVarID(temp, 0)} ] must be [ {self.getVarType(temp, 0)} ] !!!")
                        sys.exit()
                elif(4000 <= temp < 5000):
                    self.gMemory.global_strings[temp - 4000] = aux
                elif(8000 <= temp < 9000):
                    self.lMemory.local_strings_s[-1][temp - 8000] = aux
            self.quadCont += 1
