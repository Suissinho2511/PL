################################################################################
# NAME:     CSV TO JSON
# PURPOSE:  Converting a generic csv file to a json file
#GROUP:     5
# ELEMENTS: a93234 - Diogo Matos
#           a83630 - Duarte Serrão
#           a93208 - Vasco Oliveira
################################################################################
import ply.lex as lex

states = [
    ("TEXTQUALIFIED", "exclusive"),
    #("HEADER", "inclusive"),
    #("LIST", "exclusive")
]

tokens = [
    "QUOTES", 
    "FIELD",
    "BLANK",
    "LISTSIZE",
    "LISTFUNC"
    #"LISTLIMITATION"
]

################################################################################
# TOKEN'S FUNCTIONS
################################################################################

def t_QUOTES(t):
    r'"'
    t.lexer.begin("TEXTQUALIFIED")

#TODO: Deve fazer interferência com o LISTSIZE e LISTFUNC (as in, deve fazer match com eles, não?) (A não ser que não deixemos ter {} e ::)
def t_FIELD(t):
    #Estou a dizer que tem de começar com um caracter e que dps pode ter espaços pelo meio
    r'[^\n",\ \t]([\ \t]*[^,\n\ \t]+)*'
    t.lexer.fields.append(t.value)

def t_BLANK(t):
    r'(""|,[\ \t]*,|,\n)'
    t.lexer.fields.append("")

def t_LISTSIZE(t):
    r'{(\d+)(,\d+)?}'
    field = t.lexer.fields[-1]
    min_size = t.lexer.value(1)
    max_size = t.lexer.value(2)
    t.lexer.lists.append((field, min_size, max_size))

def t_LISTFUNC(t):
    r'::([a-zA-Z]+)'
    field = t.lexer.fields[-1]
    func = t.lexer.value(1)
    t.lexer.funcs.append((field,func))


def t_TEXTQUALIFIED_QUOTES(t):
    r'"'
    t.lexer.begin("INITIAL")
    
def t_TEXTQUALIFIED_FIELD(t):
    r'[^"]+'
    t.lexer.fields.append(t.value)


def t_ANY_error(t):
    #it just skips over anything we don't care
    t.lexer.skip(1)


################################################################################
# FUNCTION:  Main function and only one that we will need
################################################################################
def lexFunc(line, mode = "RECORD"):
    lexer = lex.lex()
    #if mode == "HEADER":
    #   lexer.begin("HEADER")

    # New variable that will hold all the fields in a record
    lexer.fields = []

    #Tuples (field, min_size, max_size)
    lexer.lists = []

    #Pairs (field, function)
    lexer.funcs = []

    lexer.input(line)

    # We must always iterate through the tokens
    for tok in lexer:
        pass

    return lexer.fields

