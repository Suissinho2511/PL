
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