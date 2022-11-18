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

variablesTable = {}
auxVars = [0, 0, 0, 0]
auxTemps = [0, 0, 0, 0, 0]
constantsTable = {'int': {}, 'float': {}, 'bool': {}, 'string': {}}

# Semantic Cube
# Using a nested dictionary to create a relationship ALL to ALL and allow to reconize type mismatch errors
semanticCube = Cube().CUBE

#Quadruple's Stacks
operatorStack = deque()
operandsStack = deque()
typesStack = deque()
jumpsStack = deque()

quadruplesList = []
quadsCont = 0
tempsCont = 1

funcID = ''
programID = ''
varID = ''
varType = ''
currType = ''

#====== PARSER ======#
# Main function variables and functions Rules
def p_mainFunction(p):
    '''
    program_main : BTSProgam CTE_ID startup SEMI_COLON globalVariables globalFunctions MAIN saveFuncID addMemoryInfo LEFT_PAREN RIGHT_PAREN setMain funcBody endFunction endProgram endPrint
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
    funcs_aux : FUNC type CTE_ID saveFuncID LEFT_PAREN RIGHT_PAREN funcBody addMemoryInfo endFunction
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

# def p_auxFuncBody(p):
#     '''
#     auxFuncBody : statements auxFuncBody
#                 | empty
#     '''

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
               | writting
               | if
               | while
               | for
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
# def p_reading(p):
#     '''
#     reading : READ_INPUT addOperator LEFT_PAREN CTE_ID addOperand doReading RIGHT_PAREN SEMI_COLON
#     '''

# Assing Rules
def p_assignment(p):
    '''
    assignment : CTE_ID addOperand EQUAL addOperator logicExpression doAssign SEMI_COLON
    '''

# Expressions Rules
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
              | CTE_INT addConstantOperand
              | CTE_FLOAT addConstantOperand
              | CTE_STRING addConstantOperand
              | TRUE addConstantBool
              | FALSE addConstantBool
    '''

# Conditional Rules
def p_if(p):
    '''
    if : IF LEFT_PAREN logicExpression doIF RIGHT_PAREN funcBody else endIF
    '''

def p_else(p):
    '''
    else : ELSE doElse IF LEFT_PAREN logicExpression doIF RIGHT_PAREN funcBody endIF
         | ELSE doElse funcBody
         | empty
    '''

def p_while(p):
    '''
    while : WHILE LEFT_PAREN addCondStart logicExpression doWhile RIGHT_PAREN funcBody endWhile
    '''

def p_for(p):
    '''
    for : FOR LEFT_PAREN CTE_ID COMMA auxFor COMMA auxFor RIGHT_PAREN funcBody
    '''

def p_auxFor(p):
    '''
    auxFor : CTE_ID 
           | CTE_INT
    '''

# Read Rules
#def p_reading(p):
   # '''
   # reading : READ_INPUT LEFT_PAREN RIGHT_PAREN SEMI_COLON
   # '''
#==== AUX FUNCS ====#
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
    else:
        print("ERROR")
        sys.exit()

#==== POINTS ====#
def p_startup(p):
    'startup :'
    global funcID, programID, quadsCont

    programID = p[-1]
    funcID = programID
    variablesTable[programID] = {'type' : 'void', 'vars' : {}, 'start' : quadsCont, 'numVars' : [], 'numTemps' : []}
    newQuad = Quadruple('GOTO', None, None, 'mainStage')
    quadruplesList.append(newQuad)
    quadsCont += 1

def p_setMain(p):
    'setMain :'
    global quadruplesList, funcID

    quadruplesList[0].temp = quadsCont

def p_endProgram(p):
    'endProgram :'
    global quadruplesList

    newQuad = Quadruple('END', None, None, None)
    quadruplesList.append(newQuad)

def p_endPrint(p):
    'endPrint :'
    cont = 0
    for key, value in variablesTable.items():
        print(key, ' : ', value)

    for x in quadruplesList:
        print(cont, x)
        cont += 1

    print(constantsTable)
    print(lMemory)

    print(f"OPERATOR STACK = {operatorStack}")
    print(f"OPERAND STACK = {operandsStack}")
    print(f"TYPE STACK = {typesStack}")
    print(f"JUMPS STACK = {jumpsStack}")

def p_saveFuncID(p):
    'saveFuncID :'
    global funcID, currType, auxVars, auxTemps

    auxVars = [0 , 0, 0, 0]
    auxTemps = [0, 0, 0, 0, 0]
    funcID = p[-1]
    if(funcID not in variablesTable):
        variablesTable[funcID] = {'type': currType, 'vars': {}, 'start' : quadsCont, 'numVars' : [0, 0, 0, 0], 'numTemps' : [0, 0, 0, 0, 0]}
    else:
        print(f'Function \'{funcID}\' has already been declared!')
        sys.exit()

    #print(funcID, currType)

def p_addMemoryInfo(p):
    'addMemoryInfo :'
    global variablesTable

    variablesTable[funcID]['numVars'] = auxVars

def p_endFunction(p):
    'endFunction :'
    global quadruplesList, variablesTable, quadsCont

    if(funcID != 'mainStage'):
        newQuad = Quadruple('ENDPROC', None, None, None)
        quadruplesList.append(newQuad)
        quadsCont += 1
    variablesTable[funcID]['numTemps'] = auxTemps

# Conditionals (IF)
def p_doIF(p):
    'doIF :'
    global operandsStack, typesStack, jumpsStack, quadruplesList, quadsCont

    cond = operandsStack.pop()
    condType = typesStack.pop()
    if(condType != 'bool'):
        print('You need an expression that returns a bool(true/false) to use it in a conditional! :(')
    else:
        newQuad = Quadruple('GOTOF', cond, None, None)
        quadruplesList.append(newQuad)
        quadsCont = quadsCont + 1
        jumpsStack.append(quadsCont - 1)

def p_endIF(p):
    'endIF :'
    global jumpsStackm, quadsCont

    jumpFalse = jumpsStack.pop()
    quadruplesList[jumpFalse].temp = quadsCont

# Conditionals (ELSE)
def p_doElse(p):
    'doElse :'
    global jumpsStackm, quadsCont

    newQuad = Quadruple('GOTO', None, None, None)
    quadruplesList.append(newQuad)
    quadsCont = quadsCont + 1
    jump = jumpsStack.pop()
    jumpsStack.append(quadsCont - 1)
    quadruplesList[jump].temp = quadsCont

# Loops (WHILE)
def p_doWhile(p):
    'doWhile :'
    global operandsStack, typesStack, jumpsStack, quadruplesList, quadsCont

    cond = operandsStack.pop()
    condType = typesStack.pop()
    if(condType != 'bool'):
        print('You need an expression that returns a bool(true/false) to use it in a while loop! :(')
    else:
        newQuad = Quadruple('GOTOF', cond, None, None)
        quadruplesList.append(newQuad)
        quadsCont = quadsCont + 1
        jumpsStack.append(quadsCont - 1)

def p_endWhile(p):
    'endWhile :'
    global operandsStack, typesStack, jumpsStack, quadruplesList, quadsCont

    pendingJump = jumpsStack.pop()
    condStartJump = jumpsStack.pop()
    newQuad = Quadruple('GOTO', None, None, condStartJump)
    quadruplesList.append(newQuad)
    quadsCont = quadsCont + 1
    quadruplesList[pendingJump].temp = quadsCont

def p_addCondStart(p):
    'addCondStart :'
    global jumpsStack

    jumpsStack.append(quadsCont)

def p_saveVariableID(p):
    'saveVariableID :'
    global varID, currType, auxMemory

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
        print(f'Variable \'{varID}\' has already been declared!')
        sys.exit()

    #print(f'Variable id = {p[-1]}')

def p_setCurrentType(p):
    'setCurrentType :'
    global currType

    currType = p[-1]

def p_addOperand(p):
    'addOperand :'
    global operandsStack, typesStack, auxVars, auxTemps

    oper = p[-1]
    if oper in variablesTable[funcID]['vars']:
        operandsStack.append(variablesTable[funcID]['vars'][oper]['memoryPos'])
        typesStack.append(variablesTable[funcID]['vars'][oper]['type'])
    elif oper in variablesTable[programID]['vars']:
        operandsStack.append(variablesTable[programID]['vars'][oper]['memoryPos'])
        typesStack.append(variablesTable[programID]['vars'][oper]['type'])
    else:
        print(f'Variable \'{oper}\' does not exist :(')
        sys.exit()

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

def p_addConstantBool(p):
    'addConstantBool :'
    global operandsStack, typesStack

    oper = p[-1]
    if(oper not in constantsTable['bool']):
        pos = cMemory.malloc('bool', 1)
        constantsTable['bool'][oper] = {'type': 'bool', 'memoryPos': pos}
    operandsStack.append(constantsTable['bool'][oper]['memoryPos'])
    typesStack.append('bool')

def p_addOperator(p):
    'addOperator :'
    global operatorStack

    op = p[-1]
    operatorStack.append(op)

def p_addParenthesis(p):
    'addParenthesis :'
    global operatorStack

    operatorStack.append('(')

def p_removeParenthesis(p):
    'removeParenthesis :'
    global operatorStack

    operatorStack.pop()

# Logic Expressions
def p_doLogicExpression(p):
    'doLogicExpression :'
    global operandsStack, operatorStack, typesStack, quadruplesList, quadsCont, tempsCont

    if(len(operatorStack) != 0):
        aux = operatorStack[-1]
        if(aux == '&&' or aux == '||'):
            operator = operatorStack.pop()
            rightOperand = operandsStack.pop()
            leftOperand = operandsStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()

            if semanticCube[leftType][rightType][operator] == 'error':
                print('ERROR')
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
    global operandsStack, operatorStack, typesStack, quadruplesList, quadsCont, tempsCont

    if(len(operatorStack) != 0):
        aux = operatorStack[-1]
        if(aux == '<' or aux == '<=' or aux == '>' or aux == '>=' or aux == '!=' or aux =='=='):
            operator = operatorStack.pop()
            rightOperand = operandsStack.pop()
            leftOperand = operandsStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()

            if semanticCube[leftType][rightType][operator] == 'error':
                print('ERROR')
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
    global operandsStack, operatorStack, typesStack, quadruplesList, quadsCont, tempsCont

    if(len(operatorStack) != 0):
        aux = operatorStack[-1]
        if(aux == '+' or aux == '-'):
            operator = operatorStack.pop()
            rightOperand = operandsStack.pop()
            leftOperand = operandsStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()

            if semanticCube[leftType][rightType][operator] == 'error':
                print('ERROR')
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
    global operandsStack, operatorStack, typesStack, quadruplesList, quadsCont, tempsCont

    if(len(operatorStack) != 0):
        aux = operatorStack[-1]
        if(aux == '*' or aux == '/' or aux == '%' or aux == '^'):
            operator = operatorStack.pop()
            rightOperand = operandsStack.pop()
            leftOperand = operandsStack.pop()
            rightType = typesStack.pop()
            leftType = typesStack.pop()

            if semanticCube[leftType][rightType][operator] == 'error':
                print('ERROR')
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

# Assignment
def p_doAssign(p):
    'doAssign :'
    global operandsStack, operatorStack, typesStack, quadruplesList, quadsCont
    
    operator = operatorStack.pop()
    rightOperand = operandsStack.pop()
    leftOperand = operandsStack.pop()
    rightType = typesStack.pop()
    leftType = typesStack.pop()

    if leftType != rightType:
        print(f'Type missmatch: {rightOperand} with {leftOperand}')
        sys.exit()
    else:
        newQuad = Quadruple(operator, rightOperand, None, leftOperand)
        quadruplesList.append(newQuad)
        quadsCont += 1

# Writting
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

# Reading
# def p_doReading(p):
#     'doReading :'
#     global operandsStack, operatorStack, quadruplesList, typesStack

#     operator = operatorStack.pop()
#     opera

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

vm = virtualMachine(programID, quadruplesList, variablesTable, constantsTable, auxTemps)
vm.loadMemory(cMemory, tMemory, gMemory, lMemory)

vm.exec()