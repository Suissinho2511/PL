

reserved = {
	'for':		'FOR',
	'if':		'IF',
	'else':		'ELSE',
	'while':	'WHILE',		
}

tokens = [	'TEXT', 'STR', 'ID', 'NUM', 'COMMENTLINE', 'COMMENTBLOCK', 'SECTIONBEGIN', 'SECTIONEND',
			'COMMENTBEGIN', 'COMMENTEND', 'FORMATTEDSTRINGDELIMITER', 'SEMICOLLON', 'OPARENTHESIS',
			'CPARENTHESIS', 'OCURLYBRACKETS', 'CCURLYBRACKETS', 'COLLON', 'EQUAL', 'PLUS', 'MINUS',
			'MULT', 'DIV', 'OR', 'AND', 'NOT', 'GT', 'LT', 'GE', 'LE', 'EQ', 'NEQ', 'OSQUAREBRACKETS',
			'CSQUAREBRACKETS'] + list(reserved.values())

literals = []

states = [
	('section', 'exclusive'),
	('commentblock', 'exclusive'),
]

# INITIAL
t_ignore = ''

t_TEXT  = r'((?!/===)(.|\s))+'

def t_SECTIONBEGIN(t):
	r'/==='
	t.lexer.begin('section')
	return t



# SECTION
t_section_ignore = ' \n\t\r'

t_section_FOR						= r'for'
t_section_IF						= r'if'
t_section_WHILE						= r'while'
t_section_NUM						= r'\d+(\.\d+)?'
t_section_FORMATTEDSTRINGDELIMITER	= r'\$'
t_section_SEMICOLLON				= r';'
t_section_OCURLYBRACKETS			= r'{'
t_section_CCURLYBRACKETS			= r'}'
t_section_COLLON					= r':'
t_section_PLUS						= r'\+'
t_section_MINUS						= r'-'
t_section_MULT						= r'\*'
t_section_DIV						= r'/'
t_section_OPARENTHESIS				= r'\('
t_section_CPARENTHESIS				= r'\)'
t_section_OR						= r'\|\|'
t_section_AND						= r'&&'
t_section_GT						= r'>'
t_section_LT						= r'<'
t_section_GE						= r'>='
t_section_LE						= r'<='
t_section_EQ  						= r'=='
t_section_NEQ  						= r'!='
t_section_NOT  						= r'!'
t_section_EQUAL 					= r'='
t_section_OSQUAREBRACKETS  			= r'\['
t_section_CSQUAREBRACKETS  			= r'\]'


def t_section_SECTIONEND(t):
	r'===/'
	t.lexer.begin('INITIAL')
	return t


def t_section_STR(t):
	r'\"(?P<content>.*?)(?<!\\)\"'
	t.value = t.lexer.lexmatch.group('content')
	return t


def t_section_ID(t):
	r'[a-zA-Z_]\w*'
	t.type = reserved.get(t.value, 'ID')
	return t


def t_section_COMMENTLINE(t):
	r'//[^\n]+'


def t_section_COMMENTBEGIN(t):
	r'/\*'
	t.lexer.begin('commentblock')



# COMMENT

def t_commentblock_COMMENTEND(t):
	r'\*/'
	t.lexer.begin('section')


def t_commentblock_COMMENTBLOCK(t):
	r'(\s|.)+?(?=\*/)'




def t_ANY_error(t):
	print("LEX ERROR! " + t.value)