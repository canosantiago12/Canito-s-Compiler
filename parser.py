import ply.yacc as yacc
import sys
from lexer import *
from utilities import *

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

variablesTable = {}

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
    vars : VAR type vars_type
         | VAR type vars_type_array
         | VAR type vars_type_matrix
         | empty
    '''

def p_vars_type(p):
    '''
    vars_type : CTE_ID saveVariableID COMMA vars_type
              | CTE_ID saveVariableID SEMI_COLON vars
    '''

def p_vars_type_array(p):
    '''
    vars_type_array : CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_array
                    | CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON vars
    '''

def p_vars_type_matrix(p):
    '''
    vars_type_matrix : CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_matrix
                     | CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON vars
    '''

# Functions Rules
def p_funcs(p):
    '''
    funcs : funcs_aux globalFunctions
    '''

def p_funcs_aux(p):
    '''
    funcs_aux : FUNC type CTE_ID saveFuncID LEFT_PAREN RIGHT_PAREN funcBody
    '''

def p_funcBody(p):
    '''
    funcBody : LEFT_CURLY_BRACKET auxFuncBody RIGHT_CURLY_BRACKET
    '''

def p_auxFuncBody(p):
    '''
    auxFuncBody : vars
    '''

# Read Rule
def p_read(p):
    '''
    read : READ_INPUT LEFT_PAREN RIGHT_PAREN SEMI_COLON
    '''

# Variables Type
def p_type(p):
    '''
    type : INT setCurrentType
         | FLOAT setCurrentType
         | BOOL setCurrentType
         | STRING setCurrentType
    '''

#==== POINTS ====#
def p_startup(p):
    'startup :'
    global funcID, programID

    program = p[-1]
    funcID = program
    #variablesTable[program] = {'type' : 'void', 'vars' : {}}

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

    #print(funcID, currType)

def p_saveVariableID(p):
    'saveVariableID :'
    global varID, currType

    varID = p[-1]
    if varID not in variablesTable[funcID]['vars']:
        variablesTable[funcID]['vars'][varID] = {'type': currType}
    else:
        print(f'Variable \'{varID}\' has already been declared!')

    #print(f'Variable id = {p[-1]}')

def p_setCurrentType(p):
    'setCurrentType :'
    global currType

    currType = p[-1]
    #print(p[-1])

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