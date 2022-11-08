class Quadruple:
    def __init__(self, operator, operand1, operand2, temp):
        self.operator = operator
        self.operand1 = operand1
        self.operand2 = operand2
        self.temp = temp

    def __str__(self):
        return f'[{self.operator}][{self.operand1}][{self.operand2}][{self.temp}]'
