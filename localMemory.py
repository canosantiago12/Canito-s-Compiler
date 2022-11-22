import sys
from collections import deque

class localMemory():
    def __init__(self) -> None:
        self.localInt = 5000
        self.localFloat = 6000
        self.localBool = 7000
        self.localString = 8000

        self.local_ints = []
        self.local_ints_s = deque()
        self.local_floats = []
        self.local_floats_s = deque()
        self.local_bools = []
        self.local_bools_s = deque()
        self.local_strings = []
        self.local_strings_s = deque()

    def malloc(self, localType, size):
        if localType == 'int':
            if self.localInt > 4999 and self.localInt < 6000:
                self.localInt = self.localInt + size
                return self.localInt - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif localType == 'float':
            if self.localFloat > 5999 and self.localFloat < 7000:
                self.localFloat = self.localFloat + size
                return self.localFloat - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif localType == 'bool':
            if self.localBool > 6999 and self.localBool < 8000:
                self.localBool = self.localBool + size
                return self.localBool - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif localType == 'string':
            if self.localString > 7999 and self.localString < 9000:
                self.localString = self.localString + size
                return self.localString - size
            else:
                print('Ran out of memory! :(')
                sys.exit()

    def reset(self):
        self.local_ints_s.append(self.local_ints)
        self.local_ints = []
        self.local_floats_s.append(self.local_floats)
        self.local_floats = []
        self.local_bools_s.append(self.local_bools)
        self.local_bools = []
        self.local_strings_s.append(self.local_strings)
        self.local_strings = []

    def free(self):
        self.localInt = 5000
        self.localFloat = 6000
        self.localBool = 7000
        self.localString = 8000

    def load(self, variablesTable, currFunc, params):
        # Loading Local Memory For Main Function
        for i in range(0, variablesTable[currFunc]['numVars'][0] + params[0]):
            self.local_ints.append(None)
        for i in range(0, variablesTable[currFunc]['numVars'][1] + params[1]):
            self.local_floats.append(None)
        for i in range(0, variablesTable[currFunc]['numVars'][2] + params[2]):
            self.local_bools.append(None)
        for i in range(0, variablesTable[currFunc]['numVars'][3] + params[3]):
            self.local_strings.append(None)

    def delete(self):
        self.local_ints_s.pop()
        self.local_floats_s.pop()
        self.local_bools_s.pop()
        self.local_strings_s.pop()

    def __str__(self):
        return f'Current local pos (int/float/bool/string): {self.localInt} {self.localFloat} {self.localBool} {self.localString}'