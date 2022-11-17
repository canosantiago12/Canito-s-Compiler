import sys

class localMemory():
    def __init__(self) -> None:
        self.localInt = 5000
        self.localFloat = 6000
        self.localBool = 7000
        self.localString = 8000

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

    def __str__(self):
        return f'Current local pos (int/float/bool/string): {self.localInt} {self.localFloat} {self.localBool} {self.localString}'