


"""
Sections    : Sections Section
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
Section : SECTIONBEGIN SectionContent SECTIONEND
"""
def p_section(p):
    'Section : SECTIONBEGIN SectionContent SECTIONEND'
    p[0] = p[2]


"""
SectionContent  : ListOps
"""
def p_sectioncontent(p):
    'SectionContent : ListOps'
    p[0] = p[1]


"""
ListOps : ListOps Op ";"
        | 
"""
def p_listops_op(p):
    'ListOps : ListOps Op ";"'
    p[0] = p[1] + p[2]

def p_listops_empty(p):
    'ListOps : '
    p[0] = []


"""
Op  : ForBlock
    | "$" FormattedStr
"""
def p_op_forblock(p):
    'Op : ForBlock'
    p[0] = p[1]

def p_op_formattedstr(p):
    'Op : FORMATTEDSTRINGDELIMITER FormattedStr'
    p[0] = p[2]


"""
FormattedStr    : FormattedStr STR "$"
                | FormattedStr ID "$"
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
ForBlock    : FOR "(" ID ":" ID ")" Op
            | FOR "(" ID ":" ID ")" "{" ListOps "}"
"""
def p_forblock_iterate_single(p):
    'ForBlock : FOR "(" ID ":" ID ")" Op'
    p[0] = [('for', (p[3],p[5], p[7]))]
    
def p_forblock_iterate_mult(p):
    'ForBlock : FOR "(" ID ":" ID ")" "{" ListOps "}"'
    p[0] = [('for', (p[3],p[5], p[8]))]

    
def p_error(p):
    print("YACC ERROR!")