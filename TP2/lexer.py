
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
}
tokens = ['TEXT', 'STR', 'ID', 'COMMENTLINE', 'COMMENTBLOCK'] + list(reserved.values())
literals = []

states = [
	('section','exclusive'),
	('commentblock','exclusive'),
	('for','exclusive'),
	('if','exclusive'),
	('while','exclusive'),
]

### INITIAL
t_ignore = ''

def t_SECTIONBEGIN(t):
	r'/==='
	t.lexer.begin('section')
	#print(t)
	return t;

def t_TEXT(t):
	r'((?!/===)(.|\n))+'
	#print(t)
	return t


### SECTION
t_section_ignore = ' \n\t\r'

def t_section_FOR(t):
	r'for'
	t.lexer.begin('for')
	#print(t)
	return t;

def t_section_IF(t):
	r'if'
	t.lexer.begin('if')
	#print(t)
	return t

def t_section_WHILE(t):
	r'while'
	t.lexer.begin('while')
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

def t_section_FORMATTEDSTRINGDELIMITER(t):
	r'\$'
	#print(t)
	return t

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

def t_section_COMMENTLINE(t):
	r'//[^\n]+'
	#print(t)
	#return t

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


### COMMENT

def t_commentblock_COMMENTEND(t):
	r'\*/'
	#print(t)
	t.lexer.pop_state()
	#return t;

def t_commentblock_COMMENTBLOCK(t):
	r'(.|\n)+(?=\*/)'
	#print(t)
	#return t


### FOR
t_for_ignore = ' \n\t\r'

def t_for_ID(t):
	r'[a-zA-Z_]\w*'
	#print(t)
	return t

def t_for_OPARENTHESIS(t):
	r'\('
	#print(t)
	return t

def t_for_CPARENTHESIS(t):
	r'\)'
	t.lexer.begin('section')
	#print(t)
	return t

def t_for_COLLON(t):
	r':'
	#print(t)
	return t


### IF
t_if_ignore = ' \n\t\r'

def t_if_ID(t):
	r'[a-zA-Z_]\w*'
	#print(t)
	return t

def t_if_OPARENTHESIS(t):
	r'\('
	#print(t)
	return t

def t_if_CPARENTHESIS(t):
	r'\)'
	t.lexer.begin('section')
	#print(t)
	return t


### WHILE
t_while_ignore = ' \n\t\r'

def t_while_ID(t):
	r'[a-zA-Z_]\w*'
	#print(t)
	return t

def t_while_OPARENTHESIS(t):
	r'\('
	#print(t)
	return t

def t_while_CPARENTHESIS(t):
	r'\)'
	t.lexer.begin('section')
	#print(t)
	return t










def t_ANY_error(t):
	print("LEX ERROR! " + t.value)