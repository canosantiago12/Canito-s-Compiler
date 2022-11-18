import sys

class constantMemory():
    def __init__(self) -> None:
        self.constantInt = 9000
        self.constantFloat = 10000
        self.constantBool = 11000
        self.constantString = 12000

        self.const_ints = []
        self.const_floats = []
        self.const_bools = []
        self.const_strings = []

    def malloc(self, consType, size):
        if consType == 'int':
            if self.constantInt > 8999 and self.constantInt < 10000:
                self.constantInt = self.constantInt + size
                return self.constantInt - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif consType == 'float':
            if self.constantFloat > 9999 and self.constantFloat < 11000:
                self.constantFloat = self.constantFloat + size
                return self.constantFloat - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif consType == 'bool':
            if self.constantBool > 10999 and self.constantBool < 12000:
                self.constantBool = self.constantBool + size
                return self.constantBool - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif consType == 'string':
            if self.constantString > 11999 and self.constantString < 13000:
                self.constantString = self.constantString + size
                return self.constantString - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        
    def __str__(self):
        return f'Current const pos (int/float/bool/string): {self.constantInt} {self.constantFloat} {self.constantBool} {self.constantString}'