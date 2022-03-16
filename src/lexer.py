import sys
import ply.lex as lex

tokens = ["quotes", "field"]

states = [
    ("textQualified", "exclusive")
]


def t_field(t):
    r'(\w)+'
    print(t.value, end="")


def t_textQualified_field(t):
    r'[^"\n]+'
    print(t.value, end="")


def t_quotes(t):
    r'"'
    t.lexer.begin("textQualified")


def t_textQualifield_quotes(t):
    r'"'
    t.lexer.begin("INITIAL")


def t_ANY_error(t):
    print("ILLEGAL CHARACTER!" + '\'' + t.value[0] + '\'')


t_ANY_ignore = r'\n ?,"'

lexer = lex.lex()

f = open("alunos.csv", "r", encoding="UTF8")
texto = f.read()
lexer.input(texto)

for tok in lexer:
    print(tok)

f.close()
