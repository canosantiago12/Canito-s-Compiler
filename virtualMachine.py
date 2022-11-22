import sys
import re
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from numpy import random
from collections import deque

class virtualMachine():
    def __init__(self, programID, quadruplesList, variablesTable, constantsTable, numTemps) -> None:
        self.programID = programID
        self.quadruplesList = quadruplesList
        self.variablesTable = variablesTable
        self.constansTable = constantsTable
        self.numTemps = numTemps
        self.currFunc = 'mainStage'
        self.last = []

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
                if 'size' in self.variablesTable[self.programID]['vars'][var]:
                    for i in range(0, self.variablesTable[self.programID]['vars'][var]['size']):
                        self.gMemory.global_ints.append(None)
                else:
                    self.gMemory.global_ints.append(None)
            elif(self.variablesTable[self.programID]['vars'][var]['type'] == 'float'):
                if 'size' in self.variablesTable[self.programID]['vars'][var]:
                    for i in range(0, self.variablesTable[self.programID]['vars'][var]['size']):
                        self.gMemory.global_floats.append(None)
                else:
                    self.gMemory.global_floats.append(None)
            elif(self.variablesTable[self.programID]['vars'][var]['type'] == 'bool'):
                if 'size' in self.variablesTable[self.programID]['vars'][var]:
                    for i in range(0, self.variablesTable[self.programID]['vars'][var]['size']):
                        self.gMemory.global_bools.append(None)
                else:
                    self.gMemory.global_bools.append(None)
            elif(self.variablesTable[self.programID]['vars'][var]['type'] == 'string'):
                if 'size' in self.variablesTable[self.programID]['vars'][var]:
                    for i in range(0, self.variablesTable[self.programID]['vars'][var]['size']):
                        self.gMemory.global_strings.append(None)
                else:
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

        self.tMemory.load(self.variablesTable, self.currFunc)
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
        if(isinstance(pos, str)):
            pos = self.getValue(int(pos[1:]))
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
        # Temp Pointer
        elif(17000 <= pos < 18000):
            if(self.tMemory.temp_pointers_s[-1][pos - 17000] == None):
                print(f"Variable [ {self.getVarID(pos, False)} ] has no value !!!")
                sys.exit()
            return self.tMemory.temp_pointers_s[-1][pos - 17000]

    def doBinomial(self, trials, prob, cases):
        x = random.binomial(n=cases,p=prob, size=trials)
        self.last.append(x)
        print(x)

        sns.displot(random.binomial(n=cases,p=prob, size=trials), kind='hist')
        plt.title('Binomial Distribution')
        plt.show()

    def doPoisson(self, lamb, size):
        x = random.poisson(lam=lamb, size=size)
        self.last.append(x)
        print(x)

        sns.displot(random.poisson(lam=lamb, size=size))
        plt.title('Poisson Distribution')
        plt.show()

    def doCompare(self):
        aux1 = self.last.pop()
        aux2 = self.last.pop()

        sns.displot(aux1)
        sns.displot(aux2)
        plt.show()

    def doNormal(self, mean, stdDev, size1, size2):
        realSize = 0
        if(size1 == 0):
            realSize = size2
        elif(size2 == 0):
            realSize = size1
        
        if(realSize > 0):
            x = random.normal(loc=mean, scale=stdDev, size=realSize)
        else:
            x = random.normal(loc=mean, scale=stdDev, size=(size1, size2))
        print(x)

        if(realSize > 0):
            sns.displot(random.normal(size=realSize), kind='kde')
            plt.title('Normal Distribution')
            plt.show()
        else:
            sns.displot(random.normal(size=(size1, size2)), kind='kde')
            plt.title('Normal Distribution')
            plt.show()

    def doUniform(self, low, high):
        x = random.uniform(low=low, high=high, size=1000)
        count, bins, ignored = plt.hist(x, 20, density=True)
        plt.plot(bins, np.ones_like(bins),color='r')
        plt.title('Uniform Distribution')
        plt.ylabel('Density')
        plt.xlabel('Values')
        plt.show()

    def auxLogi(self, x, mean, stdDev):
        return np.exp((mean - x) / stdDev) / (stdDev * (1 + np.exp((mean - x) / stdDev)) ** 2)

    def doLogi(self, mean, stdDev):
        x = random.logistic(loc=mean, scale=stdDev, size=1000)
        count, bins, ignored = plt.hist(x, bins=50)
        aux = self.auxLogi(bins, mean, stdDev)
        plt.plot(bins, aux * count.max() / aux.max())
        plt.title('Logistic Distribution')
        plt.ylabel('Density')
        plt.xlabel('Values')
        plt.show()

    def doExponential(self, df, size1, size2):
        realSize = 0
        if(size1 == 0):
            realSize = size2
        elif(size2 == 0):
            realSize = size1
        
        if(realSize > 0):
            x = random.exponential(scale=df, size=realSize)
        else:
            x = random.exponential(scale=df, size=(size1, size2))
        print(x)

        if(realSize > 0):
            sns.displot(random.exponential(size=realSize), kind='kde')
            plt.title('Exponential Distribution')
            plt.show()
        else:
            sns.displot(random.exponential(size=(size1, size2)), kind='kde')
            plt.title('Exponential Distribution')
            plt.show()

    def doChiSquare(self, df, size1, size2):
        realSize = 0
        if(size1 == 0):
            realSize = size2
        elif(size2 == 0):
            realSize = size1
        
        if(realSize > 0):
            x = random.exponential(scale=df, size=realSize)
        else:
            x = random.exponential(scale=df, size=(size1, size2))
        print(x)

        if(realSize > 0):
            sns.displot(random.chisquare(df=df, size=realSize), kind='kde')
            plt.title('Chi-Square Distribution')
            plt.show()
        else:
            sns.displot(random.chisquare(df=df, size=(size1, size2)), kind='kde')
            plt.title('Chi-Square Distribution')
            plt.show()

    def exec(self):
        quadCont = 0
        pending_s = deque()
        params_s = deque()
        funcs_s = deque()
        self.lMemory.load(self.variablesTable, self.currFunc, [0, 0, 0, 0])
        self.lMemory.reset()

        while(quadCont < len(self.quadruplesList)):
            oper = self.quadruplesList[quadCont].operator
            operand1 = self.quadruplesList[quadCont].operand1
            operand2 = self.quadruplesList[quadCont].operand2
            temp = self.quadruplesList[quadCont].temp

            if(oper == 'GOTO'):
                quadCont = temp
                continue
            elif(oper == 'GOTOF'):
                if(self.getValue(operand1) == False):
                    quadCont = temp
                    continue
            elif(oper == 'ERA'):
                self.currFunc = temp
                aux = []
                funcs_s.append(self.currFunc)
                auxParams = [self.variablesTable[self.currFunc]['numParams'][0], self.variablesTable[self.currFunc]['numParams'][1], self.variablesTable[self.currFunc]['numParams'][2], self.variablesTable[self.currFunc]['numParams'][3]]
                self.lMemory.load(self.variablesTable, self.currFunc, auxParams)
                self.tMemory.load(self.variablesTable, self.currFunc)

                for key, value in self.variablesTable[self.currFunc]['vars'].items():
                    aux.append(key)
                params_s.append(aux)
            elif(oper == 'GOSUB'):
                self.lMemory.reset()
                self.tMemory.reset()
                if(isinstance(temp, str)):
                    if(temp == 'binomial'):
                        self.doBinomial(self.lMemory.local_ints_s[-1][0], self.lMemory.local_floats_s[-1][0], self.lMemory.local_ints_s[-1][1])
                    elif(temp == 'poisson'):
                        self.doPoisson(self.lMemory.local_ints_s[-1][0], self.lMemory.local_ints_s[-1][1])
                    elif(temp == 'compare'):
                        self.doCompare()
                    elif(temp == 'normal'):
                        self.doNormal(self.lMemory.local_floats_s[-1][0], self.lMemory.local_floats_s[-1][1], self.lMemory.local_ints_s[-1][0], self.lMemory.local_ints_s[-1][1])
                    elif(temp == 'uniform'):
                        self.doUniform(self.lMemory.local_floats_s[-1][0], self.lMemory.local_floats_s[-1][1])
                    elif(temp == 'logi'):
                        self.doLogi(self.lMemory.local_floats_s[-1][0], self.lMemory.local_floats_s[-1][1])
                    elif(temp == 'exponential'):
                        self.doExponential(self.lMemory.local_floats_s[-1][0], self.lMemory.local_ints_s[-1][0],  self.lMemory.local_ints_s[-1][1])
                    elif(temp == 'chiSquare'):
                        self.doChiSquare(self.lMemory.local_floats_s[-1][0], self.lMemory.local_ints_s[-1][0],  self.lMemory.local_ints_s[-1][1])
                    self.lMemory.delete()
                    self.tMemory.delete()
                else:
                    jump = self.currFunc
                    for key, value in self.variablesTable.items():
                        if(value['start'] == temp):
                            jump = key
                            continue
                    self.currFunc = jump
                    pending_s.append(quadCont)
                    quadCont = temp
                    continue
            elif(oper == 'PARAM'):
                aux2 = re.findall(r'\d+', temp)
                
                if(isinstance(operand1, str)):
                    operand1 = self.getValue(int(operand1[1:]))
                if(len(params_s[-1]) > 0):
                    if((1000 <= operand1 < 2000) or (5000 <= operand1 < 6000) or (9000 <= operand1 < 10000) or (13000 <= operand1 < 14000)):
                        self.lMemory.local_ints[self.variablesTable[self.currFunc]['vars'][params_s[-1][int(aux2[0])]]['memoryPos'] - 5000] = self.getValue(operand1)
                    if((2000 <= operand1 < 3000) or (6000 <= operand1 < 7000) or (10000 <= operand1 < 11000) or (14000 <= operand1 < 15000)):
                        self.lMemory.local_floats[self.variablesTable[self.currFunc]['vars'][params_s[-1][int(aux2[0])]]['memoryPos'] - 6000] = self.getValue(operand1)
                    if((3000 <= operand1 < 4000) or (7000 <= operand1 < 8000) or (11000 <= operand1 < 12000) or (15000 <= operand1 < 16000)):
                        self.lMemory.local_bools[self.variablesTable[self.currFunc]['vars'][params_s[-1][int(aux2[0])]]['memoryPos'] - 7000] = self.getValue(operand1)
                    if((4000 <= operand1 < 5000) or (8000 <= operand1 < 9000) or (12000 <= operand1 < 13000) or (16000 <= operand1 < 17000)):
                        self.lMemory.local_strings[self.variablesTable[self.currFunc]['vars'][params_s[-1][int(aux2[0])]]['memoryPos'] - 8000] = self.getValue(operand1)
            elif(oper == 'RET'):
                aux = self.variablesTable[self.currFunc]['type']

                pos = 0
                if(aux != ''):
                    pos = self.variablesTable[self.programID]['vars'][self.currFunc]['memoryPos']

                if(temp != None):
                    if(aux == 'int'):
                        self.gMemory.global_ints[pos - 1000] = self.getValue(temp)
                    elif(aux == 'float'):
                        self.gMemory.global_floats[pos - 2000] = self.getValue(temp)
                    elif(aux == 'bool'):
                        self.gMemory.global_bools[pos - 2000] = self.getValue(temp)
                    elif(aux == 'string'):
                        self.gMemory.global_strings[pos - 2000] = self.getValue(temp)

                self.lMemory.delete()
                self.tMemory.delete()
                quadCont = pending_s.pop() + 1
                params_s.pop()
                if(len(funcs_s) > 1):
                    funcs_s.pop()
                    self.currFunc = funcs_s.pop()
                continue
            elif(oper == 'ENDPROC'):
                self.tMemory.delete()
                self.lMemory.delete()
                quadCont = pending_s.pop() + 1
                params_s.pop()
                funcs_s.pop()
                if(len(funcs_s) > 1):
                    funcs_s.pop()
                    self.currFunc = funcs_s.pop()
                continue
            elif(oper == 'VER'):
                if(self.getValue(operand1) < self.getValue(operand2) or self.getValue(operand1) >= self.getValue(temp)):
                    print(f"Index [ {self.getValue(operand1)} ] out of bounds !!!")
                    sys.exit()
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
                elif(17000 <= temp < 18000):
                    self.tMemory.temp_pointers_s[-1][temp - 17000] = self.getValue(operand1) + self.getValue(operand2)
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
                # if(isinstance(temp, str)):
                #     temp = int(temp[1:])
                resString = str(temp)
                if(resString[0] == '*'):
                    temp = self.getValue(int(resString[1:]))
                
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
                elif(13000 <= temp < 14000):
                    self.tMemory.temp_ints_s[-1][temp - 13000] = self.getValue(operand1)
                elif(17000 <= temp < 18000):
                    self.tMemory.temp_pointers_s[-1][temp - 17000] = self.getValue(operand1)
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
            quadCont += 1
