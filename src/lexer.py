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
    ("TEXTQUALIFIED", "exclusive")
]

tokens = [
    "QUOTES", 
    "FIELD",
    "BLANK",
    "LISTSIZE",
    "LISTFUNC"
]

################################################################################
# TOKEN'S FUNCTIONS
################################################################################

def t_QUOTES(t):
    r',?"'
    t.lexer.begin("TEXTQUALIFIED")

def t_FIELD(t):
    #r',?[\ \t]*(?P<content>\w+)[\ \t]*'    # ",   exemplo_1   ,"
    r',?(?P<content>\w+)'                   # ",exemplo_2,"
    #r',?(?P<content>[^,"{}:\n]+)'          # ",   exemplo   3   ,"
    t.lexer.fields.append(t.lexer.lexmatch.group("content"))

def t_BLANK(t):
    r',?""|,(?=[,\n])'
    t.lexer.fields.append("")

def t_LISTSIZE(t):
    r'{(?P<min_size>\d+)(,(?P<max_size>\d+))?}'

    field = t.lexer.fields[-1]
    min_size = int(t.lexer.lexmatch.group("min_size"))
    max_size_str = t.lexer.lexmatch.group("max_size")
    if max_size_str:
        max_size = int(max_size_str)
    else:
        max_size = min_size

    t.lexer.lists[field] = (min_size, max_size)

def t_LISTFUNC(t):
    r'::(?P<op>[a-zA-Z]+)'
    field = t.lexer.fields[-1]
    func = t.lexer.lexmatch.group("op")
    t.lexer.funcs[field] = func


def t_TEXTQUALIFIED_QUOTES(t):
    r'"'
    t.lexer.begin("INITIAL")
    
def t_TEXTQUALIFIED_FIELD(t):
    r'[^"]+'
    t.lexer.fields.append(t.value)

t_ANY_ignore = '\n'

def t_ANY_error(t):
    #it just skips over anything we don't care
    print("Error: " + str(t))


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
        lexer.fields = removeEmpty(lexer.fields)
        return (lexer.fields, lexer.lists, lexer.funcs)
    else:
        return lexer.fields

def removeEmpty(l):
    result = []
    for s in l:
        if not s == "":
            result.append(s)
    return result