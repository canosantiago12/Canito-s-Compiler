
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BINOMIAL BOOL BTSProgam COMMA CTE_BOOL CTE_FLOAT CTE_ID CTE_INT CTE_STRING DIV ELSE EQUAL EQUALS EXP FALSE FLOAT FOR FUNC GREATER_EQUAL_THAN GREATER_THAN IF INT LEFT_BRACKET LEFT_CURLY_BRACKET LEFT_PAREN LESS_EQUAL_THAN LESS_THAN MAIN MEAN MEDIAN MINUS MOD MODE NOT_EQUALS OR PLOT PLUS POISSON PRINT READ_INPUT RETURN RIGHT_BRACKET RIGHT_CURLY_BRACKET RIGHT_PAREN SEMI_COLON STANDARD_DEVIATION STRING TIMES TRUE VAR VARIANCE VOID WHILE\n    program_main : BTSProgam CTE_ID startup SEMI_COLON globalVariables globalFunctions MAIN saveFuncID addMemoryInfo LEFT_PAREN RIGHT_PAREN setMain funcBody endFunction endProgram endPrint\n    \n    globalVariables : vars\n                    | empty\n    \n    globalFunctions : funcs\n                    | empty\n    \n    vars : auxVars\n    \n    auxVars : VAR type vars_type_single\n            | VAR type vars_type_array\n            | VAR type vars_type_matrix\n            | empty\n    \n    vars_type_single : CTE_ID saveVariableID COMMA vars_type_single\n                     | CTE_ID saveVariableID SEMI_COLON auxVars\n    \n    vars_type_array : CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_array\n                    | CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON auxVars\n    \n    vars_type_matrix : CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_matrix\n                     | CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON auxVars\n    \n    funcs : funcs_aux globalFunctions\n    \n    funcs_aux : FUNC type CTE_ID saveFuncID LEFT_PAREN RIGHT_PAREN funcBody addMemoryInfo endFunction\n    \n    funcBody : LEFT_CURLY_BRACKET auxFuncBody RIGHT_CURLY_BRACKET\n    \n    auxFuncBody : vars statements auxFuncBody\n                | statements auxFuncBody\n                | empty\n    \n    type : INT setCurrentType\n         | FLOAT setCurrentType\n         | BOOL setCurrentType\n         | STRING setCurrentType\n    \n    statements : assignment\n               | writting\n               | if\n               | while\n               | for\n    \n    writting : PRINT LEFT_PAREN auxWritting RIGHT_PAREN SEMI_COLON\n    \n    auxWritting : logicExpression doWrite multipleWrite\n                | CTE_STRING doWriteString multipleWrite\n    \n    multipleWrite : COMMA auxWritting\n                  | empty\n    \n    assignment : CTE_ID addOperand EQUAL addOperator logicExpression doAssign SEMI_COLON\n    \n    logicExpression : exp doLogicExpression auxLogicExpression\n    \n    auxLogicExpression : AND addOperator logicExpression\n                       | OR addOperator logicExpression\n                       | empty\n    \n    exp : exp2 doCompExpression auxExp\n    \n    auxExp : GREATER_THAN addOperator exp\n           | GREATER_EQUAL_THAN addOperator exp\n           | LESS_THAN addOperator exp\n           | LESS_EQUAL_THAN addOperator exp\n           | NOT_EQUALS addOperator exp\n           | EQUALS addOperator exp\n           | empty\n    \n    exp2 : term doExpression exp2Aux\n    \n    exp2Aux : PLUS addOperator exp2\n            | MINUS addOperator exp2\n            | empty\n    \n    term : factor doTerm auxTerm\n    \n    auxTerm : TIMES addOperator term\n            | DIV addOperator term\n            | MOD addOperator term\n            | EXP addOperator term\n            | empty\n    \n    factor : LEFT_PAREN addParenthesis logicExpression RIGHT_PAREN removeParenthesis\n           | constants\n    \n    constants : CTE_ID addOperand\n              | CTE_INT addConstantOperand\n              | CTE_FLOAT addConstantOperand\n              | CTE_STRING addConstantOperand\n              | TRUE addConstantBool\n              | FALSE addConstantBool\n    \n    if : IF LEFT_PAREN logicExpression doIF RIGHT_PAREN funcBody else endIF\n    \n    else : ELSE doElse IF LEFT_PAREN logicExpression doIF RIGHT_PAREN funcBody endIF\n         | ELSE doElse funcBody\n         | empty\n    \n    while : WHILE LEFT_PAREN addCondStart logicExpression doWhile RIGHT_PAREN funcBody endWhile\n    \n    for : FOR LEFT_PAREN CTE_ID COMMA auxFor COMMA auxFor RIGHT_PAREN funcBody\n    \n    auxFor : CTE_ID \n           | CTE_INT\n    startup :setMain :endProgram :endPrint :saveFuncID :addMemoryInfo :endFunction :doIF :endIF :doElse :doWhile :endWhile :addCondStart :saveVariableID :setCurrentType :addOperand :addConstantOperand :addConstantBool :addOperator :addParenthesis :removeParenthesis :doLogicExpression :doCompExpression :doExpression :doTerm :doAssign :doWrite :doWriteString :empty :'
    
_lr_action_items = {'BTSProgam':([0,],[2,]),'$end':([1,57,77,79,89,113,],[0,-82,-78,-19,-79,-1,]),'CTE_ID':([2,9,16,17,18,19,20,23,24,25,26,28,29,30,31,37,38,43,44,45,53,55,56,60,61,62,63,64,65,66,67,75,76,79,80,83,84,85,86,91,92,108,110,111,114,115,131,133,134,138,140,144,145,148,149,150,151,152,153,156,157,160,161,162,163,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,191,193,209,211,212,215,217,221,222,223,227,228,],[3,-6,27,-90,-90,-90,-90,33,-7,-8,-9,-23,-24,-25,-26,42,-104,-11,-12,-10,68,74,-104,68,68,-10,-27,-28,-29,-30,-31,-13,-14,-19,68,101,101,-88,109,-94,-95,101,132,-104,101,101,167,-15,-16,-32,101,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,101,101,101,101,101,101,101,101,101,101,101,101,101,101,-104,167,-37,-84,-71,-87,-68,-72,-70,-73,101,-84,-69,]),'SEMI_COLON':([3,4,27,34,42,49,50,87,96,97,98,99,100,101,102,103,104,105,107,116,119,120,121,122,123,124,125,126,127,128,136,143,146,147,154,155,158,159,164,171,172,173,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,],[-76,5,-89,38,-89,38,56,111,-97,-98,-99,-100,-61,-91,-92,-92,-93,-93,-92,138,-65,-104,-104,-104,-104,-62,-63,-64,-66,-67,-101,-38,-41,-42,-49,-50,-53,-54,-59,56,193,-96,-60,-39,-40,-43,-44,-45,-46,-47,-48,-51,-52,-55,-56,-57,-58,]),'FUNC':([5,6,7,8,9,14,24,25,26,38,43,44,45,52,56,58,75,76,78,79,111,133,134,],[-104,15,-2,-3,-6,15,-7,-8,-9,-104,-11,-12,-10,-81,-104,-82,-13,-14,-18,-19,-104,-15,-16,]),'MAIN':([5,6,7,8,9,11,12,13,14,22,24,25,26,38,43,44,45,52,56,58,75,76,78,79,111,133,134,],[-104,-104,-2,-3,-6,21,-4,-5,-104,-17,-7,-8,-9,-104,-11,-12,-10,-81,-104,-82,-13,-14,-18,-19,-104,-15,-16,]),'VAR':([5,38,53,56,61,63,64,65,66,67,79,80,111,138,189,193,209,211,212,215,217,221,222,227,228,],[10,10,10,10,10,-27,-28,-29,-30,-31,-19,10,10,-32,-104,-37,-84,-71,-87,-68,-72,-70,-73,-84,-69,]),'PRINT':([9,24,25,26,38,43,44,45,53,56,60,61,62,63,64,65,66,67,75,76,79,80,111,133,134,138,189,193,209,211,212,215,217,221,222,227,228,],[-6,-7,-8,-9,-104,-11,-12,-10,69,-104,69,69,-10,-27,-28,-29,-30,-31,-13,-14,-19,69,-104,-15,-16,-32,-104,-37,-84,-71,-87,-68,-72,-70,-73,-84,-69,]),'IF':([9,24,25,26,38,43,44,45,53,56,60,61,62,63,64,65,66,67,75,76,79,80,111,133,134,138,189,193,209,210,211,212,215,216,217,221,222,227,228,],[-6,-7,-8,-9,-104,-11,-12,-10,70,-104,70,70,-10,-27,-28,-29,-30,-31,-13,-14,-19,70,-104,-15,-16,-32,-104,-37,-84,-85,-71,-87,-68,220,-72,-70,-73,-84,-69,]),'WHILE':([9,24,25,26,38,43,44,45,53,56,60,61,62,63,64,65,66,67,75,76,79,80,111,133,134,138,189,193,209,211,212,215,217,221,222,227,228,],[-6,-7,-8,-9,-104,-11,-12,-10,71,-104,71,71,-10,-27,-28,-29,-30,-31,-13,-14,-19,71,-104,-15,-16,-32,-104,-37,-84,-71,-87,-68,-72,-70,-73,-84,-69,]),'FOR':([9,24,25,26,38,43,44,45,53,56,60,61,62,63,64,65,66,67,75,76,79,80,111,133,134,138,189,193,209,211,212,215,217,221,222,227,228,],[-6,-7,-8,-9,-104,-11,-12,-10,72,-104,72,72,-10,-27,-28,-29,-30,-31,-13,-14,-19,72,-104,-15,-16,-32,-104,-37,-84,-71,-87,-68,-72,-70,-73,-84,-69,]),'INT':([10,15,],[17,17,]),'FLOAT':([10,15,],[18,18,]),'BOOL':([10,15,],[19,19,]),'STRING':([10,15,],[20,20,]),'LEFT_PAREN':([21,32,33,35,36,69,70,71,72,83,84,85,91,92,108,114,115,140,144,145,148,149,150,151,152,153,156,157,160,161,162,163,175,176,177,178,179,180,181,182,183,184,185,186,187,188,220,223,],[-80,-81,-80,40,41,83,84,85,86,92,92,-88,-94,-95,92,92,92,92,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,92,92,92,92,92,92,92,92,92,92,92,92,92,92,223,92,]),'COMMA':([27,34,42,49,50,87,94,95,96,97,98,99,100,101,102,103,104,105,107,109,117,118,119,120,121,122,123,124,125,126,127,128,143,146,147,154,155,158,159,164,167,168,169,171,173,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,],[-89,37,-89,37,55,110,-102,-92,-97,-98,-99,-100,-61,-91,-92,-92,-93,-93,-92,131,140,140,-65,-104,-104,-104,-104,-62,-63,-64,-66,-67,-38,-41,-42,-49,-50,-53,-54,-59,-74,191,-75,55,-96,-60,-39,-40,-43,-44,-45,-46,-47,-48,-51,-52,-55,-56,-57,-58,]),'LEFT_BRACKET':([27,34,50,74,88,132,170,219,],[-89,39,54,-89,112,-89,192,54,]),'CTE_INT':([39,54,83,84,85,91,92,108,112,114,115,131,140,144,145,148,149,150,151,152,153,156,157,160,161,162,163,175,176,177,178,179,180,181,182,183,184,185,186,187,188,191,192,223,],[46,73,102,102,-88,-94,-95,102,135,102,102,169,102,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,102,102,102,102,102,102,102,102,102,102,102,102,102,102,169,214,102,]),'RIGHT_PAREN':([40,41,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,117,118,119,120,121,122,123,124,125,126,127,128,129,130,137,139,141,142,143,146,147,154,155,158,159,164,166,167,169,173,174,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,213,224,225,],[47,48,116,-102,-92,-97,-98,-99,-100,-61,-91,-92,-92,-93,-93,-83,-92,-104,-104,-65,-104,-104,-104,-104,-62,-63,-64,-66,-67,165,-86,173,-33,-36,-34,-38,-41,-42,-49,-50,-53,-54,-59,190,-74,-75,-96,-35,-60,-39,-40,-43,-44,-45,-46,-47,-48,-51,-52,-55,-56,-57,-58,218,-83,226,]),'RIGHT_BRACKET':([46,73,135,214,],[50,87,171,219,]),'LEFT_CURLY_BRACKET':([47,48,51,165,190,210,216,218,226,],[-77,53,53,53,53,-85,53,53,53,]),'RIGHT_CURLY_BRACKET':([53,59,61,62,63,64,65,66,67,79,80,81,90,138,189,193,209,211,212,215,217,221,222,227,228,],[-104,79,-104,-22,-27,-28,-29,-30,-31,-19,-104,-21,-20,-32,-104,-37,-84,-71,-87,-68,-72,-70,-73,-84,-69,]),'EQUAL':([68,82,],[-91,91,]),'ELSE':([79,189,],[-19,210,]),'CTE_STRING':([83,84,85,91,92,108,114,115,140,144,145,148,149,150,151,152,153,156,157,160,161,162,163,175,176,177,178,179,180,181,182,183,184,185,186,187,188,223,],[95,107,-88,-94,-95,107,107,107,95,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,107,107,107,107,107,107,107,107,107,107,107,107,107,107,107,]),'CTE_FLOAT':([83,84,85,91,92,108,114,115,140,144,145,148,149,150,151,152,153,156,157,160,161,162,163,175,176,177,178,179,180,181,182,183,184,185,186,187,188,223,],[103,103,-88,-94,-95,103,103,103,103,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,103,103,103,103,103,103,103,103,103,103,103,103,103,103,103,]),'TRUE':([83,84,85,91,92,108,114,115,140,144,145,148,149,150,151,152,153,156,157,160,161,162,163,175,176,177,178,179,180,181,182,183,184,185,186,187,188,223,],[104,104,-88,-94,-95,104,104,104,104,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,104,104,104,104,104,104,104,104,104,104,104,104,104,104,104,]),'FALSE':([83,84,85,91,92,108,114,115,140,144,145,148,149,150,151,152,153,156,157,160,161,162,163,175,176,177,178,179,180,181,182,183,184,185,186,187,188,223,],[105,105,-88,-94,-95,105,105,105,105,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,-94,105,105,105,105,105,105,105,105,105,105,105,105,105,105,105,]),'TIMES':([95,99,100,101,102,103,104,105,107,119,123,124,125,126,127,128,173,194,],[-92,-100,-61,-91,-92,-92,-93,-93,-92,-65,160,-62,-63,-64,-66,-67,-96,-60,]),'DIV':([95,99,100,101,102,103,104,105,107,119,123,124,125,126,127,128,173,194,],[-92,-100,-61,-91,-92,-92,-93,-93,-92,-65,161,-62,-63,-64,-66,-67,-96,-60,]),'MOD':([95,99,100,101,102,103,104,105,107,119,123,124,125,126,127,128,173,194,],[-92,-100,-61,-91,-92,-92,-93,-93,-92,-65,162,-62,-63,-64,-66,-67,-96,-60,]),'EXP':([95,99,100,101,102,103,104,105,107,119,123,124,125,126,127,128,173,194,],[-92,-100,-61,-91,-92,-92,-93,-93,-92,-65,163,-62,-63,-64,-66,-67,-96,-60,]),'PLUS':([95,98,99,100,101,102,103,104,105,107,119,122,123,124,125,126,127,128,159,164,173,194,205,206,207,208,],[-92,-99,-100,-61,-91,-92,-92,-93,-93,-92,-65,156,-104,-62,-63,-64,-66,-67,-54,-59,-96,-60,-55,-56,-57,-58,]),'MINUS':([95,98,99,100,101,102,103,104,105,107,119,122,123,124,125,126,127,128,159,164,173,194,205,206,207,208,],[-92,-99,-100,-61,-91,-92,-92,-93,-93,-92,-65,157,-104,-62,-63,-64,-66,-67,-54,-59,-96,-60,-55,-56,-57,-58,]),'GREATER_THAN':([95,97,98,99,100,101,102,103,104,105,107,119,121,122,123,124,125,126,127,128,155,158,159,164,173,194,203,204,205,206,207,208,],[-92,-98,-99,-100,-61,-91,-92,-92,-93,-93,-92,-65,148,-104,-104,-62,-63,-64,-66,-67,-50,-53,-54,-59,-96,-60,-51,-52,-55,-56,-57,-58,]),'GREATER_EQUAL_THAN':([95,97,98,99,100,101,102,103,104,105,107,119,121,122,123,124,125,126,127,128,155,158,159,164,173,194,203,204,205,206,207,208,],[-92,-98,-99,-100,-61,-91,-92,-92,-93,-93,-92,-65,149,-104,-104,-62,-63,-64,-66,-67,-50,-53,-54,-59,-96,-60,-51,-52,-55,-56,-57,-58,]),'LESS_THAN':([95,97,98,99,100,101,102,103,104,105,107,119,121,122,123,124,125,126,127,128,155,158,159,164,173,194,203,204,205,206,207,208,],[-92,-98,-99,-100,-61,-91,-92,-92,-93,-93,-92,-65,150,-104,-104,-62,-63,-64,-66,-67,-50,-53,-54,-59,-96,-60,-51,-52,-55,-56,-57,-58,]),'LESS_EQUAL_THAN':([95,97,98,99,100,101,102,103,104,105,107,119,121,122,123,124,125,126,127,128,155,158,159,164,173,194,203,204,205,206,207,208,],[-92,-98,-99,-100,-61,-91,-92,-92,-93,-93,-92,-65,151,-104,-104,-62,-63,-64,-66,-67,-50,-53,-54,-59,-96,-60,-51,-52,-55,-56,-57,-58,]),'NOT_EQUALS':([95,97,98,99,100,101,102,103,104,105,107,119,121,122,123,124,125,126,127,128,155,158,159,164,173,194,203,204,205,206,207,208,],[-92,-98,-99,-100,-61,-91,-92,-92,-93,-93,-92,-65,152,-104,-104,-62,-63,-64,-66,-67,-50,-53,-54,-59,-96,-60,-51,-52,-55,-56,-57,-58,]),'EQUALS':([95,97,98,99,100,101,102,103,104,105,107,119,121,122,123,124,125,126,127,128,155,158,159,164,173,194,203,204,205,206,207,208,],[-92,-98,-99,-100,-61,-91,-92,-92,-93,-93,-92,-65,153,-104,-104,-62,-63,-64,-66,-67,-50,-53,-54,-59,-96,-60,-51,-52,-55,-56,-57,-58,]),'AND':([95,96,97,98,99,100,101,102,103,104,105,107,119,120,121,122,123,124,125,126,127,128,147,154,155,158,159,164,173,194,197,198,199,200,201,202,203,204,205,206,207,208,],[-92,-97,-98,-99,-100,-61,-91,-92,-92,-93,-93,-92,-65,144,-104,-104,-104,-62,-63,-64,-66,-67,-42,-49,-50,-53,-54,-59,-96,-60,-43,-44,-45,-46,-47,-48,-51,-52,-55,-56,-57,-58,]),'OR':([95,96,97,98,99,100,101,102,103,104,105,107,119,120,121,122,123,124,125,126,127,128,147,154,155,158,159,164,173,194,197,198,199,200,201,202,203,204,205,206,207,208,],[-92,-97,-98,-99,-100,-61,-91,-92,-92,-93,-93,-92,-65,145,-104,-104,-104,-62,-63,-64,-66,-67,-42,-49,-50,-53,-54,-59,-96,-60,-43,-44,-45,-46,-47,-48,-51,-52,-55,-56,-57,-58,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program_main':([0,],[1,]),'startup':([3,],[4,]),'globalVariables':([5,],[6,]),'vars':([5,53,61,80,],[7,60,60,60,]),'empty':([5,6,14,38,53,56,61,80,111,117,118,120,121,122,123,189,],[8,13,13,45,62,45,62,62,45,141,141,146,154,158,164,211,]),'auxVars':([5,38,53,56,61,80,111,],[9,44,9,76,9,9,134,]),'globalFunctions':([6,14,],[11,22,]),'funcs':([6,14,],[12,12,]),'funcs_aux':([6,14,],[14,14,]),'type':([10,15,],[16,23,]),'vars_type_single':([16,37,],[24,43,]),'vars_type_array':([16,55,],[25,75,]),'vars_type_matrix':([16,110,],[26,133,]),'setCurrentType':([17,18,19,20,],[28,29,30,31,]),'saveFuncID':([21,33,],[32,36,]),'saveVariableID':([27,42,74,132,],[34,49,88,170,]),'addMemoryInfo':([32,52,],[35,58,]),'setMain':([47,],[51,]),'funcBody':([48,51,165,190,216,218,226,],[52,57,189,212,221,222,227,]),'auxFuncBody':([53,61,80,],[59,81,90,]),'statements':([53,60,61,80,],[61,80,61,61,]),'assignment':([53,60,61,80,],[63,63,63,63,]),'writting':([53,60,61,80,],[64,64,64,64,]),'if':([53,60,61,80,],[65,65,65,65,]),'while':([53,60,61,80,],[66,66,66,66,]),'for':([53,60,61,80,],[67,67,67,67,]),'endFunction':([57,58,],[77,78,]),'addOperand':([68,101,],[82,124,]),'endProgram':([77,],[89,]),'auxWritting':([83,140,],[93,174,]),'logicExpression':([83,84,108,114,115,140,175,176,223,],[94,106,130,136,137,94,195,196,224,]),'exp':([83,84,108,114,115,140,175,176,177,178,179,180,181,182,223,],[96,96,96,96,96,96,96,96,197,198,199,200,201,202,96,]),'exp2':([83,84,108,114,115,140,175,176,177,178,179,180,181,182,183,184,223,],[97,97,97,97,97,97,97,97,97,97,97,97,97,97,203,204,97,]),'term':([83,84,108,114,115,140,175,176,177,178,179,180,181,182,183,184,185,186,187,188,223,],[98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,98,205,206,207,208,98,]),'factor':([83,84,108,114,115,140,175,176,177,178,179,180,181,182,183,184,185,186,187,188,223,],[99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,]),'constants':([83,84,108,114,115,140,175,176,177,178,179,180,181,182,183,184,185,186,187,188,223,],[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,]),'addCondStart':([85,],[108,]),'endPrint':([89,],[113,]),'addOperator':([91,144,145,148,149,150,151,152,153,156,157,160,161,162,163,],[114,175,176,177,178,179,180,181,182,183,184,185,186,187,188,]),'addParenthesis':([92,],[115,]),'doWrite':([94,],[117,]),'doWriteString':([95,],[118,]),'addConstantOperand':([95,102,103,107,],[119,125,126,119,]),'doLogicExpression':([96,],[120,]),'doCompExpression':([97,],[121,]),'doExpression':([98,],[122,]),'doTerm':([99,],[123,]),'addConstantBool':([104,105,],[127,128,]),'doIF':([106,224,],[129,225,]),'multipleWrite':([117,118,],[139,142,]),'auxLogicExpression':([120,],[143,]),'auxExp':([121,],[147,]),'exp2Aux':([122,],[155,]),'auxTerm':([123,],[159,]),'doWhile':([130,],[166,]),'auxFor':([131,191,],[168,213,]),'doAssign':([136,],[172,]),'removeParenthesis':([173,],[194,]),'else':([189,],[209,]),'endIF':([209,227,],[215,228,]),'doElse':([210,],[216,]),'endWhile':([212,],[217,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program_main","S'",1,None,None,None),
  ('program_main -> BTSProgam CTE_ID startup SEMI_COLON globalVariables globalFunctions MAIN saveFuncID addMemoryInfo LEFT_PAREN RIGHT_PAREN setMain funcBody endFunction endProgram endPrint','program_main',16,'p_mainFunction','parser.py',48),
  ('globalVariables -> vars','globalVariables',1,'p_globalVariables','parser.py',53),
  ('globalVariables -> empty','globalVariables',1,'p_globalVariables','parser.py',54),
  ('globalFunctions -> funcs','globalFunctions',1,'p_globalFunctions','parser.py',59),
  ('globalFunctions -> empty','globalFunctions',1,'p_globalFunctions','parser.py',60),
  ('vars -> auxVars','vars',1,'p_vars','parser.py',66),
  ('auxVars -> VAR type vars_type_single','auxVars',3,'p_auxVars','parser.py',71),
  ('auxVars -> VAR type vars_type_array','auxVars',3,'p_auxVars','parser.py',72),
  ('auxVars -> VAR type vars_type_matrix','auxVars',3,'p_auxVars','parser.py',73),
  ('auxVars -> empty','auxVars',1,'p_auxVars','parser.py',74),
  ('vars_type_single -> CTE_ID saveVariableID COMMA vars_type_single','vars_type_single',4,'p_vars_type_single','parser.py',79),
  ('vars_type_single -> CTE_ID saveVariableID SEMI_COLON auxVars','vars_type_single',4,'p_vars_type_single','parser.py',80),
  ('vars_type_array -> CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_array','vars_type_array',7,'p_vars_type_array','parser.py',85),
  ('vars_type_array -> CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON auxVars','vars_type_array',7,'p_vars_type_array','parser.py',86),
  ('vars_type_matrix -> CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_matrix','vars_type_matrix',10,'p_vars_type_matrix','parser.py',91),
  ('vars_type_matrix -> CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON auxVars','vars_type_matrix',10,'p_vars_type_matrix','parser.py',92),
  ('funcs -> funcs_aux globalFunctions','funcs',2,'p_funcs','parser.py',98),
  ('funcs_aux -> FUNC type CTE_ID saveFuncID LEFT_PAREN RIGHT_PAREN funcBody addMemoryInfo endFunction','funcs_aux',9,'p_funcs_aux','parser.py',103),
  ('funcBody -> LEFT_CURLY_BRACKET auxFuncBody RIGHT_CURLY_BRACKET','funcBody',3,'p_funcBody','parser.py',108),
  ('auxFuncBody -> vars statements auxFuncBody','auxFuncBody',3,'p_auxFuncBody','parser.py',113),
  ('auxFuncBody -> statements auxFuncBody','auxFuncBody',2,'p_auxFuncBody','parser.py',114),
  ('auxFuncBody -> empty','auxFuncBody',1,'p_auxFuncBody','parser.py',115),
  ('type -> INT setCurrentType','type',2,'p_type','parser.py',133),
  ('type -> FLOAT setCurrentType','type',2,'p_type','parser.py',134),
  ('type -> BOOL setCurrentType','type',2,'p_type','parser.py',135),
  ('type -> STRING setCurrentType','type',2,'p_type','parser.py',136),
  ('statements -> assignment','statements',1,'p_statements','parser.py',142),
  ('statements -> writting','statements',1,'p_statements','parser.py',143),
  ('statements -> if','statements',1,'p_statements','parser.py',144),
  ('statements -> while','statements',1,'p_statements','parser.py',145),
  ('statements -> for','statements',1,'p_statements','parser.py',146),
  ('writting -> PRINT LEFT_PAREN auxWritting RIGHT_PAREN SEMI_COLON','writting',5,'p_writting','parser.py',152),
  ('auxWritting -> logicExpression doWrite multipleWrite','auxWritting',3,'p_auxWritting','parser.py',157),
  ('auxWritting -> CTE_STRING doWriteString multipleWrite','auxWritting',3,'p_auxWritting','parser.py',158),
  ('multipleWrite -> COMMA auxWritting','multipleWrite',2,'p_multipleWrite','parser.py',163),
  ('multipleWrite -> empty','multipleWrite',1,'p_multipleWrite','parser.py',164),
  ('assignment -> CTE_ID addOperand EQUAL addOperator logicExpression doAssign SEMI_COLON','assignment',7,'p_assignment','parser.py',176),
  ('logicExpression -> exp doLogicExpression auxLogicExpression','logicExpression',3,'p_logicExpression','parser.py',182),
  ('auxLogicExpression -> AND addOperator logicExpression','auxLogicExpression',3,'p_auxLogicExpression','parser.py',187),
  ('auxLogicExpression -> OR addOperator logicExpression','auxLogicExpression',3,'p_auxLogicExpression','parser.py',188),
  ('auxLogicExpression -> empty','auxLogicExpression',1,'p_auxLogicExpression','parser.py',189),
  ('exp -> exp2 doCompExpression auxExp','exp',3,'p_exp','parser.py',194),
  ('auxExp -> GREATER_THAN addOperator exp','auxExp',3,'p_auxExp','parser.py',199),
  ('auxExp -> GREATER_EQUAL_THAN addOperator exp','auxExp',3,'p_auxExp','parser.py',200),
  ('auxExp -> LESS_THAN addOperator exp','auxExp',3,'p_auxExp','parser.py',201),
  ('auxExp -> LESS_EQUAL_THAN addOperator exp','auxExp',3,'p_auxExp','parser.py',202),
  ('auxExp -> NOT_EQUALS addOperator exp','auxExp',3,'p_auxExp','parser.py',203),
  ('auxExp -> EQUALS addOperator exp','auxExp',3,'p_auxExp','parser.py',204),
  ('auxExp -> empty','auxExp',1,'p_auxExp','parser.py',205),
  ('exp2 -> term doExpression exp2Aux','exp2',3,'p_exp2','parser.py',210),
  ('exp2Aux -> PLUS addOperator exp2','exp2Aux',3,'p_exp2Aux','parser.py',215),
  ('exp2Aux -> MINUS addOperator exp2','exp2Aux',3,'p_exp2Aux','parser.py',216),
  ('exp2Aux -> empty','exp2Aux',1,'p_exp2Aux','parser.py',217),
  ('term -> factor doTerm auxTerm','term',3,'p_term','parser.py',223),
  ('auxTerm -> TIMES addOperator term','auxTerm',3,'p_auxTerm','parser.py',228),
  ('auxTerm -> DIV addOperator term','auxTerm',3,'p_auxTerm','parser.py',229),
  ('auxTerm -> MOD addOperator term','auxTerm',3,'p_auxTerm','parser.py',230),
  ('auxTerm -> EXP addOperator term','auxTerm',3,'p_auxTerm','parser.py',231),
  ('auxTerm -> empty','auxTerm',1,'p_auxTerm','parser.py',232),
  ('factor -> LEFT_PAREN addParenthesis logicExpression RIGHT_PAREN removeParenthesis','factor',5,'p_factor','parser.py',238),
  ('factor -> constants','factor',1,'p_factor','parser.py',239),
  ('constants -> CTE_ID addOperand','constants',2,'p_constants','parser.py',244),
  ('constants -> CTE_INT addConstantOperand','constants',2,'p_constants','parser.py',245),
  ('constants -> CTE_FLOAT addConstantOperand','constants',2,'p_constants','parser.py',246),
  ('constants -> CTE_STRING addConstantOperand','constants',2,'p_constants','parser.py',247),
  ('constants -> TRUE addConstantBool','constants',2,'p_constants','parser.py',248),
  ('constants -> FALSE addConstantBool','constants',2,'p_constants','parser.py',249),
  ('if -> IF LEFT_PAREN logicExpression doIF RIGHT_PAREN funcBody else endIF','if',8,'p_if','parser.py',255),
  ('else -> ELSE doElse IF LEFT_PAREN logicExpression doIF RIGHT_PAREN funcBody endIF','else',9,'p_else','parser.py',260),
  ('else -> ELSE doElse funcBody','else',3,'p_else','parser.py',261),
  ('else -> empty','else',1,'p_else','parser.py',262),
  ('while -> WHILE LEFT_PAREN addCondStart logicExpression doWhile RIGHT_PAREN funcBody endWhile','while',8,'p_while','parser.py',267),
  ('for -> FOR LEFT_PAREN CTE_ID COMMA auxFor COMMA auxFor RIGHT_PAREN funcBody','for',9,'p_for','parser.py',272),
  ('auxFor -> CTE_ID','auxFor',1,'p_auxFor','parser.py',277),
  ('auxFor -> CTE_INT','auxFor',1,'p_auxFor','parser.py',278),
  ('startup -> <empty>','startup',0,'p_startup','parser.py',304),
  ('setMain -> <empty>','setMain',0,'p_setMain','parser.py',315),
  ('endProgram -> <empty>','endProgram',0,'p_endProgram','parser.py',321),
  ('endPrint -> <empty>','endPrint',0,'p_endPrint','parser.py',328),
  ('saveFuncID -> <empty>','saveFuncID',0,'p_saveFuncID','parser.py',345),
  ('addMemoryInfo -> <empty>','addMemoryInfo',0,'p_addMemoryInfo','parser.py',360),
  ('endFunction -> <empty>','endFunction',0,'p_endFunction','parser.py',366),
  ('doIF -> <empty>','doIF',0,'p_doIF','parser.py',376),
  ('endIF -> <empty>','endIF',0,'p_endIF','parser.py',390),
  ('doElse -> <empty>','doElse',0,'p_doElse','parser.py',398),
  ('doWhile -> <empty>','doWhile',0,'p_doWhile','parser.py',410),
  ('endWhile -> <empty>','endWhile',0,'p_endWhile','parser.py',424),
  ('addCondStart -> <empty>','addCondStart',0,'p_addCondStart','parser.py',435),
  ('saveVariableID -> <empty>','saveVariableID',0,'p_saveVariableID','parser.py',441),
  ('setCurrentType -> <empty>','setCurrentType',0,'p_setCurrentType','parser.py',469),
  ('addOperand -> <empty>','addOperand',0,'p_addOperand','parser.py',475),
  ('addConstantOperand -> <empty>','addConstantOperand',0,'p_addConstantOperand','parser.py',490),
  ('addConstantBool -> <empty>','addConstantBool',0,'p_addConstantBool','parser.py',514),
  ('addOperator -> <empty>','addOperator',0,'p_addOperator','parser.py',525),
  ('addParenthesis -> <empty>','addParenthesis',0,'p_addParenthesis','parser.py',532),
  ('removeParenthesis -> <empty>','removeParenthesis',0,'p_removeParenthesis','parser.py',538),
  ('doLogicExpression -> <empty>','doLogicExpression',0,'p_doLogicExpression','parser.py',545),
  ('doCompExpression -> <empty>','doCompExpression',0,'p_doCompExpression','parser.py',572),
  ('doExpression -> <empty>','doExpression',0,'p_doExpression','parser.py',599),
  ('doTerm -> <empty>','doTerm',0,'p_doTerm','parser.py',626),
  ('doAssign -> <empty>','doAssign',0,'p_doAssign','parser.py',653),
  ('doWrite -> <empty>','doWrite',0,'p_doWrite','parser.py',672),
  ('doWriteString -> <empty>','doWriteString',0,'p_doWriteString','parser.py',682),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',705),
]
