
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BINOMIAL BOOL COMMA CTE_BOOL CTE_FLOAT CTE_ID CTE_INT DIV ELSE EQUAL EXP FALSE FLOAT FOR FUNC GREATER_EQUAL_THAN GREATER_THAN IF INT LEFT_BRACKET LEFT_CURLY_BRACKET LEFT_PAREN LESS_EQUAL_THAN LESS_THAN MAIN MEAN MEDIAN MINUS MOD MODE NOT_EQUAL OR PLOT PLUS POISSON PRINT PROGRAM READ_INPUT RETURN RIGHT_BRACKET RIGHT_CURLY_BRACKET RIGHT_PAREN SEMI_COLON STANDARD_DEVIATION STRING TIMES TRUE VAR VARIANCE VOID WHILE\n    program_main : PROGRAM CTE_ID startup SEMI_COLON globalVariables globalFunctions MAIN saveFuncID LEFT_PAREN RIGHT_PAREN LEFT_CURLY_BRACKET RIGHT_CURLY_BRACKET\n    \n    globalVariables : vars\n                    | empty\n    \n    globalFunctions : funcs\n                    | empty\n    \n    vars : VAR type vars_type\n         | VAR type vars_type_array\n         | VAR type vars_type_matrix\n         | empty\n    \n    vars_type : CTE_ID saveVariableID COMMA vars_type\n              | CTE_ID saveVariableID SEMI_COLON vars\n    \n    vars_type_array : CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_array\n                    | CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON vars\n    \n    vars_type_matrix : CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_matrix\n                     | CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON vars\n    \n    funcs : funcs_aux globalFunctions\n    \n    funcs_aux : FUNC CTE_ID saveFuncID LEFT_PAREN RIGHT_PAREN LEFT_CURLY_BRACKET RIGHT_CURLY_BRACKET\n    \n    type : INT setCurrentType\n         | FLOAT setCurrentType\n         | BOOL setCurrentType\n         | STRING setCurrentType\n    startup :saveFuncID :saveVariableID :setCurrentType :empty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,50,],[0,-1,]),'CTE_ID':([2,14,15,16,17,18,19,27,28,29,30,36,53,61,],[3,22,26,-25,-25,-25,-25,-18,-19,-20,-21,41,56,64,]),'SEMI_COLON':([3,4,26,33,41,48,49,59,69,],[-22,5,-24,37,-24,37,54,62,54,]),'VAR':([5,37,54,62,],[9,9,9,9,]),'FUNC':([5,6,7,8,13,23,24,25,37,42,43,44,51,54,57,58,62,65,66,],[-26,14,-2,-3,14,-6,-7,-8,-26,-10,-11,-9,-17,-26,-12,-13,-26,-14,-15,]),'MAIN':([5,6,7,8,10,11,12,13,21,23,24,25,37,42,43,44,51,54,57,58,62,65,66,],[-26,-26,-2,-3,20,-4,-5,-26,-16,-6,-7,-8,-26,-10,-11,-9,-17,-26,-12,-13,-26,-14,-15,]),'INT':([9,],[16,]),'FLOAT':([9,],[17,]),'BOOL':([9,],[18,]),'STRING':([9,],[19,]),'LEFT_PAREN':([20,22,31,32,],[-23,-23,34,35,]),'COMMA':([26,33,41,48,49,59,69,],[-24,36,-24,36,53,61,53,]),'LEFT_BRACKET':([26,33,49,56,60,64,68,72,],[-24,38,52,-24,63,-24,70,52,]),'RIGHT_PAREN':([34,35,],[39,40,]),'CTE_INT':([38,52,63,70,],[45,55,67,71,]),'LEFT_CURLY_BRACKET':([39,40,],[46,47,]),'RIGHT_BRACKET':([45,55,67,71,],[49,59,69,72,]),'RIGHT_CURLY_BRACKET':([46,47,],[50,51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program_main':([0,],[1,]),'startup':([3,],[4,]),'globalVariables':([5,],[6,]),'vars':([5,37,54,62,],[7,43,58,66,]),'empty':([5,6,13,37,54,62,],[8,12,12,44,44,44,]),'globalFunctions':([6,13,],[10,21,]),'funcs':([6,13,],[11,11,]),'funcs_aux':([6,13,],[13,13,]),'type':([9,],[15,]),'vars_type':([15,36,],[23,42,]),'vars_type_array':([15,53,],[24,57,]),'vars_type_matrix':([15,61,],[25,65,]),'setCurrentType':([16,17,18,19,],[27,28,29,30,]),'saveFuncID':([20,22,],[31,32,]),'saveVariableID':([26,41,56,64,],[33,48,60,68,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program_main","S'",1,None,None,None),
  ('program_main -> PROGRAM CTE_ID startup SEMI_COLON globalVariables globalFunctions MAIN saveFuncID LEFT_PAREN RIGHT_PAREN LEFT_CURLY_BRACKET RIGHT_CURLY_BRACKET','program_main',12,'p_mainFunction','parser.py',172),
  ('globalVariables -> vars','globalVariables',1,'p_globalVariables','parser.py',177),
  ('globalVariables -> empty','globalVariables',1,'p_globalVariables','parser.py',178),
  ('globalFunctions -> funcs','globalFunctions',1,'p_globalFunctions','parser.py',183),
  ('globalFunctions -> empty','globalFunctions',1,'p_globalFunctions','parser.py',184),
  ('vars -> VAR type vars_type','vars',3,'p_vars','parser.py',191),
  ('vars -> VAR type vars_type_array','vars',3,'p_vars','parser.py',192),
  ('vars -> VAR type vars_type_matrix','vars',3,'p_vars','parser.py',193),
  ('vars -> empty','vars',1,'p_vars','parser.py',194),
  ('vars_type -> CTE_ID saveVariableID COMMA vars_type','vars_type',4,'p_vars_type','parser.py',199),
  ('vars_type -> CTE_ID saveVariableID SEMI_COLON vars','vars_type',4,'p_vars_type','parser.py',200),
  ('vars_type_array -> CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_array','vars_type_array',7,'p_vars_type_array','parser.py',205),
  ('vars_type_array -> CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON vars','vars_type_array',7,'p_vars_type_array','parser.py',206),
  ('vars_type_matrix -> CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET COMMA vars_type_matrix','vars_type_matrix',10,'p_vars_type_matrix','parser.py',211),
  ('vars_type_matrix -> CTE_ID saveVariableID LEFT_BRACKET CTE_INT RIGHT_BRACKET LEFT_BRACKET CTE_INT RIGHT_BRACKET SEMI_COLON vars','vars_type_matrix',10,'p_vars_type_matrix','parser.py',212),
  ('funcs -> funcs_aux globalFunctions','funcs',2,'p_funcs','parser.py',218),
  ('funcs_aux -> FUNC CTE_ID saveFuncID LEFT_PAREN RIGHT_PAREN LEFT_CURLY_BRACKET RIGHT_CURLY_BRACKET','funcs_aux',7,'p_funcs_aux','parser.py',223),
  ('type -> INT setCurrentType','type',2,'p_type','parser.py',229),
  ('type -> FLOAT setCurrentType','type',2,'p_type','parser.py',230),
  ('type -> BOOL setCurrentType','type',2,'p_type','parser.py',231),
  ('type -> STRING setCurrentType','type',2,'p_type','parser.py',232),
  ('startup -> <empty>','startup',0,'p_startup','parser.py',237),
  ('saveFuncID -> <empty>','saveFuncID',0,'p_saveFuncID','parser.py',244),
  ('saveVariableID -> <empty>','saveVariableID',0,'p_saveVariableID','parser.py',251),
  ('setCurrentType -> <empty>','setCurrentType',0,'p_setCurrentType','parser.py',255),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',265),
]
