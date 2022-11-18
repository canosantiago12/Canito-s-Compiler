import sys
from collections import deque

class temporalMemory():
    def __init__(self) -> None:
        self.tempInt = 13000
        self.tempFloat = 14000
        self.tempBool = 15000
        self.tempString = 16000
        self.tempPointer = 17000

        self.temp_ints = []
        self.temp_ints_s = deque()
        self.temp_floats = []
        self.temp_floats_s = deque()
        self.temp_bools = []
        self.temp_bools_s = deque()
        self.temp_strings = []
        self.temp_strings_s = deque()

    def malloc(self, tempType, size):
        if tempType == 'int':
            if self.tempInt > 12999 and self.tempInt < 14000:
                self.tempInt = self.tempInt + size
                return self.tempInt - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif tempType == 'float':
            if self.tempFloat > 13999 and self.tempFloat < 15000:
                self.tempFloat = self.tempFloat + size
                return self.tempFloat - size
            else:
                print('Ran out of memory! :( BB')
                sys.exit()
        elif tempType == 'bool':
            if self.tempBool > 14999 and self.tempBool < 16000:
                self.tempBool = self.tempBool + size
                return self.tempBool - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif tempType == 'string':
            if self.tempString > 15999 and self.tempString < 17000:
                self.tempString = self.tempString + size
                return self.tempString - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif tempType == 'pointer':
            if self.tempPointer > 16999 and self.tempPointer < 18000:
                self.tempPointer = self.tempPointer + size
                return self.tempPointer - size
            else:
                print('Ran out of memory! :(')
                sys.exit()

    def reset(self):
        self.temp_ints_s.append(self.temp_ints)
        self.temp_ints = []
        self.temp_floats_s.append(self.temp_floats)
        self.temp_floats = []
        self.temp_bools_s.append(self.temp_bools)
        self.temp_bools = []
        self.temp_strings_s.append(self.temp_strings)
        self.temp_strings = []

    def free(self):
        self.tempInt = 13000
        self.tempFloat = 14000
        self.tempBool = 15000
        self.tempString = 16000
        self.tempPointer = 17000
        
    def __str__(self):
        return f'Current const pos (int/float/bool/string): {self.tempInt} {self.tempFloat} {self.tempBool} {self.tempString}'