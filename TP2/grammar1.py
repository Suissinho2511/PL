


"""
Sections    : Sections Section
			| Sections TEXT
			| 
"""
def p_sections_section(p):
	'Sections : Sections Section'
	p[0] = p[1] + [('section', p[2])]
	#print('Sections : Sections Section')

def p_sections_text(p):
	'Sections : Sections TEXT'
	p[0] = p[1] + [('text', p[2])]
	#print('Sections : Sections TEXT')

def p_sections_empty(p):
	'Sections : '
	p[0] = []
	#print('Sections : ')


"""
Section : SECTIONBEGIN SectionContent SECTIONEND
"""
def p_section(p):
	'Section : SECTIONBEGIN SectionContent SECTIONEND'
	p[0] = p[2]
	#print('Section : SECTIONBEGIN SectionContent SECTIONEND')


"""
SectionContent  : ListOps
"""
def p_sectioncontent(p):
	'SectionContent : ListOps'
	p[0] = p[1]
	#print('SectionContent : ListOps')


"""
ListOps : ListOps Op
		| 
"""
def p_listops_op(p):
	'ListOps : ListOps Op'
	p[0] = p[1] + p[2]
	#print('ListOps : ListOps Op')

def p_listops_empty(p):
	'ListOps : '
	p[0] = []
	#print('ListOps : ')


"""
Op  : ForBlock
	| "$" FormattedStr ";"
	| IfBlock
"""
def p_op_forblock(p):
	'Op : ForBlock'
	p[0] = p[1]
	#print('Op : ForBlock')

def p_op_formattedstr(p):
	'Op : FORMATTEDSTRINGDELIMITER FormattedStr SEMICOLLON'
	p[0] = p[2]
	#print('Op : FORMATTEDSTRINGDELIMITER FormattedStr ";"')

def p_op_ifblock(p):
	'Op : IfBlock'
	p[0] = p[1]
	#print('Op : IfBlock')


"""
FormattedStr    : FormattedStr STR "$"
				| FormattedStr ID "$"
				| 
"""
def p_formattedstr_str(p):
	'FormattedStr : FormattedStr STR FORMATTEDSTRINGDELIMITER'
	p[0] = p[1] + [('str', p[2])]
	#print('FormattedStr : FormattedStr STR FORMATTEDSTRINGDELIMITER')

def p_formattedstr_id(p):
	'FormattedStr : FormattedStr ID FORMATTEDSTRINGDELIMITER'
	p[0] = p[1] + [('id', p[2])]
	#print('FormattedStr : FormattedStr ID FORMATTEDSTRINGDELIMITER')

def p_formattedstr_empty(p):
	'FormattedStr : '
	p[0] = []
	#print('FormattedStr : ')


"""
ForBlock	: FOR "(" ID ":" ID ")" Op
			| FOR "(" ID ":" ID ")" "{" ListOps "}"
"""
def p_forblock_iterate_single(p):
	'ForBlock : FOR OPARENTHESIS ID COLLON ID CPARENTHESIS Op'
	p[0] = [('for', (p[3],p[5], p[7]))]
	#print('ForBlock : FOR "(" ID ":" ID ")" Op')
	
def p_forblock_iterate_mult(p):
	'ForBlock : FOR OPARENTHESIS ID COLLON ID CPARENTHESIS OCURLYBRACKETS ListOps CCURLYBRACKETS'
	p[0] = [('for', (p[3],p[5], p[8]))]
	#print('ForBlock : FOR "(" ID ":" ID ")" "{" ListOps "}"')


"""
IfBlock : "if(" Condition ")" Op
		| "if(" Condition ")" "{" ListOps "}"
		| "if(" Condition ")" Op ElseBlock
		| "if(" Condition ")" "{" ListOps "}" ElseBlock
"""
def p_ifblock_ifsingle(p):
	'IfBlock : IF OPARENTHESIS Condition CPARENTHESIS Op'
	p[0] = [('if',(p[3],p[5],[]))]
	
def p_ifblock_ifmult(p):
	'IfBlock : IF OPARENTHESIS Condition CPARENTHESIS OCURLYBRACKETS ListOps CCURLYBRACKETS'
	p[0] = [('if',(p[3],p[6],[]))]
	
def p_ifblock_ifsingle_else(p):
	'IfBlock : IF OPARENTHESIS Condition CPARENTHESIS Op ElseBlock'
	p[0] = [('if',(p[3],p[5],p[6]))]
	
def p_ifblock_ifmult_else(p):
	'IfBlock : IF OPARENTHESIS Condition CPARENTHESIS OCURLYBRACKETS ListOps CCURLYBRACKETS ElseBlock'
	p[0] = [('if',(p[3],p[6],p[8]))]


"""
ElseBlock   : "else" Op
			| "else" "{" ListOps "}"
"""
def p_elseblock_single(p):
	'ElseBlock : ELSE Op'
	p[0] = p[2]
	
def p_elseblock_mult(p):
	'ElseBlock : ELSE OCURLYBRACKETS ListOps CCURLYBRACKETS'
	p[0] = p[3]


"""
Condition	: List
			| Dict
			| BoolExpression
"""
def p_condition_ID(p):
	'Condition : ID'
	p[0] = ('id',p[1])







def p_error(p):
	print("YACC ERROR!")