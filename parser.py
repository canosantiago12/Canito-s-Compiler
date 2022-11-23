import ply.yacc as yacc
import sys

from lexer import *
from utilities import *
from collections import deque
from constantMemory import *
from tempMemory import *
from globalMemory import *
from localMemory import *
from virtualMachine import *

# Memory
cMemory = constantMemory()
tMemory = temporalMemory()
gMemory = globalMemory()
lMemory = localMemory()

# Variables Table (dictionary)
variablesTable = {}

# Coounters for variables, parameters and temp per function
auxVars = [0, 0, 0, 0]
auxTemps = [0, 0, 0, 0, 0]
auxParams = [0, 0, 0, 0]

# Constants table with every constant of tipe 'x'
constantsTable = {'int': {}, 'float': {}, 'bool': {}, 'string': {}}

# Semantic Cube
# Using a nested dictionary to create a relationship ALL to ALL and allow to reconize type mismatch errors
semanticCube = Cube().CUBE

# Quadruple's Stacks
operatorStack = deque()
operandsStack = deque()
typesStack = deque()
jumpsStack = deque()

# Main quadruple list
quadruplesList = []
quadsCont = 0

# Temp variables to keep track of current values
funcID = ''
auxFunc = ''
programID = ''
varID = ''
currType = ''
flagReturn = False
contParams = 0

#====== PARSER ======#
# Main function variables and functions Rules
def p_mainFunction(p):
    '''
    program_main : BTSProgram CTE_ID startup SEMI_COLON globalVariables globalFunctions MAIN saveFuncID addMemoryInfo LEFT_PAREN RIGHT_PAREN setMain funcBody endFunction endProgram
    '''

def p_globalVariables(p):
    '''
    globalVariables : vars addMemoryInfo
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
            | empty
    '''

def p_vars_type_single(p):
    '''
    vars_type_single : CTE_ID saveVariableID COMMA vars_type_single
                     | CTE_ID saveVariableID SEMI_COLON auxVars
    '''

def p_vars_type_array(p):
    '''
    vars_type_array : CTE_ID LEFT_BRACKET CTE_INT addConstantOperand RIGHT_BRACKET saveArray COMMA vars_type_array
                    | CTE_ID LEFT_BRACKET CTE_INT addConstantOperand RIGHT_BRACKET saveArray SEMI_COLON auxVars
    '''

# Functions Rules
def p_funcs(p):
    '''
    funcs : funcs_aux globalFunctions
    '''

def p_funcs_aux(p):
    '''
    funcs_aux : FUNC type CTE_ID saveFuncID LEFT_PAREN params RIGHT_PAREN funcBody addMemoryInfo endFunction
              | FUNC CTE_ID saveFuncID setVoidType LEFT_PAREN params RIGHT_PAREN funcBody addMemoryInfo endFunction
    '''

def p_params(p):
    '''
    params : auxParams
          | empty
    '''

def p_auxParams(p):
    '''
    auxParams : type CTE_ID addParam multipleParams
              | type CTE_ID addParam LEFT_BRACKET CTE_INT RIGHT_BRACKET multipleParams
    '''

def p_multipleParams(p):
    '''
    multipleParams : COMMA auxParams
                   | empty
    '''

def p_funcBody(p):
    '''
    funcBody : LEFT_CURLY_BRACKET auxFuncBody RIGHT_CURLY_BRACKET
    '''

def p_auxFuncBody(p):
    '''
    auxFuncBody : vars statements auxFuncBody
                | statements auxFuncBody
                | vars
                | empty
    '''

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
               | writting
               | reading
               | if
               | while
               | auxFuncCall
               | return
    '''

# Assign Rules
def p_assignment(p):
    '''
    assignment : CTE_ID addOperand EQUAL addOperator logicExpression doAssign SEMI_COLON
               | CTE_ID LEFT_BRACKET addParenthesis logicExpression RIGHT_BRACKET addOperand removeParenthesis EQUAL addOperator logicExpression doAssign SEMI_COLON
    '''

# Writting Rules
def p_writting(p):
    '''
    writting : PRINT LEFT_PAREN auxWritting RIGHT_PAREN SEMI_COLON
    '''

def p_auxWritting(p):
    '''
    auxWritting : logicExpression doWrite multipleWrite
                | CTE_STRING doWriteString multipleWrite
    '''

def p_multipleWrite(p):
    '''
    multipleWrite : COMMA auxWritting
                  | empty
    '''

# Reading Rules
def p_reading(p):
    '''
    reading : READ_INPUT LEFT_PAREN auxReading RIGHT_PAREN SEMI_COLON
    '''

def p_auxReading(p):
    '''
    auxReading : CTE_ID addOperand doReading multipleRead
    '''

def p_multipleRead(p):
    '''
    multipleRead : COMMA auxReading
                 | empty
    '''

# Logic Expressions Rules
def p_logicExpression(p):
    '''
    logicExpression : exp doLogicExpression auxLogicExpression
    '''

def p_auxLogicExpression(p):
    '''
    auxLogicExpression : AND addOperator logicExpression
                       | OR addOperator logicExpression
                       | empty
    '''

# Comparison Expressions Rules
def p_exp(p):
    '''
    exp : exp2 doCompExpression auxExp
    '''

def p_auxExp(p):
    '''
    auxExp : GREATER_THAN addOperator exp
           | GREATER_EQUAL_THAN addOperator exp
           | LESS_THAN addOperator exp
           | LESS_EQUAL_THAN addOperator exp
           | NOT_EQUALS addOperator exp
           | EQUALS addOperator exp
           | empty
    '''

# Expressions Rules
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

# Terms Rules
def p_term(p):
    '''
    term : factor doTerm auxTerm
    '''

def p_auxTerm(p):
    '''
    auxTerm : TIMES addOperator term
            | DIV addOperator term
            | MOD addOperator term
            | EXP addOperator term
            | empty
    '''

# Factor Rules
def p_factor(p):
    '''
    factor : LEFT_PAREN addParenthesis logicExpression RIGHT_PAREN removeParenthesis
           | constants
    '''

def p_constants(p):
    '''
    constants : CTE_ID addOperand
              | CTE_ID LEFT_BRACKET addParenthesis logicExpression RIGHT_BRACKET addOperand removeParenthesis
              | CTE_INT addConstantOperand
              | CTE_FLOAT addConstantOperand
              | CTE_STRING addConstantOperand
              | TRUE addConstantBool
              | FALSE addConstantBool
              | functionCall
    '''

# Conditional Rules
def p_if(p):
    '''
    if : IF LEFT_PAREN logicExpression doIF RIGHT_PAREN funcBody else endIF
    '''

def p_else(p):
    '''
    else : ELSE doElse IF LEFT_PAREN logicExpression doIF RIGHT_PAREN funcBody else endIF
         | ELSE doElse funcBody
         | empty
    '''

# While Rules
def p_while(p):
    '''
    while : WHILE LEFT_PAREN addCondStart logicExpression doWhile RIGHT_PAREN funcBody endWhile
    '''

# Function Call Rules
def p_functionCall(p):
    '''
    functionCall : CTE_ID doFuncCall LEFT_PAREN arguments checkParams RIGHT_PAREN doGoSub
                 | BINOMIAL doFuncCall LEFT_PAREN arguments checkParams RIGHT_PAREN doGoSubS
                 | POISSON doFuncCall LEFT_PAREN arguments checkParams RIGHT_PAREN doGoSubS
                 | COMPARE doFuncCall LEFT_PAREN arguments checkParams RIGHT_PAREN doGoSubS
                 | NORMAL doFuncCall LEFT_PAREN arguments checkParams RIGHT_PAREN doGoSubS
                 | UNIFORM doFuncCall LEFT_PAREN arguments checkParams RIGHT_PAREN doGoSubS
                 | LOGISTIC doFuncCall LEFT_PAREN arguments checkParams RIGHT_PAREN doGoSubS
                 | EXPONENTIAL doFuncCall LEFT_PAREN arguments checkParams RIGHT_PAREN doGoSubS
                 | CHISQUARE doFuncCall LEFT_PAREN arguments checkParams RIGHT_PAREN doGoSubS
    '''

def p_auxFuncCall(p):
    '''
    auxFuncCall : functionCall SEMI_COLON
    '''

# Arguments Rules
def p_arguments(p):
    '''
    arguments : auxArguments
              | empty
    '''

def p_auxArguments(p):
    '''
    auxArguments : logicExpression checkType multipleArguments
    '''

def p_multipleArguments(p):
    '''
    multipleArguments : COMMA auxArguments
                      | empty
    '''

# Function Return Rules
def p_return(p):
    '''
    return : RETURN RETURN_SIGN LEFT_PAREN auxReturn RIGHT_PAREN SEMI_COLON
    '''

def p_auxReturn(p):
    '''
    auxReturn : logicExpression doReturn
              | empty
    '''

#==== AUX FUNCS ====#
# Add 1 to global counter of temps according to current type
def addTemp(type):
    global auxTemps
    
    if type == 'int':
        auxTemps[0] += 1
    elif type == 'float':
        auxTemps[1] += 1
    elif type == 'bool':
        auxTemps[2] += 1
    elif type == 'string':
        auxTemps[3] += 1
    elif type == 'pointer':
        auxTemps[4] += 1
    else:
        print("ERROR")
        sys.exit()

# Append to variablesTable the especial fumctions that will always exist
def loadSpecial():
    variablesTable['binomial'] = {'type':'', 'params': {0: 'int', 1:'float', 2: 'int'}, 'vars':{'trials': {'type':'int', 'memoryPos': 5000}, 'prob': {'type': 'floats', 'memoryPos': 6000}, 'cases':{'type': 'int', 'memoryPos': 5001}}, 'start': 0, 'numParams': [2, 1, 0, 0], 'numVars': [0, 0, 0, 0], 'numTemps': [0, 0, 0, 0, 0]}
    variablesTable['poisson'] = {'type':'', 'params': {0: 'int', 1:'int'}, 'vars':{'lambda': {'type':'int', 'memoryPos': 5000}, 'size':{'type': 'int', 'memoryPos': 5001}}, 'start': 0, 'numParams': [2, 0, 0, 0], 'numVars': [0, 0, 0, 0], 'numTemps': [0, 0, 0, 0, 0]}
    variablesTable['compare'] = {'type':'', 'params': {}, 'vars':{}, 'start': 0, 'numParams': [0, 0, 0, 0], 'numVars': [0, 0, 0, 0], 'numTemps': [0, 0, 0, 0, 0]}
    variablesTable['normal'] = {'type':'', 'params': {0: 'float', 1:'float', 2:'int', 3:'int'}, 'vars':{'mean': {'type':'float', 'memoryPos': 6000}, 'stdDev':{'type': 'float', 'memoryPos': 6001}, 'size1': {'type': 'int', 'memoryPos': 5000}, 'size2': {'type': 'int', 'memoryPos': 5001}}, 'start': 0, 'numParams': [2, 2, 0, 0], 'numVars': [0, 0, 0, 0], 'numTemps': [0, 0, 0, 0, 0]}
    variablesTable['uniform'] = {'type':'', 'params': {0: 'float', 1:'float'}, 'vars':{'low': {'type':'float', 'memoryPos': 6000}, 'high':{'type': 'float', 'memoryPos': 6001}}, 'start': 0, 'numParams': [0, 2, 0, 0], 'numVars': [0, 0, 0, 0], 'numTemps': [0, 0, 0, 0, 0]}
    variablesTable['logi'] = {'type':'', 'params': {0: 'float', 1:'float'}, 'vars':{'mean': {'type':'float', 'memoryPos': 6000}, 'stdDev':{'type': 'float', 'memoryPos': 6001}}, 'start': 0, 'numParams': [0, 2, 0, 0], 'numVars': [0, 0, 0, 0], 'numTemps': [0, 0, 0, 0, 0]}
    variablesTable['exponential'] = {'type':'', 'params': {0: 'float', 1:'int', 2: 'int'}, 'vars':{'df': {'type':'float', 'memoryPos': 6000}, 'size1':{'type': 'int', 'memoryPos': 5000}, 'size2': {'type': 'int', 'memoryPos': 5001}}, 'start': 0, 'numParams': [2, 1, 0, 0], 'numVars': [0, 0, 0, 0], 'numTemps': [0, 0, 0, 0, 0]}
    variablesTable['chiSquare'] = {'type':'', 'params': {0: 'float', 1:'int', 2: 'int'}, 'vars':{'df': {'type':'float', 'memoryPos': 6000}, 'size1':{'type': 'int', 'memoryPos': 5000}, 'size2': {'type': 'int', 'memoryPos': 5001}}, 'start': 0, 'numParams': [2, 1, 0, 0], 'numVars': [0, 0, 0, 0], 'numTemps': [0, 0, 0, 0, 0]}

#==== POINTS ====#
# Startup global variables so we can start saving data inside of them.
# Creates first GOTO quadruple going to main funciton
def p_startup(p):
    'startup :'
    global funcID, programID, quadsCont

    loadSpecial()

    programID = p[-1]
    funcID = programID
    variablesTable[programID] = {'type' : '', 'params' : {}, 'vars' : {}, 'start' : quadsCont, 'numVars' : [], 'numTemps' : []}
    newQuad = Quadruple('GOTO', None, None, 'mainStage')
    quadruplesList.append(newQuad)
    quadsCont += 1

# Once reached the end of main, add missing parameter of GOTO
def p_setMain(p):
    'setMain :'
    global quadruplesList, funcID

    quadruplesList[0].temp = quadsCont

# Add END quadruple at the end of the list
def p_endProgram(p):
    'endProgram :'
    global quadruplesList

    newQuad = Quadruple('END', None, None, None)
    quadruplesList.append(newQuad)

# Debugging print
# def p_endPrint(p):
#     'endPrint :'
#     cont = 0
#     for key, value in variablesTable.items():
#         print(key, ' : ', value)

#     print("CONS TABLE", constantsTable)

#     for x in quadruplesList:
#         print(cont, x)
#         cont += 1

#     print(f"OPERATOR STACK = {operatorStack}")
#     print(f"OPERAND STACK = {operandsStack}")
#     print(f"TYPE STACK = {typesStack}")
#     print(f"JUMPS STACK = {jumpsStack}")

# Saves variable function depending if it already exists, if not then create entry inside
# dictionary so we can start adding local variables, paramets, temps, etc.
def p_saveFuncID(p):
    'saveFuncID :'
    global funcID, currType, auxVars, auxTemps

    auxVars = [0 , 0, 0, 0]
    auxTemps = [0, 0, 0, 0, 0]
    funcID = p[-1]
    if(funcID not in variablesTable):
        variablesTable[funcID] = {'type': currType, 'params' : {}, 'vars': {}, 'start' : quadsCont, 'numParams': [0, 0, 0, 0], 'numVars' : [0, 0, 0, 0], 'numTemps' : [0, 0, 0, 0, 0]}
        if(currType != ''):
            if(funcID not in variablesTable[programID]['vars']):
                pos = gMemory.malloc(currType, 1)
                variablesTable[programID]['vars'][funcID] = {'type': currType, 'memoryPos': pos}
            else:
                print(f'Function [ {funcID} ] has already been declared !!!')
                sys.exit()
        lMemory.free()
        tMemory.free()
    else:
        print(f'Function [ {funcID} ] has already been declared !!!')
        sys.exit()

# Add parameter to current functions params key and increase the counter of params per function.
def p_addParam(p):
    'addParam :'
    global funcID, varID, auxParams, currType

    varID = p[-1]
    if varID not in variablesTable[funcID]['vars']:
        aux = 0
        pos = lMemory.malloc(currType, 1)
        variablesTable[funcID]['vars'][varID] = {'type': currType, 'memoryPos': pos}

        if(len(variablesTable[funcID]['params'])) == 0:
            auxParams = [0, 0, 0, 0]

        if(currType == 'int'):
            aux = auxParams[0]
            auxParams[0] += 1
        elif(currType == 'float'):
            aux = auxParams[1]
            auxParams[1] += 1
        elif(currType == 'bool'):
            aux = auxParams[2]
            auxParams[2] += 1
        elif(currType == 'string'):
            aux = auxParams[3]
            auxParams[3] += 1

        variablesTable[funcID]['params'][aux] = currType
    else:
        print(f'Variable [ {varID} ] has already been declared !!!')
        sys.exit()    

# Save current counter to variablesTable[funcID] so we can restart the counters safely
def p_addMemoryInfo(p):
    'addMemoryInfo :'
    global variablesTable, auxParams, currType

    variablesTable[funcID]['numVars'] = auxVars
    variablesTable[funcID]['numParams'] = auxParams
    auxParams = [0, 0, 0, 0]

# Verify if type of function is empty and we detected the token for return, exit since we shouldn't have a return.
# If it is different != '' verify that said return matches the current function type
def p_endFunction(p):
    'endFunction :'
    global quadruplesList, variablesTable, quadsCont, currType, flagReturn

    if(funcID != 'mainStage'):
        if(variablesTable[funcID]['type'] == '' and flagReturn):
            print(f'Function [ {funcID} ] expects no return value !!!')
            sys.exit()
        if(variablesTable[funcID]['type'] != '' and not flagReturn):
            print(f"Function [ {funcID} ] expects [ {variablesTable[funcID]['type']} ] no return value !!!")
            sys.exit()
        newQuad = Quadruple('ENDPROC', None, None, None)
        quadruplesList.append(newQuad)
        quadsCont += 1
    variablesTable[funcID]['numTemps'] = auxTemps
    currType = ''
    tMemory.free()
    lMemory.free()
    flagReturn = False

# Save current variable into variables table and increase virtual memory counter depending
# on the type of the variable and the scope
def p_saveVariableID(p):
    'saveVariableID :'
    global varID, currType, auxVars

    varID = p[-1]
    if varID not in variablesTable[funcID]['vars']:
        pos = 0

        if(funcID == programID):
            pos = gMemory.malloc(currType, 1)
        else:
            pos = lMemory.malloc(currType, 1)

        if currType == 'int':
            auxVars[0] += 1
        elif currType == 'float':
            auxVars[1] += 1
        elif currType == 'bool':
            auxVars[2] += 1
        else:
            auxVars[3] += 1
        variablesTable[funcID]['vars'][varID] = {'type': currType, 'memoryPos': pos}
    else:
        print(f'Variable [ {varID} ] has already been declared !!!')
        sys.exit()

# Save current variable array id inside variablesTable but instead of just adding 1 to the memory
# we need to add the full lenght of the array since we need 'x' memory positions not just 1.
# We need to add 0 since we need to work with VER quadruple that verifies that index 'x' is between
# 0 and the size of the array
def p_saveArray(p):
    'saveArray :'
    global varID, currType, typesStack, operandsStack

    varID = p[-5]
    size1 = p[-3]
    typesStack.pop()
    operandsStack.pop()
    pos = 0

    if(funcID == programID):
        pos = gMemory.malloc(currType, size1)
    else:
        pos = lMemory.malloc(currType, size1)
    
    if(varID not in variablesTable[funcID]['vars']):
        variablesTable[funcID]['vars'][varID] = {'type': currType, 'memoryPos': pos, 'size': size1}
        if currType == 'int':
            auxVars[0] += size1
        elif currType == 'float':
            auxVars[1] += size1
        elif currType == 'bool':
            auxVars[2] += size1
        else:
            auxVars[3] += size1
    else:
        print(f'Variable [ {varID} ] has already been declared !!!')
        sys.exit()

    auxPos = pos
    if(auxPos not in constantsTable['int']):
        pos = cMemory.malloc('int', 1)
        constantsTable['int'][auxPos] = {'type': 'int', 'memoryPos': pos}
    if(0 not in constantsTable['int']):
        pos = cMemory.malloc('int', 1)
        constantsTable['int'][0] = {'type': 'int', 'memoryPos': pos}
    if(size1 not in constantsTable['int']):
        pos = cMemory.malloc('int', 1)
        constantsTable['int'][size1] = {'type': 'int', 'memoryPos': pos}

# Whenever we detect a toket of type INT, FLOAT, STRING, BOOL, we need to save
# the current type into temp variable.
def p_setCurrentType(p):
    'setCurrentType :'
    global currType

    currType = p[-1]

# Add operand to operandsStack and typesStack current operand and it's type
# if operand is an array we need to verify before adding, because whe shoul exit
# if the index is greater than our current array size
def p_addOperand(p):
    'addOperand :'
    global operandsStack, typesStack, quadruplesList, quadsCont

    oper = p[-1]
    if(oper != ']'):
        if oper in variablesTable[funcID]['vars']:
            operandsStack.append(variablesTable[funcID]['vars'][oper]['memoryPos'])
            typesStack.append(variablesTable[funcID]['vars'][oper]['type'])
        elif oper in variablesTable[programID]['vars']:
            operandsStack.append(variablesTable[programID]['vars'][oper]['memoryPos'])
            typesStack.append(variablesTable[programID]['vars'][oper]['type'])
        else:
            print(f'Variable [ {oper} ] does not exist !!!')
            sys.exit()
    else:
        oper = p[-5]
        operand1 = operandsStack.pop()
        typesStack.pop()
        if(oper in variablesTable[funcID]['vars']):
            if 'size' in variablesTable[funcID]['vars'][oper]:
                newQuad = Quadruple('VER', operand1, constantsTable['int'][0]['memoryPos'], constantsTable['int'][variablesTable[funcID]['vars'][oper]['size']]['memoryPos'])
                quadruplesList.append(newQuad)
                quadsCont += 1

                pos = tMemory.malloc('pointer', 1)
                
                newQuad = Quadruple('+', operand1, constantsTable['int'][variablesTable[funcID]['vars'][oper]['memoryPos']]['memoryPos'], pos)
                quadruplesList.append(newQuad)
                quadsCont += 1

                operandsStack.append('*' + str(pos))
                typesStack.append(variablesTable[funcID]['vars'][oper]['type'])
            else:
                print(f"Variable [ {oper} ] is not an array !!!")
                sys.exit()
        elif(oper in variablesTable[programID]['vars']):
            if 'size' in variablesTable[programID]['vars'][oper]:
                newQuad = Quadruple('VER', operand1, constantsTable['int'][0]['memoryPos'], constantsTable['int'][variablesTable[programID]['vars'][oper]['size']]['memoryPos'])
                quadruplesList.append(newQuad)
                quadsCont += 1

                pos = tMemory.malloc('pointer', 1)
                
                newQuad = Quadruple('+', operand1, constantsTable['int'][variablesTable[programID]['vars'][oper]['memoryPos']]['memoryPos'], pos)
                quadruplesList.append(newQuad)
                quadsCont += 1

                operandsStack.append('*' + str(pos))
                typesStack.append(variablesTable[programID]['vars'][oper]['type'])
            else:
                print(f"Variable [ {oper} ] is not an array !!!")
                sys.exit()
        else:
            print(f'Variable [ {oper} ] does not exist !!!')
            sys.exit()
        addTemp('pointer')

# Add a constat such as a number, string, etc. to the constantsTable
def p_addConstantOperand(p):
    'addConstantOperand :'
    global operandsStack, typesStack

    oper = p[-1]
    if(isinstance(oper, int)):
        if(oper not in constantsTable['int']):
            pos = cMemory.malloc('int', 1)
            constantsTable['int'][oper] = {'type': 'int', 'memoryPos': pos}
        operandsStack.append(constantsTable['int'][oper]['memoryPos'])
        typesStack.append('int')
    elif(isinstance(oper, float)):
        if(oper not in constantsTable['float']):
            pos = cMemory.malloc('float', 1)
            constantsTable['float'][oper] = {'type': 'float', 'memoryPos': pos}
        operandsStack.append(constantsTable['float'][oper]['memoryPos'])
        typesStack.append('float')
    else:
        if(oper not in constantsTable['string']):
            pos = cMemory.malloc('string', 1)
            constantsTable['string'][oper] = {'type': 'string', 'memoryPos': pos}
        operandsStack.append(constantsTable['string'][oper]['memoryPos'])
        typesStack.append('string')

# Add bools to constant tables
def p_addConstantBool(p):
    'addConstantBool :'
    global operandsStack, typesStack

    oper = p[-1]
    if(oper not in constantsTable['bool']):
        pos = cMemory.malloc('bool', 1)
        constantsTable['bool'][oper] = {'type': 'bool', 'memoryPos': pos}
    operandsStack.append(constantsTable['bool'][oper]['memoryPos'])
    typesStack.append('bool')

# Whenever we read an operator add it to the operatorsStack
def p_addOperator(p):
    'addOperator :'
    global operatorStack

    op = p[-1]
    operatorStack.append(op)

# Add parenthesis or fake bottom as seen in class
def p_addParenthesis(p):
    'addParenthesis :'
    global operatorStack

    operatorStack.append('(')

# Remove parenthesis or fake bottom
def p_removeParenthesis(p):
    'removeParenthesis :'
    global operatorStack

    operatorStack.pop()

# Logic Expressions (&&, ||)
def p_doLogicExpression(p):
    'doLogicExpression :'
    global operandsStack, operatorStack, typesStack, quadruplesList, quadsCont

    if(len(operatorStack) != 0):
        aux = operatorStack[-1]
        if(aux == '&&' or aux == '||'):
            operator = operatorStack.pop()
            rightOperand = operandsStack.pop()
            leftOperand = operandsStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()

            if semanticCube[leftType][rightType][operator] == 'error':
                print(f'Cannot perform operation [ {operator} ] with: [ {leftType}] and [ {rightType} ] !!!')
                sys.exit()
            else:
                resType = semanticCube[leftType][rightType][operator]
                pos = tMemory.malloc(resType, 1)
                newQuad = Quadruple(operator, leftOperand, rightOperand, pos)
                quadruplesList.append(newQuad)
                operandsStack.append(pos)
                typesStack.append(semanticCube[leftType][rightType][operator])
                quadsCont += 1
                addTemp(resType)

# Expressions (<, <=, >, >=, !=, ==)
def p_doCompExpression(p):
    'doCompExpression :'
    global operandsStack, operatorStack, typesStack, quadruplesList, quadsCont

    if(len(operatorStack) != 0):
        aux = operatorStack[-1]
        if(aux == '<' or aux == '<=' or aux == '>' or aux == '>=' or aux == '!=' or aux =='=='):
            operator = operatorStack.pop()
            rightOperand = operandsStack.pop()
            leftOperand = operandsStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()

            if semanticCube[leftType][rightType][operator] == 'error':
                print(f'Cannot perform operation {operator} with: [ {leftType}] and [ {rightType} ] !!!')
                sys.exit()
            else:
                resType = semanticCube[leftType][rightType][operator]
                pos = tMemory.malloc(resType, 1)
                newQuad = Quadruple(operator, leftOperand, rightOperand, pos)
                quadruplesList.append(newQuad)
                operandsStack.append(pos)
                typesStack.append(semanticCube[leftType][rightType][operator])
                quadsCont += 1
                addTemp(resType)

# Expressions (SUMS and MINUS)
def p_doExpression(p):
    'doExpression :'
    global operandsStack, operatorStack, typesStack, quadruplesList, quadsCont

    if(len(operatorStack) != 0):
        aux = operatorStack[-1]
        if(aux == '+' or aux == '-'):
            operator = operatorStack.pop()
            rightOperand = operandsStack.pop()
            leftOperand = operandsStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()

            if semanticCube[leftType][rightType][operator] == 'error':
                print(f'Cannot perform operation [ {operator} ] with: [ {leftType}] and [ {rightType} ] !!!')
                sys.exit()
            else:
                resType = semanticCube[leftType][rightType][operator]
                pos = tMemory.malloc(resType, 1)
                newQuad = Quadruple(operator, leftOperand, rightOperand, pos)
                quadruplesList.append(newQuad)
                operandsStack.append(pos)
                typesStack.append(semanticCube[leftType][rightType][operator])
                quadsCont += 1
                addTemp(resType)

# Terms (TIMES, DIV, MOD, EXP)
def p_doTerm(p):
    'doTerm :'
    global operandsStack, operatorStack, typesStack, quadruplesList, quadsCont

    if(len(operatorStack) != 0):
        aux = operatorStack[-1]
        if(aux == '*' or aux == '/' or aux == '%' or aux == '^'):
            operator = operatorStack.pop()
            rightOperand = operandsStack.pop()
            leftOperand = operandsStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()

            if semanticCube[leftType][rightType][operator] == 'error':
                print(f'Cannot perform operation  [ {operator} ] with: [ {leftType}] and [ {rightType} ] !!!')
                sys.exit()
            else:
                resType = semanticCube[leftType][rightType][operator]
                pos = tMemory.malloc(resType, 1)
                newQuad = Quadruple(operator, leftOperand, rightOperand, pos)
                quadruplesList.append(newQuad)
                operandsStack.append(pos)
                typesStack.append(semanticCube[leftType][rightType][operator])
                quadsCont += 1
                addTemp(resType)

# Assignment (=)
def p_doAssign(p):
    'doAssign :'
    global operandsStack, operatorStack, typesStack, quadruplesList, quadsCont
    
    operator = operatorStack.pop()
    rightOperand = operandsStack.pop()
    leftOperand = operandsStack.pop()
    rightType = typesStack.pop()
    leftType = typesStack.pop()

    if leftType != rightType:
        print(f'Type mismatch: [ {leftType} ] with [ {rightType} ] !!!')
        sys.exit()
    else:
        newQuad = Quadruple(operator, rightOperand, None, leftOperand)
        quadruplesList.append(newQuad)
        quadsCont += 1

# Writting (print)
def p_doWrite(p):
    'doWrite :'
    global operandsStack, operatorStack, quadruplesList, typesStack, quadsCont

    operand = operandsStack.pop()
    typesStack.pop()
    newQuad = Quadruple('print', None, None, operand)
    quadruplesList.append(newQuad)
    quadsCont += 1

def p_doWriteString(p):
    'doWriteString :'
    global operandsStack, operatorStack, quadruplesList, typesStack, quadsCont

    operand = p[-1]
    newQuad = Quadruple('print', None, None, operand)
    quadruplesList.append(newQuad)
    quadsCont += 1

# Reading (listen)
def p_doReading(p):
    'doReading :'
    global operandsStack, operatorStack, quadruplesList, typesStack, quadsCont

    operand = operandsStack.pop()
    typesStack.pop()
    newQuad = Quadruple('listen', None, None, operand)
    quadruplesList.append(newQuad)
    quadsCont += 1

# Conditionals (IF)
# Afeter evaluating expression add GOTOF in case the expression was false and we need to skip the whole if
# append pending jump to jumpsStack
def p_doIF(p):
    'doIF :'
    global operandsStack, typesStack, jumpsStack, quadruplesList, quadsCont

    cond = operandsStack.pop()
    condType = typesStack.pop()
    if(condType != 'bool'):
        print('You need an expression that returns a bool(true/false) to use it in a conditional !!!')
        sys.exit()
    else:
        newQuad = Quadruple('GOTOF', cond, None, None)
        quadruplesList.append(newQuad)
        quadsCont += 1
        jumpsStack.append(quadsCont - 1)

# After reaching the end of the if, we need to fill missing parameter at jumpFalse
def p_endIF(p):
    'endIF :'
    global jumpsStackm, quadsCont

    jumpFalse = jumpsStack.pop()
    quadruplesList[jumpFalse].temp = quadsCont

# Conditionals (ELSE)
# Append quadruple GOTO and fill pending jump and add next quadruple to jumpsStack
def p_doElse(p):
    'doElse :'
    global jumpsStackm, quadsCont

    newQuad = Quadruple('GOTO', None, None, None)
    quadruplesList.append(newQuad)
    quadsCont += 1
    jump = jumpsStack.pop()
    jumpsStack.append(quadsCont - 1)
    quadruplesList[jump].temp = quadsCont

# Loops (WHILE)
# Add GOTOF quadruple since we need tu jump all the way
# over to the next quadruple after the while loop
def p_doWhile(p):
    'doWhile :'
    global operandsStack, typesStack, jumpsStack, quadruplesList, quadsCont

    cond = operandsStack.pop()
    condType = typesStack.pop()
    if(condType != 'bool'):
        print('You need an expression that returns a bool(true/false) to use it in a while loop !!!')
        sys.exit()
    else:
        newQuad = Quadruple('GOTOF', cond, None, None)
        quadruplesList.append(newQuad)
        quadsCont += 1
        jumpsStack.append(quadsCont - 1)

# Append GOTO quadruple to the start of the condition to re-evaluate and check if we need to enter
# or exit the looop
def p_endWhile(p):
    'endWhile :'
    global operandsStack, typesStack, jumpsStack, quadruplesList, quadsCont

    pendingJump = jumpsStack.pop()
    condStartJump = jumpsStack.pop()
    newQuad = Quadruple('GOTO', None, None, condStartJump)
    quadruplesList.append(newQuad)
    quadsCont += 1
    quadruplesList[pendingJump].temp = quadsCont

# We need to save where tu condition starts to re-evaluate the expression
def p_addCondStart(p):
    'addCondStart :'
    global jumpsStack

    jumpsStack.append(quadsCont)

# Function Call
# Whenever we call a function append ERA quad of said function since we
# need to know what memory to load
def p_doFunCall(p):
    'doFuncCall :'
    global contParams, operatorStack, auxFunc, quadruplesList, quadsCont

    auxFunc = p[-1]

    if(auxFunc in variablesTable):
        contParams = 0
        operatorStack.append('(')
        newQuad = Quadruple('ERA', None, None, auxFunc)
        quadruplesList.append(newQuad)
        quadsCont += 1
    else:
        print(f'Function [ {auxFunc} ] is not declared !!!')
        sys.exit()

def p_setVoidType(p):
    'setVoidType :'
    variablesTable[funcID]['type'] = ''

# If the total amount of params (contParams) is different to what we have that the funciton
# need inside the variablesTable, we need to let the user know he's missing some paramters
def p_checkParams(p):
    'checkParams :'
    global variablesTable, contParams
    if(len(variablesTable[auxFunc]['params']) != contParams):
        print(f"Function [ {auxFunc} ] expected [ {len(variablesTable[auxFunc]['params'])} ] and got [ {contParams} ] instead !!!")
        sys.exit()
    contParams = 0

# Check if parameters type corresponds to the ones that are expected for the function
def p_checkType(p):
    'checkType :'
    global contParams, typesStack, operandsStack, quadruplesList, quadsCont

    if(contParams in variablesTable[auxFunc]['params']):
        paramType = typesStack.pop()
        if(paramType == variablesTable[auxFunc]['params'][contParams]):
            operand = operandsStack.pop()
            newQuad = Quadruple('PARAM', operand, None, 'PAR ' + str(contParams))
            quadruplesList.append(newQuad)
            quadsCont += 1
        else:
            print(f"Function [ {auxFunc} ] expects [ {variablesTable[auxFunc]['params'][contParams] } ] as #{ contParams + 1} argument !!!")
            sys.exit()
    contParams += 1

# Append quadruple RET that will let know the virtual machine which memory address to access
# in order to retrieve actual value of return
def p_doReturn(p):
    'doReturn :'
    global flagReturn, quadruplesList, operandsStack, typesStack, quadsCont
    flagReturn = True
    oper = operandsStack.pop()
    operType = typesStack.pop()

    if operType != variablesTable[funcID]['type']:
        print(f"Function [ {funcID} ] expects [ {variablesTable[funcID]['type']} ] as return type !!!")
        sys.exit()
    else:
        newQuad = Quadruple('RET', None, None, oper)
        quadruplesList.append(newQuad)
        quadsCont += 1

# Append GOSUB quadruple with the pointer to the quadruplesList where the called function starts
def p_doGoSub(p):
    'doGoSub :'
    global operatorStack, quadruplesList, quadsCont, auxFunc, operandsStack
    operatorStack.pop()
    newQuad = Quadruple('GOSUB', None, None, variablesTable[auxFunc]['start'])
    quadruplesList.append(newQuad)
    quadsCont += 1
    if(variablesTable[auxFunc]['type'] != ''):
        pos = variablesTable[programID]['vars'][auxFunc]['memoryPos']
        temp = tMemory.malloc(variablesTable[auxFunc]['type'], 1)
        newQuad = Quadruple('=', pos, None, temp)
        quadruplesList.append(newQuad)
        quadsCont += 1

        operandsStack.append(temp)
        typesStack.append(variablesTable[auxFunc]['type'])
        addTemp(variablesTable[auxFunc]['type'])

    auxFunc = ''

# Append GOSUB but insted of adding a number, we need to know which special function is being called
# since all of therm are already at the beggining with start 0
def p_doGoSubS(p):
    'doGoSubS :'
    global operatorStack, quadruplesList, quadsCont, auxFunc, operandsStack
    operatorStack.pop()
    newQuad = Quadruple('GOSUB', None, None, auxFunc)
    quadruplesList.append(newQuad)
    quadsCont += 1
    if(variablesTable[auxFunc]['type'] != ''):
        pos = variablesTable[programID]['vars'][auxFunc]['memoryPos']
        temp = tMemory.malloc(variablesTable[auxFunc]['type'], 1)
        newQuad = Quadruple('=', pos, None, temp)
        quadruplesList.append(newQuad)
        quadsCont += 1

        operandsStack.append(temp)
        typesStack.append(variablesTable[auxFunc]['type'])
        addTemp(variablesTable[auxFunc]['type'])
    
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

# Send all important info to class virtual machine to start loading memory
vm = virtualMachine(programID, quadruplesList, variablesTable, constantsTable, auxTemps)
vm.loadMemory(gMemory, lMemory, cMemory, tMemory)

# Start to execute quadruplesList
vm.exec()