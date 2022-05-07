"""
/**
num i = 0.1;
str j = "";
list l = ["abc",1,"def",2];
dict d = ["abc":1,"def":2];

if(condition)
    for(element : list) {

        $text$element$text$; #same as printf("text %s text", element)

        //text
        /*
            text
        */
    }
else
    for(i = 0; i < 10; i = i + 1)
        j = j + i;
    
**/

if + else
for(;;)
for(:)
comments (//, /**/)
variable declaration (num & str & list & dictionary)
num operations (+, -, *,  /, //)
str operations (+str, +num, [::])
list operations (+value, -value, [::])
dict operations ([key], -key, [key] = value)
"""

import sys
import re
import ply.lex as lex
import ply.yacc as yacc
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


from lexer import *
from grammar1 import *






### lexer

lexer = lex.lex()

### yacc
    
parser = yacc.yacc()

### open files

f_template = open(sys.argv[1],'r')
f_yaml = open(sys.argv[2],'r')
f_output = open(sys.argv[3],'w')

### read files

content = f_template.read()
yaml_content = f_yaml.read()

### parse files

lexer.input(content)

dic = yaml.load(yaml_content, Loader=Loader)

ast = parser.parse(content)

### solve

print(dic ,end='\n\n\n')
print(ast, end='\n\n\n')

def format(string):
    symbols = {
        '\\n':'\n',
        '\\t':'\t',
        '\\"':'\"'
    }
    for symbol in symbols:
        string = string.replace(symbol,symbols[symbol])
    return string

def evaluate_bool_expression(condition,dic):
    cond_type = condition[0]

    if(cond_type == 'id'):
        return (dic.get(condition[1],None))

    if(cond_type == 'num'):
        return (condition[1] != 0)


    return False

def evaluate_expression(exp,dic):
    op_type = exp[0]

    if(op_type == 'id'):
        return dic.get(exp[1])

    if(op_type == 'num'):
        try:
            result = int(exp[1])
        except:
            result = float(exp[1])
        return result

    right = evaluate_expression(exp[1][0],dic)
    left = evaluate_expression(exp[1][1],dic)

    if(op_type == 'add'):
        return right + left

    if(op_type == 'sub'):
        return right - left

    if(op_type == 'mult'):
        return right * left

    if(op_type == 'div'):
        return right / left

    return None

level = -1
def solve(ast,dic,output):
    global level
    level = level + 1
    for op in ast:
        for i in range(0,level):
            print('\t',end='')
        print(op)
        op_type = op[0]

        if op_type == 'text':
            output.write(op[1])
        elif op_type == 'section':
            solve(op[1],dic,output)
        elif op_type == 'str':
            output.write(format(op[1]))
        elif op_type == 'id':
            output.write(str(dic[op[1]]))
        elif op_type == 'for':
            var,lst,ops = op[1]
            for element in dic[lst]:
                dic[var] = element
                solve(ops,dic,output)
            dic.pop(var)
        elif op_type == 'if':
            condition,ifops,elseops = op[1]
            if(evaluate_bool_expression(condition,dic)):
                solve(ifops,dic,output)
            else:
                solve(elseops,dic,output)
        elif op_type == 'assign':
            var,exp = op[1]
            dic[var] = evaluate_expression(exp,dic)
    level = level - 1

solve(ast,dic,f_output)
#print(dic ,end='\n\n\n')

### exit

f_template.close()
f_yaml.close()
f_output.close()