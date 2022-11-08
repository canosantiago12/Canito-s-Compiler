import ply.yacc as yacc
import sys

from lexer import *
from utilities import *
from collections import deque

# Semantic Cube
# Using a nested dictionary to create a relationship ALL to ALL and allow to reconize type mismatch errors
CUBE = {
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
        }
    }
}

#Quadruple's Stacks
operatorStack = deque()
operandsStack = deque()
typesStack = deque()
jumpsStack = deque()

variablesTable = {}
quadruplesList = []
quadsCont = 0

funcID = ''
programID = ''
varID = ''
varType = ''
currType = ''

#====== PARSER ======#
# Main function variables and functions Rules
def p_mainFunction(p):
    '''
    program_main : PROGRAM CTE_ID startup SEMI_COLON globalVariables globalFunctions MAIN saveFuncID LEFT_PAREN RIGHT_PAREN funcBody endPrint
    '''

def p_globalVariables(p):
    '''
    globalVariables : vars
                    | empty
    '''

def p_globalFunctions(p):
    '''
    globalFunctions : funcs
                    | empty
    '''

# Variables Rules
def p_vars(p):
    '''
    vars : auxVars
    '''

def p_auxVars(p):
    '''
    auxVars : VAR type vars_type_single
            | VAR type vars_type_array
            | VAR type vars_type_matrix
            | empty
    '''

def p_vars_type_single(p):
    '''
    vars_type_single : CTE_ID saveVariableID COMMA vars_type_single
                     | CTE_ID saveVariableID SEMI_COLON auxVars
    '''

def p_vars_type_array(p):
    '''
    vars_type_array : CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_array
                    | CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON auxVars
    '''

def p_vars_type_matrix(p):
    '''
    vars_type_matrix : CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_matrix
                     | CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON auxVars
    '''

# Functions Rules
def p_funcs(p):
    '''
    funcs : funcs_aux globalFunctions
    '''

def p_funcs_aux(p):
    '''
    funcs_aux : FUNC type CTE_ID saveFuncID LEFT_PAREN RIGHT_PAREN funcBody endFunction
    '''

def p_funcBody(p):
    '''
    funcBody : LEFT_CURLY_BRACKET auxFuncBody RIGHT_CURLY_BRACKET
    '''

def p_auxFuncBody(p):
    '''
    auxFuncBody : vars statements auxFuncBody
                | statements auxFuncBody
                | empty
    '''

# Function return Rules
# def p_return(p):
#     '''
#     return : RETURN LEFT_PAREN RIGHT_PAREN SEMI_COLON
#     '''

# Variables type Rules
def p_type(p):
    '''
    type : INT setCurrentType
         | FLOAT setCurrentType
         | BOOL setCurrentType
         | STRING setCurrentType
    '''

# Statements Rules
def p_statements(p):
    '''
    statements : assignment
    '''

# Assing Rules
def p_assignment(p):
    '''
    assignment : CTE_ID addOperand EQUAL addOperator logicExpression doAssign SEMI_COLON
    '''

# Expressions Rules
def p_logicExpression(p):
    '''
    logicExpression : exp auxLogicExpression
    '''

def p_auxLogicExpression(p):
    '''
    auxLogicExpression : AND logicExpression
                       | OR logicExpression
                       | empty
    '''

def p_exp(p):
    '''
    exp : exp2 auxExp
    '''

def p_auxExp(p):
    '''
    auxExp : GREATER_THAN exp
           | GREATER_EQUAL_THAN exp
           | LESS_THAN exp
           | LESS_EQUAL_THAN exp
           | NOT_EQUALS exp
           | EQUALS exp
           | empty
    '''

def p_exp2(p):
    '''
    exp2 : term doExpression exp2Aux
    '''

def p_exp2Aux(p):
    '''
    exp2Aux : PLUS addOperator exp2
            | MINUS addOperator exp2
            | empty
    '''

def p_term(p):
    '''
    term : factor auxTerm
    '''

def p_auxTerm(p):
    '''
    auxTerm : TIMES term
            | DIV term
            | MOD term
            | EXP term
            | empty
    '''

def p_factor(p):
    '''
    factor : constants
    '''

def p_constants(p):
    '''
    constants : CTE_ID addOperand
              | CTE_INT
              | CTE_FLOAT
              | TRUE
              | FALSE
    '''

# Read Rules
#def p_reading(p):
   # '''
   # reading : READ_INPUT LEFT_PAREN RIGHT_PAREN SEMI_COLON
   # '''

#==== POINTS ====#
def p_startup(p):
    'startup :'
    global funcID, programID

    programID = p[-1]
    funcID = programID

    variablesTable[programID] = {'type' : 'void', 'vars' : {}}

def p_endPrint(p):
    'endPrint :'
    print(variablesTable)

def p_saveFuncID(p):
    'saveFuncID :'
    global funcID, currType

    funcID = p[-1]
    if(funcID not in variablesTable):
        variablesTable[funcID] = {'type': currType, 'vars': {}}
    else:
        print(f'Function \'{funcID}\' has already been declared!')
        sys.exit()

    #print(funcID, currType)

def p_endFunction(p):
    'endFunction :'
    global quadsCont
    print("RESET MEMORY")
    quadsCont = 0

def p_saveVariableID(p):
    'saveVariableID :'
    global varID, currType

    varID = p[-1]
    if varID not in variablesTable[funcID]['vars']:
        variablesTable[funcID]['vars'][varID] = {'type': currType}
    else:
        print(f'Variable \'{varID}\' has already been declared!')
        sys.exit()

    #print(f'Variable id = {p[-1]}')

def p_setCurrentType(p):
    'setCurrentType :'
    global currType

    currType = p[-1]
    #print(p[-1])

def p_addOperand(p):
    'addOperand :'

    oper = p[-1]

    if oper in variablesTable[funcID]['vars']:
        operandsStack.append(oper)
        typesStack.append(variablesTable[funcID]['vars'][oper]['type'])
    elif oper in variablesTable[programID]['vars']:
        operandsStack.append(oper)
        typesStack.append(variablesTable[programID]['vars'][oper]['type'])
    else:
        print(f'Variable \'{oper}\' does not exist :(')
        sys.exit()

def p_addOperator(p):
    'addOperator :'
    global operatorStack

    op = p[-1]
    operatorStack.append(op)

# Expressions (SUMS and MINUS)
def p_doExpression(p):
    'doExpression :'
    global operandsStack, operatorStack, typesStack, quadruplesList, quadsCont

    if(len(operatorStack) != 0):
        operator = operatorStack[-1]
        if(operator == '+' or operator == '-'):
            rightOperand = operandsStack.pop()
            leftOperand = operandsStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()
            operator = operatorStack.pop()

            if CUBE[leftType][rightType][operator] == 'error':
                print('ERROR')
                sys.exit()
            else:
                newQuad = Quadruple(operator, leftOperand, rightOperand, 't' + str(quadsCont))
                print(newQuad)
                quadruplesList.append(newQuad)
                operandsStack.append('t' + str(quadsCont))
                typesStack.append(CUBE[leftType][rightType][operator])
                quadsCont += 1

# Assignment
def p_doAssign(p):
    'doAssign :'
    global operandsStack, operatorStack, typesStack, quadruplesList
    
    #print(operandsStack, operatorStack, typesStack)
    rightOperand = operandsStack.pop()
    leftOperand = operandsStack.pop()
    rightType = typesStack.pop()
    leftType = typesStack.pop()
    operator = operatorStack.pop()

    if leftType != rightType:
        print(f'Type missmatch: {leftOperand} with {rightOperand}')
        sys.exit()
    else:
        newQuad = Quadruple(operator, leftOperand, None, rightOperand)
        print(newQuad)
        quadruplesList.append(newQuad)

# Error handling
def p_error(p):
    print(f'Syntax error at {p.value!r}')
    sys.exit()

# Empty production
def p_empty(p):
    'empty :'
    pass

# Build parser
parser = yacc.yacc()

#==== READ INPUT ====#
if __name__ == '__main__':
    fileName = sys.argv[1]
    
    inputFile = open(fileName, 'r')
    inputCode = inputFile.read()
    inputFile.close()

    parser.parse(inputCode)