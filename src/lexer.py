import ply.lex as lex
import re

states = [
    ("TEXTQUALIFIED", "exclusive")
]

tokens = [
    "QUOTES", 
    "FIELD"
]


def t_FIELD(t):
    #Estou a dizer que tem de começar com um caracter e que dps pode ter espaços pelo meio
    r'[^\n", ](\ *[^,\n\ ]+)*'
    t.lexer.fields.append(t.value)
    
def t_TEXTQUALIFIED_FIELD(t):
    r'[^"\n]+'
    t.lexer.fields.append(t.value)

def t_QUOTES(t):
    r'"'
    t.lexer.begin("TEXTQUALIFIED")


def t_TEXTQUALIFIED_QUOTES(t):
    r'"'
    t.lexer.begin("INITIAL")


def t_ANY_error(t):
    t.lexer.skip(1)
    #print("ILLEGAL CHARACTER!" + '\'' + t.value[0] + '\'')

def t_newline(t):
    r'\n+'
        
t_ANY_ignore = r','

lexer = lex.lex()

lexer.fields = []

f = open("alunos.csv", "r", encoding="UTF8")
texto = f.readline()
lexer.input(texto)

for tok in lexer:
    pass

for field in lexer.fields:
    print(field)

f.close()
