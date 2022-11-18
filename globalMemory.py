import sys

class globalMemory():
    def __init__(self) -> None:
        self.globalInt = 1000
        self.globalFloat = 2000
        self.globalBool = 3000
        self.globalString = 4000

        self.global_ints = []
        self.global_floats = []
        self.global_bools = []
        self.global_strings = []

    def malloc(self, globalType, size):
        if globalType == 'int':
            if self.globalInt > 999 and self.globalInt < 2000:
                self.globalInt = self.globalInt + size
                return self.globalInt - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif globalType == 'float':
            if self.globalFloat > 1999 and self.globalFloat < 3000:
                self.globalFloat = self.globalFloat + size
                return self.globalFloat - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif globalType == 'bool':
            if self.globalBool > 2999 and self.globalBool < 4000:
                self.globalBool = self.globalBool + size
                return self.globalBool - size
            else:
                print('Ran out of memory! :(')
                sys.exit()
        elif globalType == 'string':
            if self.globalString > 3999 and self.globalString < 5000:
                self.globalString = self.globalString + size
                return self.globalString - size
            else:
                print('Ran out of memory! :(')
                sys.exit()