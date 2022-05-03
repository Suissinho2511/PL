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

print(ast)

def format(string):
    symbols = {
        '\\n':'\n',
        '\\t':'\t',
        '\\"':'\"'
    }
    for symbol in symbols:
        string = string.replace(symbol,symbols[symbol])
    return string

def solve(ast,dic,output):
    for op in ast:
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
            v,l,ops = op[1]
            for element in dic[l]:
                dic[v] = element
                solve(ops,dic,output)
            dic.pop(v)

solve(ast,dic,f_output)

print(dic)

### exit

f_template.close()
f_yaml.close()
f_output.close()