################################################################################
# NAME:     CSV TO JSON
# PURPOSE:  Converting a generic csv file to a json file
#GROUP:     5
# ELEMENTS: a93234 - Diogo Matos
#           a83630 - Duarte Serrão
#           a93208 - Vasco Oliveira
################################################################################
import ply.lex as lex

list_counter = str(1)

states = [
    ("TEXTQUALIFIED", "exclusive"),
    ("LIST", "exclusive")
    
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
    #Estou a dizer que tem de começar com um caracter e que dps pode ter espaços pelo meio
    r'([^,\n\ \t{}]|::)([\ \t]*([^,\n\ \t{}]|::)+)*'
    t.lexer.fields.append(t.value)

#def t_BLANK(t):
#    r'(""|,[\ \t]*,|,\n)'
#    global list_counter
#    print(str(list_counter) + "1")
#    
#    #r',?[\ \t]*(?P<content>\w+)[\ \t]*'    # ",   exemplo_1   ,"
#    r',?(?P<content>\w+)'                   # ",exemplo_2,"
#    #r',?(?P<content>[^,"{}:\n]+)'          # ",   exemplo   3   ,"
#    t.lexer.fields.append(t.lexer.lexmatch.group("content"))

#def t_BLANK(t):
#    r',?""|,(?=[,\n])'
#    t.lexer.fields.append("")

# We need to have the @TOKEN because we need to use the variable
# list_counter in the regular expression
@lex.TOKEN(r'(,[\ \t]*){' + list_counter + r'}')
def t_LIST_BLANK(t):
    global list_counter
    print(str(list_counter) + "2")
    list_counter = str(1)
    t.lexer.begin('INITIAL')


def t_LISTSIZE(t):
    # the [\ \t]* is to ignore white characters
    r'{[\ \t]*(?P<MIN>\d+)[\ \t]*(?:,[\ \t]*(?P<MAX>\d+)[\ \t]*)?}'
    
    # We need to begin the list state to read the consequent commas
    t.lexer.begin('LIST')
    
    # Getting each group with values for the interval
    match = t.lexer.lexmatch
    min_size = match.group('MIN')
    # We can't have the int function here, because max_size may be a NoneType
    max_size = match.group('MAX')
    
    field = t.lexer.fields[-1]
    # If the second group doesn't exist, then the min size is the only one
    if max_size == None:
        global list_counter
        list_counter = str(min_size)
        t.lexer.fields[-1] = (field, int(min_size))
        
        
    else:
        list_counter = str(max_size)
        t.lexer.fields[-1] = (field, (int(min_size), int(max_size)))
        

def t_LISTFUNC(t):
    r'::(?P<op>[a-zA-Z]+)'
    field = t.lexer.fields[-1]
    func = t.lexer.lexmatch.group("op")
    t.lexer.funcs[field] = func


def t_TEXTQUALIFIED_QUOTES(t):
    r'"'
    t.lexer.begin("INITIAL")
    
def t_TEXTQUALIFIED_FIELD(t):
    r'([^"]|\\")+'
    t.lexer.fields.append(t.value)

t_ANY_ignore = '\n,'

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

    # Dictionary {field: function}
    #lexer.funcs = {}

    lexer.input(line)

    # We must always iterate through the tokens
    for tok in lexer:
        pass


    return lexer.fields

    #if mode == "HEADER":
    #    lexer.fields = removeEmpty(lexer.fields)
    #    return (lexer.fields, lexer.lists, lexer.funcs)
    #else:
    #    return lexer.fields

def removeEmpty(l):
    result = []
    for s in l:
        if not s == "":
            result.append(s)
    return result

