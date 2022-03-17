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
    #"LISTSIZE",
    #"LISTLIMITATION"
]

################################################################################
# TOKEN'S FUNCTIONS
################################################################################
def t_FIELD(t):
    #Estou a dizer que tem de começar com um caractere e que dps pode ter espaços pelo meio
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
    #it just skips over anything we don't care
    t.lexer.skip(1)


################################################################################
# FUNCTION:  Main function and only one that we will need
################################################################################
def lexFunc(line, mode = "RECORD"):
    lexer = lex.lex()
    #if mode == "HEADER":
        #lexer.begin(mode)

    #New variable that will hold all the fields in a record
    lexer.fields = []

    lexer.input(line)

    #We must always iterate through the tokens
    for tok in lexer:
        pass

    return lexer.fields

