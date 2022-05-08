
##############
##	 TODO	##
##############

reserved = {
	'for'	:	'FOR',
	'if'	:	'IF',
	'else'	:	'ELSE',
	'while'	:	'WHILE',
	'/==='	:	'SECTIONBEGIN',
	'===/'	:	'SECTIONEND',
	'/*'	:	'COMMENTBEGIN',
	'*/'	:	'COMMENTEND',
	'$'		:	'FORMATTEDSTRINGDELIMITER',
	';'		:	'SEMICOLLON',
	'('		:	'OPARENTHESIS',
	')'		:	'CPARENTHESIS',
	'{'		:	'OCURLYBRACKETS',
	'}'		:	'CCURLYBRACKETS',
	':'		:	'COLLON',
	'='		:	'EQUAL',
	'+'		:	'PLUS',
	'-'		:	'MINUS',
	'*'		:	'MULT',
	'/'		:	'DIV',
	'||'	:	'OR',
	'&&'	:	'AND',
	'!'		:	'NOT',
	'>'		:	'GT',
	'<'		:	'LT',
	'>='	:	'GE',
	'<='	:	'LE',
	'=='	:	'EQ',
	'!='	:	'NEQ',
	'['		:	'OSQUAREBRACKETS',
	']'		:	'CSQUAREBRACKETS',
}
tokens = ['TEXT', 'STR', 'ID', 'NUM', 'COMMENTLINE', 'COMMENTBLOCK'] + list(reserved.values())
literals = []

states = [
	('section','exclusive'),
	('commentblock','exclusive'),
]

### INITIAL
t_ignore = ''

def t_SECTIONBEGIN(t):
	r'/==='
	t.lexer.begin('section')
	#print(t)
	return t;

def t_TEXT(t):
	r'((?!/===)(.|\s))+'
	#print(t)
	return t


### SECTION
t_section_ignore = ' \n\t\r'

def t_section_FOR(t):
	r'for'
	#print(t)
	return t;

def t_section_IF(t):
	r'if'
	#print(t)
	return t

def t_section_WHILE(t):
	r'while'
	#print(t)
	return t
	
def t_section_SECTIONEND(t):
	r'===/'
	t.lexer.begin('INITIAL')
	#print(t)
	return t;
	
def t_section_COMMENTBEGIN(t):
	r'/\*'
	t.lexer.push_state('commentblock')
	#print(t)
	#return t;

def t_section_STR(t):
	r'\"(?P<content>.*?)\"(?=\s*\$)'
	t.value = t.lexer.lexmatch.group('content')
	#print(t)
	return t

def t_section_ID(t):
	r'[a-zA-Z_]\w*'
	t.type = reserved.get(t.value, 'ID')
	#print(t)
	return t

def t_section_NUM(t):
	r'\d+(\.\d+)?'
	#print(t)
	return t

def t_section_COMMENTLINE(t):
	r'//[^\n]+'
	#print(t)
	#return t


### SYMBOLS

def t_section_FORMATTEDSTRINGDELIMITER(t):
	r'\$'
	#print(t)
	return t

def t_section_SEMICOLLON(t):
	r';'
	#print(t)
	return t

def t_section_OCURLYBRACKETS(t):
	r'{'
	#print(t)
	return t

def t_section_CCURLYBRACKETS(t):
	r'}'
	#print(t)
	return t

def t_section_COLLON(t):
	r':'
	#print(t)
	return t

def t_section_PLUS(t):
	r'\+'
	#print(t)
	return t

def t_section_MINUS(t):
	r'-'
	#print(t)
	return t

def t_section_MULT(t):
	r'\*'
	#print(t)
	return t

def t_section_DIV(t):
	r'/'
	#print(t)
	return t

def t_section_OPARENTHESIS(t):
	r'\('
	#print(t)
	return t

def t_section_CPARENTHESIS(t):
	r'\)'
	#print(t)
	return t

def t_section_OR(t):
	r'\|\|'
	#print(t)
	return t

def t_section_AND(t):
	r'&&'
	#print(t)
	return t


def t_section_GT(t):
	r'>'
	#print(t)
	return t

def t_section_LT(t):
	r'<'
	#print(t)
	return t

def t_section_GE(t):
	r'>='
	#print(t)
	return t

def t_section_LE(t):
	r'<='
	#print(t)
	return t

def t_section_EQ(t):
	r'=='
	#print(t)
	return t

def t_section_NEQ(t):
	r'!='
	#print(t)
	return t

def t_section_NOT(t):
	r'!'
	#print(t)
	return t

def t_section_EQUAL(t):
	r'='
	#print(t)
	return t

def t_section_OSQUAREBRACKETS(t):
	r'\['
	#print(t)
	return t

def t_section_CSQUAREBRACKETS(t):
	r'\]'
	#print(t)
	return t


### COMMENT

def t_commentblock_COMMENTEND(t):
	r'\*/'
	#print(t)
	t.lexer.pop_state()
	#return t;

def t_commentblock_COMMENTBLOCK(t):
	r'(\s|.)+?(?=\*/)'
	#print(t)
	#return t










def t_ANY_error(t):
	print("LEX ERROR! " + t.value)