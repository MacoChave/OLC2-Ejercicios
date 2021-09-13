tokens = [
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'PARI',
    'PARD',
    'ID',
    'MENOR',
    'MENORIGUAL',
    'MAYOR',
    'MAYORIGUAL',
    'IGUAL',
    'NOIGUAL',
    'NOT',
    'AND',
    'OR',
    'NUM'
]

# TOKENS
t_MAS = r'\+'
t_MENOS = r'-'
t_POR = r'\*'
t_DIV = r'/'
t_MENOR = r'<'
t_MENORIGUAL = r'<='
t_MAYOR = r'>'
t_MAYORIGUAL = r'>='
t_IGUAL = r'=='
t_NOIGUAL = r'!='
t_NOT = r'!'
t_AND = r'&&'
t_OR = r'\|\|'
t_PARI = r'\('
t_PARD = r'\)'

def t_ID(t) :
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUM(t) :
    r'\d+'
    try :
        t.value = int(t.value)
    except ValueError :
        print('Entero {t.value} es muy grande')
        t.value = 0
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

precedence = (
    ('left', 'IGUAL', 'NOIGUAL', 'MENOR', 'MAYOR', 'MENORIGUAL', 'MAYORIGUAL'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
)

# GRAMMAR
from atributos import *

temporal = 0
label = 0

def newTemp() :
    global temporal
    temporal += 1
    return f't{temporal}'

def newLabel() :
    global label
    label += 1
    return f'L{label}'

def p_start(t) :
    'start : logic_o'
    t[0] = t[1]

def p_logic_o(t) :
    'logic_o : logic_o OR logic_a'
    c3d = f'{t[1].c3d} {t[1].false_label}:\n{t[3].c3d}'
    t[0] = Atributo('', c3d, f'{t[1].true_label}, {t[3].true_label}', t[3].false_label)

def p_to_logic_a(t) :
    'logic_o : logic_a'
    t[0] = t[1]

def p_logic_a(t) :
    'logic_a : logic_a AND logic_n'
    c3d = f'{t[1].c3d} {t[1].true_label}:\n{t[3].c3d}'
    t[0] = Atributo('', c3d, t[3].true_label, f'{t[1].false_label}, {t[3].false_label}')

def p_to_logic_not(t) :
    'logic_a : logic_n'
    t[0] = t[1]

def p_logic_not(t) :
    'logic_n : NOT logic_o'
    t[0] = Atributo('', t[2].c3d, t[2].false_label, t[2].true_label)

def p_logic_rel(t) :
    'logic_n : exp_r'
    t[0] = t[1]

def p_rel(t) :
    '''exp_r    : exp_e MENOR exp_e
                | exp_e MENORIGUAL exp_e
                | exp_e MAYOR exp_e
                | exp_e MAYORIGUAL exp_e
                | exp_e IGUAL exp_e
                | exp_e NOIGUAL exp_e'''
    if t[2] == '<' :
        lv = newLabel()
        lf = newLabel()
        temp = ''
        c3d = f'{t[1].c3d}{t[3].c3d}\nif {t[1].temp} < {t[3].temp} goto {lv}\n goto {lf}\n'
        t[0] = Atributo(temp, c3d, lv, lf)
    elif t[2] == '<=' :
        lv = newLabel()
        lf = newLabel()
        temp = ''
        c3d = f'{t[1].c3d}{t[3].c3d}\nif {t[1].temp} <= {t[3].temp} goto {lv}\n goto {lf}\n'
        t[0] = Atributo(temp, c3d, lv, lf)
    elif t[2] == '>' :
        lv = newLabel()
        lf = newLabel()
        temp = ''
        c3d = f'{t[1].c3d}{t[3].c3d}\nif {t[1].temp} > {t[3].temp} goto {lv}\n goto {lf}\n'
        t[0] = Atributo(temp, c3d, lv, lf)
    elif t[2] == '>=' :
        lv = newLabel()
        lf = newLabel()
        temp = ''
        c3d = f'{t[1].c3d}{t[3].c3d}\nif {t[1].temp} >= {t[3].temp} goto {lv}\n goto {lf}\n'
        t[0] = Atributo(temp, c3d, lv, lf)
    elif t[2] == '==' :
        lv = newLabel()
        lf = newLabel()
        temp = ''
        c3d = f'{t[1].c3d}{t[3].c3d}\nif {t[1].temp} == {t[3].temp} goto {lv}\n goto {lf}\n'
        t[0] = Atributo(temp, c3d, lv, lf)
    elif t[2] == '!=' :
        lv = newLabel()
        lf = newLabel()
        temp = ''
        c3d = f'{t[1].c3d}{t[3].c3d}\nif {t[1].temp} != {t[3].temp} goto {lv}\n goto {lf}\n'
        t[0] = Atributo(temp, c3d, lv, lf)

# def p_rel_e(t) :
#     'exp_r : exp_e'
#     t[0] = Atributo(t[1].temp, t[1].c3d)
    
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
    t[0] = t[1]

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
    t[0] = t[1]

def p_parentesis(t) :
    'exp_f : PARI exp_e PARD'
    t[0] = Atributo(t[2].temp, t[2].c3d)

def p_soloid(t) :
    'exp_f : ID'
    t[0] = Atributo(t[1], '')

def p_num(t) :
    'exp_f : NUM'
    t[0] = Atributo(t[1], '')

def p_error(t):
    print(t)
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input) :
    global temporal
    global label
    label = 0
    temporal = 0
    return parser.parse(input)