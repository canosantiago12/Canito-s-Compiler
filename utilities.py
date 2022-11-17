class Quadruple:
    def __init__(self, operator, operand1, operand2, temp):
        self.operator = operator
        self.operand1 = operand1
        self.operand2 = operand2
        self.temp = temp

    def __str__(self):
        return f'[{self.operator}][{self.operand1}][{self.operand2}][{self.temp}]'

class Cube:
    def __init__(self) -> None:
        self.CUBE = {
            'int' : {
                'int' : {
                    '+' : 'int',
                    '-' : 'int',
                    '*' : 'int',
                    '/' : 'int',
                    '%' : 'int',
                    '^' : 'int',
                    '>' : 'bool',
                    '>=' : 'bool',
                    '<' : 'bool',
                    '<=' : 'bool',
                    '==' : 'bool',
                    '!=' : 'bool',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'float' : {
                    '+' : 'float',
                    '-' : 'float',
                    '*' : 'float',
                    '/' : 'float',
                    '%' : 'float',
                    '^' : 'float',
                    '>' : 'bool',
                    '>=' : 'bool',
                    '<' : 'bool',
                    '<=' : 'bool',
                    '==' : 'bool',
                    '!=' : 'bool',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'bool' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'error',
                    '!=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'string' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'error',
                    '!=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                }
            },
            'float' : {
                'int' : {
                    '+' : 'float',
                    '-' : 'float',
                    '*' : 'float',
                    '/' : 'float',
                    '%' : 'float',
                    '^' : 'float',
                    '>' : 'bool',
                    '>=' : 'bool',
                    '<' : 'bool',
                    '<=' : 'bool',
                    '==' : 'bool',
                    '!=' : 'bool',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'float' : {
                    '+' : 'float',
                    '-' : 'float',
                    '*' : 'float',
                    '/' : 'float',
                    '%' : 'float',
                    '^' : 'float',
                    '>' : 'bool',
                    '>=' : 'bool',
                    '<' : 'bool',
                    '<=' : 'bool',
                    '==' : 'bool',
                    '!=' : 'bool',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'bool' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'error',
                    '!=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'string' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'error',
                    '!=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                }
            },
            'bool' : {
                'int' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'error',
                    '!=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'float' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'error',
                    '!=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'bool' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'bool',
                    '!=' : 'bool',
                    '&&' : 'bool',
                    '||' : 'bool'
                },
                'string' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'error',
                    '!=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                }
            },
            'string' : {
                'int' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'error',
                    '!=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'float' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'error',
                    '!=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'bool' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'error',
                    '!=' : 'error',
                    '&&' : 'error',
                    '||' : 'error'
                },
                'string' : {
                    '+' : 'error',
                    '-' : 'error',
                    '*' : 'error',
                    '/' : 'error',
                    '%' : 'error',
                    '^' : 'error',
                    '>' : 'error',
                    '>=' : 'error',
                    '<' : 'error',
                    '<=' : 'error',
                    '==' : 'bool',
                    '!=' : 'bool',
                    '&&' : 'error',
                    '||' : 'error'
                }
            }
        }