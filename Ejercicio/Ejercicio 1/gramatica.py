tokens = [
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'PARI',
    'PARD',
    'ID'
]

# TOKENS
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIV = r'/'
t_PARI = r'\('
t_PARD = r'\)'

def t_ID(t) :
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# CARACTERES IGNORADOS
t_ignore = ' \t'

def t_newline(t) :
    r'\n'
    t.lexer.lineno += t.value.count('\n')

def t_error(t) :
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# LEX PARSER
import ply.lex as lex
lexer = lex.lex()

# GRAMMAR
from atributos import *

temporal = 0

def newTemp() :
    global temporal
    temporal += 1
    return f't{temporal}'

def p_start(t) :
    'start : exp_e'
    t[0] = t[1]
    
def p_adicion(t) :
    '''exp_e    : exp_e MAS exp_t
                | exp_e MENOS exp_t'''
    if t[2] == '+' : 
        temp = newTemp()
        c3d = f'{t[1].c3d}{t[3].c3d}\n{temp} = {t[1].temp} + {t[3].temp}'
        t[0] = Atributo(temp, c3d)
    elif t[2] == '-' :
        temp = newTemp()
        c3d = f'{t[1].c3d}{t[3].c3d}\n{temp} = {t[1].temp} - {t[3].temp}'
        t[0] = Atributo(temp, c3d)

def p_to_multiplo(t) :
    'exp_e : exp_t'
    t[0] = Atributo(t[1].temp, t[1].c3d)

def p_multiplicacion(t) :
    '''exp_t    : exp_t POR exp_f
                | exp_t DIV exp_f'''
    if t[2] == '*' : 
        temp = newTemp()
        c3d = f'{t[1].c3d}{t[3].c3d}\n{temp} = {t[1].temp} * {t[3].temp}'
        t[0] = Atributo(temp, c3d)
    elif t[2] == '/' :
        temp = newTemp()
        c3d = f'{t[1].c3d}{t[3].c3d}\n{temp} = {t[1].temp} / {t[3].temp}'
        t[0] = Atributo(temp, c3d)

def p_to_f(t) :
    'exp_t : exp_f'
    t[0] = Atributo(t[1].temp, t[1].c3d)

def p_parentesis(t) :
    'exp_f : PARI exp_e PARD'
    t[0] = Atributo(t[2].temp, t[2].c3d)

def p_soloid(t) :
    'exp_f : ID'
    t[0] = Atributo(t[1], '')

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    global temporal
    temporal = 0
    return parser.parse(input)