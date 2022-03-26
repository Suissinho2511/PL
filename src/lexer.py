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
    "LSIZE",
    "FUNC"
]

################################################################################
# TOKEN'S FUNCTIONS
################################################################################

def t_QUOTES(t):
    # the [\ \t]* is to ignore white characters
    r',?[\ \t]*"'
    t.lexer.begin("TEXTQUALIFIED")

def t_FIELD(t):
    # First it needs a character, then it can have spaces in between and ends in a character
    r',?[\ \t]*(?P<FIELD>[^,\n\ \t{}]([\ \t]*[^,\n\ \t{}]+)*)'
    t.lexer.fields.append(str(t.lexer.lexmatch.group("FIELD")))

def t_BLANK(t):
    # Empty fields
    r',?[\ \t]*""|,[\ \t]*(?=(,))|,[\ \t]*\n'
    # This way it wont pick up the commas belongling to lists
    if t.lexer.lexpos > t.lexer.pos:
        if t.lexer.mode == "HEADER":
            # If there is an empty field in the header, then we will create a category
            t.lexer.fields.append("EMPTY_" + str(t.lexer.count_empties))
            t.lexer.count_empties += 1
        else:
            t.lexer.fields.append("")

# We need to have the @TOKEN because we need to use the variable
# list_counter in the regular expression
@lex.TOKEN(r'(,[\ \t]*){' + list_counter + r'}')
def t_LIST_BLANK(t):
    global list_counter
    # We need to know the end of the list
    t.lexer.pos = t.lexer.lexpos + int(list_counter)
    # resetting the list counter
    list_counter = str(1)
    t.lexer.begin('INITIAL')


def t_LSIZE(t):
    r'{[\ \t]*(?P<MIN>\d+)[\ \t]*(,[\ \t]*(?P<MAX>\d+)[\ \t]*)?}'
    # Lists only exist in the header, not in records
    if t.lexer.mode == 'HEADER':
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
        

def t_LIST_FUNC(t):
    r'::(?P<OP>[a-zA-Z]+)'
    # We just need to add it to the end of the field list tuple by concatenation
    t.lexer.fields[-1] += (t.lexer.lexmatch.group("OP"),)


def t_TEXTQUALIFIED_QUOTES(t):
    r'"[\ \t]*'
    t.lexer.begin("INITIAL")
    
def t_TEXTQUALIFIED_FIELD(t):
    r'([^"]|\\")+'
    t.lexer.fields.append(t.value)

t_LIST_INITIAL_ignore = ' \t\n' # The INITIAL state will also ignore spaces
t_TEXTQUALIFIED_ignore = '\n'
#t_ANY_ignore = '\n'

def t_ANY_error(t):
    #it just skips over anything we don't care
    #t.lexer.skip(1)
    print("Error: " + str(t))


################################################################################
# FUNCTION:  Main function and only one that we will need
################################################################################
def lexFunc(line, mode = "RECORD"):
    lexer = lex.lex()
    
    lexer.mode = mode
    
    lexer.count_empties = 0
    
    lexer.pos = 0

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

