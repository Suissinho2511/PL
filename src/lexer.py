import ply.lex as lex

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


def lexFunc(line, mode):
    lexer = lex.lex()

    lexer.fields = []

    lexer.input(line)

    for tok in lexer:
        pass

    return lexer.fields

