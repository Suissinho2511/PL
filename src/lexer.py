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

def t_FIELD(t):
    #Estou a dizer que tem de começar com um caracter e que dps pode ter espaços pelo meio
    r'[^\n",\ \t\{\}\:]([\ \t]*[^",\n\ \t\{\}\:]+)*[\ \t]*,?'
    t.lexer.fields.append(t.value)

def t_BLANK(t):
    #r'(,[\ \t]*,|,\n)'
    r',(?=[,\n])'
    t.lexer.fields.append(t.lexer.fields[-1] + ".")

def t_LISTSIZE(t):
    r'{(\d+)(,\d+)?}'

    print(t.lexer.lexmatch.groups())
    field = t.lexer.fields[-1]
    min_size = t.lexer.lexmatch.group(1)
    max_size = t.lexer.lexmatch.group(2)
    t.lexer.lists[field] = (min_size, max_size)

def t_LISTFUNC(t):
    r'::([a-zA-Z]+)'
    field = t.lexer.fields[-1]
    func = t.lexer.lexmatch.group(1)
    t.lexer.funcs[field] = func


def t_TEXTQUALIFIED_QUOTES(t):
    r'"[\ \t]*,'
    t.lexer.begin("INITIAL")
    
def t_TEXTQUALIFIED_FIELD(t):
    r'[^"]+'
    t.lexer.fields.append(t.value)

t_ignore = "\n"

t_TEXTQUALIFIED_ignore = ""

def t_ANY_error(t):
    #it just skips over anything we don't care
    #t.lexer.skip(1)
    print(t.value)


################################################################################
# FUNCTION:  Main function and only one that we will need
################################################################################
def lexFunc(line, mode = "RECORD"):
    lexer = lex.lex()
    #if mode == "HEADER":
    #   lexer.begin("HEADER")

    # New variable that will hold all the fields in a record
    lexer.fields = []

    # Dictionary {field: (min_size, max_size)}
    lexer.lists = {}

    # Dictionary {field: function}
    lexer.funcs = {}

    lexer.input(line)

    # We must always iterate through the tokens
    for tok in lexer:
        pass

    if mode == "HEADER":
        return (lexer.fields, lexer.lists, lexer.funcs)
    else:
        return lexer.fields