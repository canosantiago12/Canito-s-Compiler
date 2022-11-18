from re import M
import ply.lex as lex

# Tokens
tokens = ('IF', 'ELSE', 'FOR', 'WHILE', 
        'FUNC', 'RETURN', 'RETURN_SIGN', 'MAIN', 'BTSProgam',
        'VAR', 'INT', 'FLOAT', 'BOOL', 'STRING', 'TRUE', 'FALSE', 'CTE_INT', 'CTE_FLOAT', 'CTE_ID', 'CTE_STRING',
        'PLUS', 'MINUS', 'TIMES', 'DIV', 'MOD', 'EXP', 'EQUAL', 'LESS_THAN', 'LESS_EQUAL_THAN', 'GREATER_THAN', 'GREATER_EQUAL_THAN', 'EQUALS', 'NOT_EQUALS', 'AND', 'OR',
        'LEFT_PAREN', 'RIGHT_PAREN', 'LEFT_BRACKET', 'RIGHT_BRACKET', 'LEFT_CURLY_BRACKET', 'RIGHT_CURLY_BRACKET', 'COMMA', 'SEMI_COLON',
        'MEAN', 'MEDIAN', 'MODE', 'STANDARD_DEVIATION', 'VARIANCE', 'POISSON', 'BINOMIAL', 'PLOT', 'PRINT', 'READ_INPUT'
        )

# Reserved words
reserved = {
    'mainStage': 'MAIN',
    'var' : 'VAR',
    'func': 'FUNC',
    'return': 'RETURN',
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL',
    'string': 'STRING',
    'true': 'TRUE',
    'false': 'FALSE',
    'listen' : 'READ_INPUT',
    'print' : 'PRINT'
}

# Regexp
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIV = r'\/'
t_MOD = r'\%'
t_EXP = r'\^'
t_EQUAL = r'\='

t_EQUALS = r'\=\='
t_NOT_EQUALS = r'\!\='
t_LESS_THAN = r'\<'
t_LESS_EQUAL_THAN = r'\<\='
t_GREATER_THAN = r'\>'
t_GREATER_EQUAL_THAN = r'\>\='
t_AND = r'\&\&'
t_OR = r'\|\|'

t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_BRACKET = r'\['
t_RIGHT_BRACKET = r'\]'
t_LEFT_CURLY_BRACKET = r'\{'
t_RIGHT_CURLY_BRACKET = r'\}'

t_COMMA = r'\,'
t_SEMI_COLON = r'\;'

# Ignored characters
t_ignore = " \t"

t_CTE_STRING = r'"(.*?)"'
t_RETURN_SIGN = r'\-\>'
# t_CTE_STRING = r"""\"(.*)\"|\'(.*)\'"""
t_BTSProgam = "BTSProgam"

def t_CTE_ID(t):
    r'([a-z][a-zA-Z0-9]*)'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t
    
def t_CTE_FLOAT(t):
    r'[-]?[0-9]+([.][0-9]+)'
    t.value = float(t.value)
    return t

def t_CTE_INT(t):
    r'[-]?[0-9]+'
    t.value = int(t.value)
    return t

def t_skip_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_BLOCK_COMMENT(t):
    r'(\*\|(.|\n)*?\|\*)'
    pass

def t_LINE_COMMENT(t):
    r'\#.*'
    pass

lexer = lex.lex()