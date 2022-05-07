


"""
Sections	: Sections Section
			| Sections TEXT
			| 
"""
def p_sections_section(p):
	'Sections : Sections Section'
	p[0] = p[1] + [('section', p[2])]

def p_sections_text(p):
	'Sections : Sections TEXT'
	p[0] = p[1] + [('text', p[2])]

def p_sections_empty(p):
	'Sections : '
	p[0] = []


"""
Section	: /=== SectionContent ===/
"""
def p_section(p):
	'Section : SECTIONBEGIN SectionContent SECTIONEND'
	p[0] = p[2]


"""
SectionContent	: ListOps
"""
def p_sectioncontent(p):
	'SectionContent : ListOps'
	p[0] = p[1]


"""
ListOps	: ListOps Op
		| 
"""
def p_listops_op(p):
	'ListOps : ListOps Op'
	p[0] = p[1] + p[2]

def p_listops_empty(p):
	'ListOps : '
	p[0] = []


"""
Op	: ForBlock
	| $ FormattedStr ;
	| IfBlock

	| VarManipulation ;
	| while
"""
def p_op_forblock(p):
	'Op : ForBlock'
	p[0] = p[1]

def p_op_formattedstr(p):
	'Op : FORMATTEDSTRINGDELIMITER FormattedStr SEMICOLLON'
	p[0] = p[2]

def p_op_ifblock(p):
	'Op : IfBlock'
	p[0] = p[1]

def p_op_varmanipulation(p):
	'Op : VarManipulation SEMICOLLON'
	p[0] = p[1]

def p_op_while(p):
	'Op : WhileBlock'
	p[0] = p[1]


"""
FormattedStr	: FormattedStr STR $
				| FormattedStr ID $
				| FormattedStr NUM $
				|
"""
def p_formattedstr_str(p):
	'FormattedStr : FormattedStr STR FORMATTEDSTRINGDELIMITER'
	p[0] = p[1] + [('str', p[2])]

def p_formattedstr_id(p):
	'FormattedStr : FormattedStr ID FORMATTEDSTRINGDELIMITER'
	p[0] = p[1] + [('id', p[2])]

def p_formattedstr_empty(p):
	'FormattedStr : '
	p[0] = []


"""
ForBlock	: for ( ID : ID ) Op
			| for ( ID : ID ) { ListOps }
"""
def p_forblock_iterate_single(p):
	'ForBlock : FOR OPARENTHESIS ID COLLON ID CPARENTHESIS Op'
	p[0] = [('for', (p[3],p[5], p[7]))]
	
def p_forblock_iterate_mult(p):
	'ForBlock : FOR OPARENTHESIS ID COLLON ID CPARENTHESIS OCURLYBRACKETS ListOps CCURLYBRACKETS'
	p[0] = [('for', (p[3],p[5], p[8]))]


"""
IfBlock	: if ( Condition ) Op
		| if ( Condition ) { ListOps }
		| if ( Condition ) Op ElseBlock
		| if ( Condition ) { ListOps } ElseBlock
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
ElseBlock	: else Op
			| else { ListOps }
"""
def p_elseblock_single(p):
	'ElseBlock : ELSE Op'
	p[0] = p[2]
	
def p_elseblock_mult(p):
	'ElseBlock : ELSE OCURLYBRACKETS ListOps CCURLYBRACKETS'
	p[0] = p[3]


"""
Condition	: BoolExpression
"""
def p_condition_ID(p):
	'Condition : ID'
	p[0] = ('id',p[1])


"""
VarManipulation : ID = Expression
"""
#def p_varmanipulation(p):
#	'VarManipulation : ID EQUAL Expression'
#	print('VarManipulation : ID EQUAL Expression')
#	p[0] = [('assign',(p[1],p[3]))]
#	print(p[0])

def p_varmanipulation(p):
	'VarManipulation : ID EQUAL Expression'
	p[0] = [('assign',(p[1],p[3]))]


"""
Expression : ...
"""
def p_expression_plus(p):
	'Expression : Expression PLUS Term'
	p[0] = ('add',(p[1],p[3]))
	
def p_expression_minus(p):
	'Expression : Expression MINUS Term'
	p[0] = ('sub',(p[1],p[3]))
	
def p_expression_term(p):
	'Expression : Term'
	p[0] = p[1]
	
def p_term_mult(p):
	'Term : Term MULT Factor'
	p[0] = ('mult',(p[1],p[3]))
	
def p_term_div(p):
	'Term : Term DIV Factor'
	p[0] = ('div',(p[1],p[3]))
	
def p_term_factor(p):
	'Term : Factor'
	p[0] = p[1]
	
def p_factor_expression(p):
	'Factor : OPARENTHESIS Expression CPARENTHESIS'
	p[0] = p[2]
	
def p_factor_num(p):
	'Factor : NUM'
	p[0] = ('num',p[1])
	
def p_factor_id(p):
	'Factor : ID'
	p[0] = ('id',p[1])


"""
WhileBlock	: WHILE OPARENTHESIS BoolExpression CPARENTHESIS Op
			| WHILE OPARENTHESIS BoolExpression CPARENTHESIS OCURLYBRACKETS ListOps CCURLYBRACKETS
"""
def p_whileblock_single(p):
	'WhileBlock : WHILE OPARENTHESIS Condition CPARENTHESIS Op'

def p_whileblock_mult(p):
	'WhileBlock : WHILE OPARENTHESIS Condition CPARENTHESIS OCURLYBRACKETS ListOps CCURLYBRACKETS'





def p_error(p):
	print("YACC ERROR!")