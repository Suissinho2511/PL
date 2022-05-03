
##############
##	 TODO	##
##############

reserved = {
    'for': 'FOR',
    '/===': 'SECTIONBEGIN',
    '===/': 'SECTIONEND',
    '/*': 'COMMENTBEGIN',
    '*/': 'COMMENTEND',
    '$': 'FORMATTEDSTRINGDELIMITER'
}
tokens = ['NEWLINE', 'TEXT', 'STR', 'ID', 'COMMENTLINE', 'COMMENTBLOCK'] + list(reserved.values())
literals = [";", "(" , ")", "{", "}", ":"]

states = [
    ('foriterate','exclusive'),
    ('section','exclusive'),
    ('commentblock','exclusive')
]

def t_NEWLINE(t):
    r'\n'
    t.type = 'TEXT'
    return t

def t_section_FOR(t):
    r'for'
    print(t)
    t.lexer.begin('foriterate')
    t.lexer.args = 2
    return t;
    
def t_SECTIONBEGIN(t):
    r'/==='
    print(t)
    t.lexer.begin('section')
    return t;
    
def t_section_SECTIONEND(t):
    r'===/'
    print(t)
    t.lexer.begin('INITIAL')
    return t;
    
def t_section_COMMENTBEGIN(t):
    r'/\*'
    print(t)
    t.lexer.push_state('commentblock')
    #return t;
    
def t_commentblock_COMMENTEND(t):
    r'\*/'
    print(t)
    t.lexer.pop_state()
    #return t;

def t_section_FORMATTEDSTRINGDELIMITER(t):
    r'\$'
    print(t)
    return t
    
    
    
def t_TEXT(t):
    r'.+'
    print(t)
    return t

def t_section_STR(t):
    r'\"(?P<content>.*?)\"(?=\s*\$)'
    t.value = t.lexer.lexmatch.group('content')
    print(t)
    return t

def t_section_ID(t):
    r'[a-zA-Z_]\w*'
    #t.type = reserved.get(t.value, 'ID')
    print(t)
    return t

def t_foriterate_ID(t):
    r'[a-zA-Z_]\w*'
    #t.type = reserved.get(t.value, 'ID')
    print(t)
    t.lexer.args = t.lexer.args - 1
    if t.lexer.args <= 0:
        t.lexer.begin('section')
    return t
    
def t_section_COMMENTLINE(t):
    r'//[^\n]+'
    print(t)
    #return t
    
def t_commentblock_COMMENTBLOCK(t):
    r'(.|\n)+(?=\*/)'
    print(t)
    #return t
    
t_section_ignore = ' \n\t\r'
t_foriterate_ignore = ' \n\t\r'
t_ignore = ''

def t_ANY_error(t):
    print("LEX ERROR! " + t.value)