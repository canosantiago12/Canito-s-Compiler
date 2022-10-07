import ply.yacc as yacc
import sys
from lexer import *

#====== PARSER ======#
# Main function variables and functions
def p_mainFunction(p):
    '''
    program_main :  PROGRAM CTE_ID SEMI_COLON globalVariables globalFunctions MAIN LEFT_BRACKET RIGHT_BRACKET func_body
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

# Variables
def p_vars(p):
    '''
    vars : VAR vars_aux
    '''

def p_vars_aux(p):
    '''
    vars_aux : type vars_type
             | type vars_type_array
             | type vars_type_matrix
             | empty
    '''

def p_vars_type(p):
    '''
    vars_type : CTE_ID COMMA vars_type
              | CTE_ID SEMI_COLON vars_aux
    '''

def p_vars_type_array(p):
    '''
    vars_type_array : CTE_ID LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_array
                    | CTE_ID LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON vars_aux
    '''

def p_vars_type_matrix(p):
    '''
    vars_type_matrix : CTE_ID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_matrix
                     | CTE_ID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON vars_aux
    '''

# Error handling
def p_error(p):
    print(f'Syntax error at {p.value!r}')
    sys.exit()

# Empty production
def p_empty(p):
    'empty :'
    pass

parser = yacc.yacc()