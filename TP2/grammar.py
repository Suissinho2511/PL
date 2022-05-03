


"""
Sections    : Sections Section
            | Sections TEXT
            | 
"""
def p_sections_section(p):
    'Sections : Sections Section'

def p_sections_text(p):
    'Sections : Sections TEXT'

def p_sections_empty(p):
    'Sections : '


"""
Section : "/**" SectionContent "**/"
"""
def p_section(p):
    'Section : "/**" SectionContent "**/"'


"""
SectionContent  : ListOps
"""
def p_sectioncontent(p):
    'SectionContent : ListOps'


"""
ListOps : ListOps Op ";"
        | ListOps Comment
        | 
"""
def p_listops_op(p):
    'ListOps : ListOps Op ";"'

def p_listops_comment(p):
    'ListOps : ListOps Comment'

def p_listops_empty(p):
    'ListOps : '


"""
Op  : VarDeclaration
    | VarManipulation
    | IfBlock
    | ForBlock
    | FormattedStr
"""
def p_op_vardeclaration(p):
    'Op : VarDeclaration'

def p_op_varmanipulation(p):
    'Op : VarManipulation'

def p_op_ifblock(p):
    'Op : IfBlock'

def p_op_forblock(p):
    'Op : ForBlock'

def p_op_formattedstr(p):
    'Op : FormattedStr'


"""
VarDeclaration  : Type ID
                | Type ID "=" Var
"""
def p_vardeclaration_novalue(p):
    'VarDeclaration : Type ID'

def p_vardeclaration_value(p):
    'VarDeclaration : Type ID "=" Var'


"""
Type    : "num" | "str" | "list" | "dict"
"""
def p_type_num(p):
    'Type : "num"'

def p_type_str(p):
    'Type : "str"'

def p_type_list(p):
    'Type : "list"'

def p_type_dict(p):
    'Type : "dict"'


"""
Var : Expression | STR | List | Dict
"""
def p_var_expression(p):
    'Var : Expression'

def p_var_str(p):
    'Var : STR'

def p_var_list(p):
    'Var : List'

def p_var_dict(p):
    'Var : Dict'


"""
FormattedStr    : FormattedStr "$" STR "$"
                | FormattedStr "$" ID "$"
                | 
"""
def p_formattedstr_str(p):
    'FormattedStr : FormattedStr "$" STR "$"'

def p_formattedstr_id(p):
    'FormattedStr : FormattedStr "$" ID "$"'

def p_formattedstr_empty(p):
    'FormattedStr : '


"""
List    : "[" ListElements "]"
"""
def p_list(p):
    'List : "[" ListElements "]"'


"""
ListElements    : ListElements "," Var
                | 
"""
def p_listelements_element(p):
    'ListElements : ListElements "," Var'

def p_listelements_empty(p):
    'ListElements : '


"""
Dict    : "[" ListEntries "]"
"""
def p_dict(p):
    'Dict : "[" ListEntries "]"'


"""
ListEntries : ListEntries "," STR ":" Var
            | 
"""
def p_listentries_entry(p):
    'ListEntries : ListEntries "," STR ":" Var'

def p_listentries_empty(p):
    'ListEntries : '


"""
VarManipulation : Left "=" Right
"""
def p_varmanipulation(p):
    'VarManipulation : Left "=" Right'


"""
Left    : ID
        | ID "[" TEXT "]"
        | ID "[" NUM "]"
"""
def p_left_id(p):
    'Left : ID'
    
def p_left_dict(p):
    'Left : ID "[" TEXT "]"'
    
def p_left_list(p):
    'Left : ID "[" NUM "]"'


"""
OP  : "+"
    | "-"
    | "*"
    | "/"
"""
def p_op_plus(p):
    'OP : "+"'
    
def p_op_minus(p):
    'OP : "-"'
    
def p_op_mult(p):
    'OP : "*"'
    
def p_op_div(p):
    'OP : "/"'


"""
Right   : Expression
        | STR
        | List
        | Dict
"""
def p_right_expression(p):
    'Right : Expression'
    
def p_right_str(p):
    'Right : STR'
    
def p_right_list(p):
    'Right : List'
    
def p_right_dict(p):
    'Right : Dict'


"""
IfBlock : "if(" Condition ")" Op
        | "if(" Condition ")" "{" ListOps "}"
        | "if(" Condition ")" Op ElseBlock
        | "if(" Condition ")" "{" ListOps "}" ElseBlock
"""
def p_ifblock_ifsingle(p):
    'IfBlock : "if(" Condition ")" Op'
    
def p_ifblock_ifmult(p):
    'IfBlock : "if(" Condition ")" "{" ListOps "}"'
    
def p_ifblock_ifsingle_else(p):
    'IfBlock : "if(" Condition ")" Op ElseBlock'
    
def p_ifblock_ifmult_else(p):
    'IfBlock : "if(" Condition ")" "{" ListOps "}" ElseBlock'


"""
ElseBlock   : "else" Op
            | "else" "{" ListOps "}"
"""
def p_elseblock_single(p):
    'ElseBlock : "else" Op'
    
def p_elseblock_mult(p):
    'ElseBlock : "else" "{" ListOps "}"'
    

"""
ForBlock    : "for(" ID ":" ID ")" Op
            | "for(" ID ":" ID ")" "{" ListOps "}"
            | "for(" ListVarDeclaration ";" Condition ";" ListVarManipulation ")" Op
            | "for(" ListVarDeclaration ";" Condition ";" ListVarManipulation ")" "{" ListOps "}"
"""
def p_forblock_iterate_single(p):
    'ForBlock : "for(" ID ":" ID ")" Op'
    
def p_forblock_iterate_mult(p):
    'ForBlock : "for(" ID ":" ID ")" "{" ListOps "}"'
    
def p_forblock_loop_single(p):
    'ForBlock : "for(" ListVarDeclaration ";" Condition ";" ListVarManipulation ")" Op'
    
def p_forblock_loop_mult(p):
    'ForBlock : "for(" ListVarDeclaration ";" Condition ";" ListVarManipulation ")" "{" ListOps "}"'


"""
Comment : "//" COMMENTLINE
        | "/*" COMMENTBLOCK "*/"
"""
def p_comment_single(p):
    'Comment : "//" COMMENTLINE'
    
def p_comment_mult(p):
    '"/*" COMMENTBLOCK "*/"'


"""
Expression : ...
"""
def p_expression_plus(p):
    'Expression : Expression "+" Term'
    p[0] = p[1] + p[3]
    
def p_expression_minus(p):
    'Expression : Expression "-" Term'
    p[0] = p[1] - p[3]
    
def p_expression_term(p):
    'Expression : Term'
    p[0] = p[1]
    
def p_term_mult(p):
    'Term : Term "*" Factor'
    p[0] = p[1] * p[3]
    
def p_term_div(p):
    'Term : Term "/" Factor'
    p[0] = p[1] / p[3]
    
def p_term_factor(p):
    'Term : Factor'
    p[0] = p[1]
    
def p_factor_expression(p):
    'Factor : "(" Expression ")"'
    p[0] = p[2]
    
def p_factor_num(p):
    'Factor : NUM'
    try:
        p[0] = int(p[1])
    except:
        p[0] = float(p[1])
    
def p_factor_id(p):
    'Factor : ID'
    if p[1] in p.parser.symtab:
        p[0] = p.parser.symtab[p[1]]['value']
    else:
        print(f"Variable {p[1]} not defined!")
    
def p_error(p):
    print("YACC ERROR!")