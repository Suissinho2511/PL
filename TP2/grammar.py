

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
	| WhileBlock
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
FormattedStr	: FormattedStr Expression $
				|
"""


def p_formattedstr_exp(p):
    'FormattedStr : FormattedStr Expression FORMATTEDSTRINGDELIMITER'
    p[0] = p[1] + [('exp', p[2])]


def p_formattedstr_empty(p):
    'FormattedStr : '
    p[0] = []


"""
ForBlock	: for ( ID : ID ) Op
			| for ( ID : ID ) { ListOps }
"""


def p_forblock_iterate_single(p):
    'ForBlock : FOR OPARENTHESIS ID COLLON ID CPARENTHESIS Op'
    p[0] = [('for', (p[3], p[5], p[7]))]


def p_forblock_iterate_mult(p):
    'ForBlock : FOR OPARENTHESIS ID COLLON ID CPARENTHESIS OCURLYBRACKETS ListOps CCURLYBRACKETS'
    p[0] = [('for', (p[3], p[5], p[8]))]


"""
IfBlock	: if ( BoolExpression ) Op
		| if ( BoolExpression ) { ListOps }
		| if ( BoolExpression ) Op ElseBlock
		| if ( BoolExpression ) { ListOps } ElseBlock
"""


def p_ifblock_ifsingle(p):
    'IfBlock : IF OPARENTHESIS BoolExpression CPARENTHESIS Op'
    p[0] = [('if', (p[3], p[5], []))]


def p_ifblock_ifmult(p):
    'IfBlock : IF OPARENTHESIS BoolExpression CPARENTHESIS OCURLYBRACKETS ListOps CCURLYBRACKETS'
    p[0] = [('if', (p[3], p[6], []))]


def p_ifblock_ifsingle_else(p):
    'IfBlock : IF OPARENTHESIS BoolExpression CPARENTHESIS Op ElseBlock'
    p[0] = [('if', (p[3], p[5], p[6]))]


def p_ifblock_ifmult_else(p):
    'IfBlock : IF OPARENTHESIS BoolExpression CPARENTHESIS OCURLYBRACKETS ListOps CCURLYBRACKETS ElseBlock'
    p[0] = [('if', (p[3], p[6], p[8]))]


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
BoolExpression : ...
"""


def p_boolexpression_or(p):
    'BoolExpression : BoolExpression OR BoolTerm'
    p[0] = ('or', (p[1], p[3]))


def p_boolexpression_and(p):
    'BoolExpression : BoolExpression AND BoolTerm'
    p[0] = ('and', (p[1], p[3]))


def p_boolexpression_boolterm(p):
    'BoolExpression : BoolTerm'
    p[0] = p[1]


def p_boolterm_gt(p):
    'BoolTerm : Expression GT Expression'
    p[0] = ('>', (p[1], p[3]))


def p_boolterm_lt(p):
    'BoolTerm : Expression LT Expression'
    p[0] = ('<', (p[1], p[3]))


def p_boolterm_ge(p):
    'BoolTerm : Expression GE Expression'
    p[0] = ('>=', (p[1], p[3]))


def p_boolterm_le(p):
    'BoolTerm : Expression LE Expression'
    p[0] = ('<=', (p[1], p[3]))


def p_boolterm_eq(p):
    'BoolTerm : Expression EQ Expression'
    p[0] = ('==', (p[1], p[3]))


def p_boolterm_neq(p):
    'BoolTerm : Expression NEQ Expression'
    p[0] = ('!=', (p[1], p[3]))


def p_boolterm_boolfactor(p):
    'BoolTerm : BoolFactor'
    p[0] = p[1]


def p_boolterm_notboolfactor(p):
    'BoolTerm : NOT BoolTerm'
    #'BoolTerm : NOT BoolFactor'
    p[0] = ('not', p[2])


def p_boolfactor_boolexpression(p):
    'BoolFactor : OPARENTHESIS BoolExpression CPARENTHESIS'
    p[0] = p[2]


def p_boolfactor_id(p):
    'BoolFactor : ID'
    p[0] = ('id', p[1])


"""
VarManipulation : ID = Expression
"""


def p_varmanipulation(p):
    'VarManipulation : ID EQUAL Expression'
    p[0] = [('assign', (p[1], p[3]))]


"""
Expression : ...
"""


def p_expression_plus(p):
    'Expression : Expression PLUS Term'
    p[0] = ('add', (p[1], p[3]))


def p_expression_minus(p):
    'Expression : Expression MINUS Term'
    p[0] = ('sub', (p[1], p[3]))


def p_expression_plus_single(p):
    'Expression : PLUS Term'
    p[0] = ('add', (('num', 0), p[2]))


def p_expression_minus_single(p):
    'Expression : MINUS Term'
    p[0] = ('sub', (('num', 0), p[2]))


def p_expression_term(p):
    'Expression : Term'
    p[0] = p[1]


def p_term_mult(p):
    'Term : Term MULT Factor'
    p[0] = ('mult', (p[1], p[3]))


def p_term_div(p):
    'Term : Term DIV Factor'
    p[0] = ('div', (p[1], p[3]))


def p_term_factor(p):
    'Term : Factor'
    p[0] = p[1]


def p_factor_expression(p):
    'Factor : OPARENTHESIS Expression CPARENTHESIS'
    p[0] = p[2]


def p_factor_num(p):
    'Factor : NUM'
    p[0] = ('num', p[1])


def p_factor_id(p):
    'Factor : ID'
    p[0] = ('id', p[1])


def p_factor_index(p):
    'Factor : ID OSQUAREBRACKETS Expression CSQUAREBRACKETS'
    p[0] = ('index', (p[1], p[3]))


def p_factor_str(p):
    'Factor : STR'
    p[0] = ('str', p[1])


"""
WhileBlock	: while ( BoolExpression ) Op
			| while ( BoolExpression ) { ListOps }
"""


def p_whileblock_single(p):
    'WhileBlock : WHILE OPARENTHESIS BoolExpression CPARENTHESIS Op'
    p[0] = [('while', (p[3], p[5]))]


def p_whileblock_mult(p):
    'WhileBlock : WHILE OPARENTHESIS BoolExpression CPARENTHESIS OCURLYBRACKETS ListOps CCURLYBRACKETS'
    p[0] = [('while', (p[3], p[6]))]







def p_error(p):
    print("YACC ERROR!")