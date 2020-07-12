#!/usr/bin/env python3

import sys
import ply.lex as lex
import ply.yacc as yacc


class Node():
    def __init__(self):
        self.parent = None

    def parentCount(self):
        count = 0
        current = self.parent
        while current is not None:
            count += 1
            current = current.parent
        return count

class Assignment(Node):
    def __init__(self, lvalue, rvalue):
        super().__init__()
        self.lvalue = lvalue
        self.rvalue = rvalue
        self.lvalue.parent = self
        self.rvalue.parent = self
        
    def eval(self):
        pass
        
    def __str__(self):
        res = "\t" * self.parentCount() + "Assignment"
        res += "\n" + str(self.lvalue)
        res += "\n" + str(self.rvalue)
        return res
    
class Not(Node):
    def __init__(self, child):
        super().__init__()
        self.child = child
        self.child.parent = self

    def eval(self):
        if (type(self.child.eval()) is bool):
            v = not self.child.eval()
        else:
            print("SEMANTIC ERROR")
            sys.exit()
        
        return v

    def __str__(self):
        res = "\t" * self.parentCount() + "Not"
        res += "\n" + str(self.child)
        return res
    
class AST_True(Node):
    def __init__(self):
        super().__init__()
        self.value = True

    def eval(self):
        return self.value

    def __str__(self):
        res = "\t" * self.parentCount() + "True"
        return res

class AST_False(Node):
    def __init__(self):
        super().__init__()
        self.value = False

    def eval(self):
        return self.value

    def __str__(self):
        res = "\t" * self.parentCount() + "False"
        return res
    
class And(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(x)) is type(y) and (type(x) is bool):
            return x and y
        else:
            print("SEMANTIC ERROR")
            sys.exit()

    def __str__(self):
        res = "\t" * self.parentCount() + "Andalso"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res

class Or(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self

    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(x)) is type(y) and (type() is bool):
            return x or y
        else:
            print("SEMANTIC ERROR")
            sys.exit()

    def __str__(self):
        res = "\t" * self.parentCount() + "Orelse"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
      
    
class Number(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value
        
    def eval(self):
        return self.value
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Number"
        return res
    
class Real(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value
        
    def eval(self):
        return self.value
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Real"
        return res

class Plus(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if(type(x) is type(y) and (type(x) is list or str)):
            return x + y
        elif (type(y) is int) or (type(y) is float):
            if (type(x) is int) or (type(x) is float):
                return x + y
        else:
            print("SEMANTIC ERROR")
            sys.exit()
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Plus"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
        
class Minus(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if(type(x) is int or float and (type(y) is int or float)):
            return x - y
        else:
            print("SEMANTIC ERROR")
            sys.exit()
        
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Minus"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
class Times(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if(type(x) is int or float and (type(y) is int or float)):
            return x * y
        else:
            print("SEMANTIC ERROR")
            sys.exit()
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Times"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
class Intdivision(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(x) is type(y)) and (type(x) is int) and (y != 0):
            return int(x / y)
        else:
            print("SEMANTIC ERROR")
            sys.exit()
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Intdivision"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
    
class Exponent(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        return pow(self.left.eval(), self.right.eval())
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Exponent"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
    
class String(Node):
    def __init__(self, value):
        super().__init__()
        self.value = str(value)
        
    def eval(self):
        return self.value
    
    def __str__(self):
        res = "\t" * self.parentCount() + "String"
        return res
 
class Lessthan(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(x) is type(y)) and (type(x) is int or float or str):
            v = x < y
        else:
            print("SEMANTIC ERROR")
            sys.exit()
        return v
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Lessthan"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
class Greaterthan(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(x) is type(y)) and (type(x) is int or float or str):
            v = x > y
        else:
            print("SEMANTIC ERROR")
            sys.exit()
        return v
    
    def __str__(self):
        res = "\t" * self.parentCount() + "GreaterThan"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
class LEQ(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(x) is type(y)) and (type(x) is int or float or str):
            v = x <= y
        else:
            print("SEMANTIC ERROR")
            sys.exit()
        return v
    
    def __str__(self):
        res = "\t" * self.parentCount() + "LEQ"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res

class GEQ(Node):
    
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(x) is type(y)) and (type(x) is int or float or str):
            return x >= y
        else:
            print("SEMANTIC ERROR")
            sys.exit()
    
    def __str__(self):
        res = "\t" * self.parentCount() + "GEQ"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
class EqualTo(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(x) is type(y)) and (type(x) is int or float or str):
            return (x == y)
        else:
            print("SEMANTIC ERROR")
            sys.exit()
    
    def __str__(self):
        res = "\t" * self.parentCount() + "EqualTO"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
class NEQ(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(x) is type(y)) and (type(x) is int or float or str):
            return x != y
        else:
            print("SEMANTIC ERROR")
            sys.exit()
    
    def __str__(self):
        res = "\t" * self.parentCount() + "NEQ"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
class Uminus(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value
        
    def eval(self):
        return -self.value
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Uminus"
        return res
    
class Division(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(x) is int or float) and (type(y) is int or float) and (y != 0):
            v = float(x / y)
        else:
            print("SEMANTIC ERROR")
            sys.exit()
        return v
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Division"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
class Modulus(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(x) is type(y)) and (type(x) is int or float):
            v = x % y
        else:
            print("SEMANTIC ERROR")
            sys.exit()
        return v
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Modulus"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res

class List(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        x = []
        for item in self.value:
            x.append(item.eval())
        return x
    
    
    def __str__(self):
        res = "\t" * self.parentCount() + "List"
        return res
   
class Cons(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        #self.right.parent = self
        
    def eval(self): 
        x = self.right.eval()
        y = [self.left.eval()] + x
        return y

    
    def __str__(self):
        res = "\t" * self.parentCount() + "Cons"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res

class In(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if (type(y) is list or str):
            return x in y
        else:
            print("SEMANTIC ERROR")
            sys.exit() 
    
    def __str__(self):
        res = "\t" * self.parentCount() + "In"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
class Index(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        if type(self.left) is not list and type(self.left) is not str:
            self.left.parent = self
        self.right.parent = self
        
    def eval(self):
        x = self.left.eval()
        y = self.right.eval()
        if type(y) is int:
            if type(self.left) is list:
                try:
                    v =  (self.left)[y]
                    v = v.eval()
                except IndexError:
                    print("SEMANTIC ERROR")
                    sys.exit() 
            elif (isinstance(self.left, Index)):
                try:
                    v = (self.left.eval())[y]
                except IndexError:
                    print("SEMANTIC ERROR")
            elif (type(self.left) is str):
                strin = self.left
                strin = strin.strip('\"')
                try:
                    v =  (strin)[y]
                except IndexError:
                    print("SEMANTIC ERROR")
                    sys.exit() 
            elif (type(x) is str):
                try:
                    v =  (self.left.eval())[y]
                except IndexError:
                    print("SEMANTIC ERROR1")
                    sys.exit() 
            elif (type(x) is list):
                v = (x)[y]
            #elif ():
                #return
        else:
            print("SEMANTIC ERROR")
            sys.exit() 
        
        return v
          
    def __str__(self):
        res = "\t" * self.parentCount() + "Index"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
class Tuple(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        x = []
        for item in self.value:
            x.append(item.eval())
        return tuple(x)
    
    def __str__(self):
        res = "\t" * self.parentCount() + "Tuple"
        return res
    
class Print(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value
        
    def eval(self):
        print(self.value.eval())
        
    def __str__(self):
        res = "\t" * self.parentCount() + "Tuple"
        return res

class TupleIndex(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right
        self.left.parent = self
        #self.right.parent = self
        
    def eval(self):
        x = []
        #print(type(self.right.eval()))
        for item in self.right.eval():
            x.append(item)
            
        try:
            v =  (x)[self.left.eval() - 1]
        except IndexError:
            print("SEMANTIC ERROR")
            sys.exit() 
                
        return v
    
    def __str__(self):
        res = "\t" * self.parentCount() + "TupleIndex"
        res += "\n" + str(self.left)
        res += "\n" + str(self.right)
        return res
    
class Assign(Node):
    def __init__(self, variable, value):
        super().__init__()
        self.value = value
        self.variable = variable
        
    def eval(self):
        x = self.value.eval()
        if type(self.variable) is list:
            (names[self.variable[0]])[self.variable[1].eval()]  = x
            return
        elif type(x) is list:
            names[self.variable] = x
            return
        else:
            names[self.variable] = x
            return
        
    def __str__(self):
        res = "\t" * self.parentCount() + "Assignment"
        return res
   
   
class VariableName(Node):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def eval(self):
        if self.name in names:
            return names[self.name]
        else:
            print("SEMANTIC ERROR")
            sys.exit()

    def __str__(self):
        res = "\t" * self.parentCount() + "Variable: " + self.name
        if self.name in names:
            res += " : " + str(names[self.name])
        else:
            res += " : " + "True"
        return res

class Block(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value
        
    def eval(self):
        for item in self.value: 
            item.eval()
        return
        
    def __str__(self):
        res = "\t" * self.parentCount() + "Block"
        return res
    
class Conditional(Node):
    def __init__(self, conditional, value):
        super().__init__()
        self.value = value
        self.conditional = conditional
        
    def eval(self):
        if (self.conditional.eval()):
            self.value.eval()
            return
        else:
            return
        
    def __str__(self):
        res = "\t" * self.parentCount() + "Conditional"
        return res
    
class ConditionalElse(Node):
    def __init__(self, conditional, conditionalvalue, value):
        super().__init__()
        self.value = value
        self.conditional = conditional
        self.conditionalvalue = conditionalvalue
        
    def eval(self):        
        if (self.conditional.eval()):
            return self.conditionalvalue.eval() 
        else:
            return self.value.eval()
        
    def __str__(self):
        res = "\t" * self.parentCount() + "ConditionalElse"
        return res
    

class Loop(Node):
    def __init__(self, conditional, value):
        super().__init__()
        self.value = value
        self.conditional = conditional
        
    def eval(self):
        while(self.conditional.eval()):
            self.value.eval()
        
    def __str__(self):
        res = "\t" * self.parentCount() + "Loop"
        return res

class FunctionDef(Node):
    def __init__(self, name, var, value, output):
        super().__init__()
        self.name = name
        self.var = var
        self.value = value
        self.output = output
        
    def eval(self):
        funcnames[self.name] = [self.value, self.var, self.output]
        
    def __str__(self):
        res = "\t" * self.parentCount() + "FunctionDef"
        return res
    
class FunctionCall(Node):
    def __init__(self, name, var):
        super().__init__()
        self.name = name
        self.var = var
        
    def eval(self):
        if self.name not in funcnames:
            print("SEMANTIC ERROR")
            sys.exit()
        
        for item in self.var:
            stack.append(item.eval())                  #push variables to stack in case of recursive function call
        
        functionName = funcnames[self.name]     #set function name aside 
        blockVal = functionName[0]              #set block aside
        variableNames = functionName[1]         #set variable name(s) aside
        outputVar = functionName[2]             #set output variable aside     
        
        if len(variableNames) != len(self.var):
            print("SEMANTIC ERROR")
            sys.exit() 

        count = 0                   #set variables for block evaluation
        for x in range(len(variableNames) - 1, -1, -1):
            names[variableNames[x]] = stack[len(stack) - 1 - count]
            count += 1
        
        try:
            blockVal.eval()                     #evaluate block
        except:
            pass


        for x in range(len(variableNames) - 1, -1, -1):
            stack.pop()
            try:
                names[variableNames[x]] = stack[len(stack) - x - 2]
            except:
                pass
                
        return outputVar.eval()
        
        
    def __str__(self):
        res = "\t" * self.parentCount() + "FunctionCall"
        return res


class funcVarList(Node):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def eval(self):
        x = []
        for item in self.value:
            x.append(item.eval())
        return x
    
    def __str__(self):
        res = "\t" * self.parentCount() + "FuncVarList"
        return res

reserved = {
        'andalso' : 'AND',
        'False' : 'FALSE',
        'True' : 'TRUE',
        'orelse' : 'OR',
        'not' : 'NOT',
        'mod' : 'MOD',
        'in' : 'IN',
        'div' : 'INTDIVIDE',
        'print' : 'PRINT',
        'if' : 'IF',
        'else' : 'ELSE',
        'while' : 'WHILE',
        'fun' : 'FUN',
        }


tokens = [
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVISION',
   'LPAREN',
   'RPAREN',
   'EXPONENT',
   'REAL',
   'SCINOT',
   'STRING',
   'STRING1',
   'NAME',
   'EQUALS',
   'EQUALTO',
   'LT',
   'GT',
   'LEQ',
   'GEQ',
   'NEQ',
   'COMMA',
   'LBRACKET',
   'RBRACKET',
   'CONS',
   'TUPLEINDX',
   'SEMICOLON',
   'LBLOCK',
   'RBLOCK',
] + list(reserved.values())


t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVISION= r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EXPONENT= r'\*\*'
t_EQUALS  = r'='
t_STRING  = r'\'(.*?)\''
t_STRING1 = r'"(.*?)"'
t_LT      = r'<'
t_GT      = r'>'
t_LEQ     = r'<='
t_GEQ     = r'>='
t_NEQ     = r'<>'
t_EQUALTO = r'=='
t_LBRACKET= r'\['
t_RBRACKET= r'\]'
t_COMMA   = r','
t_CONS    = r'::'
t_TUPLEINDX= r'\#'
t_SEMICOLON = r';'
t_LBLOCK  = r'\{'
t_RBLOCK  = r'\}'
 

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if (t.value in reserved.keys()):
        t.type = reserved.get(t.value)
    return t

def t_SCINOT(t):
    r'\d*\.\d+[e][-]?\d+'
    t.value = float(t.value)   
    return t

def t_REAL(t):
    r'\d*\.\d*'
    t.value = float(t.value)   
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)   
    return t

def t_TRUE(t):
    r'True'
    t.value = True
    return t

def t_FALSE(t):
    r'False'
    t.value = False
    return t


def t_error(t):
    print("SYNTAX ERROR")
    sys.exit()

# Ignore whitespace
t_ignore = ' \t'

# Count newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# Build lexer
lexer = lex.lex(debug = 0)

def tokenize(inp):
    lexer.input(inp)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'NOT'),
        ('left', 'LT'),
        ('left', 'LEQ'),
        ('left', 'EQUALTO'),
        ('left', 'NEQ'),
        ('left', 'GEQ'),
        ('left', 'GT'),
        ('right', 'CONS'),
        ('left', 'IN'),
        ('left','PLUS','MINUS'),
        ('left','TIMES','INTDIVIDE', 'DIVISION', 'MOD'),
        ('right', 'EXPONENT'),
        ('left', 'TUPLEINDX'),
        ('right', 'UMINUS'),
        ('left','LPAREN','RPAREN'),
    )

names = {}
funcnames = {}
stack = []

    
def p_fileparser(p):
    'program : sections'
    p[0] = p[1]  
    
def p_sections(p):
    '''
    sections : sections section
             | section
    '''
    if (len(p) == 2):
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_section(p):
    '''
    section : block
            | function

    '''
    p[0] = p[1]
    
def p_expression_name(p):
    'expression : NAME'
    p[0] = VariableName(p[1])
    
def p_expression_num(p):
     'expression : NUMBER'
     p[0] = Number(p[1])   
     
def p_expression_real(p):
    'expression : REAL'
    p[0] = Real(p[1])
    
def p_expression_scinot(p):
    'expression : SCINOT'
    p[0] = Real(p[1])
    
def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = Plus(p[1], p[3])

def p_expression_minus(p):
     'expression : expression MINUS expression'
     p[0] = Minus(p[1], p[3])
     
def p_expression_uminus(p):
    '''
    expression : MINUS NUMBER %prec UMINUS
               | MINUS REAL %prec UMINUS
    '''
    p[0] = Uminus(p[2])

def p_term_times(p):
     'expression : expression TIMES expression'
     p[0] = Times(p[1], p[3])
 
def p_int_division(p):
    'expression : expression INTDIVIDE expression'
    p[0] = Intdivision(p[1], p[3])
    
def p_division(p):
    'expression : expression DIVISION expression'
    p[0] = Division(p[1], p[3])
    
def p_expression_modulus(p):
    'expression : expression MOD expression'
    p[0] = Modulus(p[1], p[3])
    
def p_true(p):
    'expression : TRUE'
    p[0] = AST_True()

def p_false(p):
    'expression : FALSE'
    p[0] = AST_False()
    
def p_boolean_and(p):
    'expression : expression AND expression'
    p[0] = And(p[1], p[3])
    
def p_boolean_or(p):
    'expression : expression OR expression'
    p[0] = Or(p[1], p[3])

def p_boolean_not(p):
    'expression : NOT expression'
    p[0] = Not(p[2])

def p_parenthetical(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]        
    
def p_expression_exponent(p):
    'expression : expression EXPONENT expression'
    p[0] = Exponent(p[1], p[3])  
    
def p_string(p):
    'expression : STRING'
    p[0] = String(p[1][1:-1])
    
def p_string1(p):
    'expression : STRING1'
    p[0] = String(p[1][1:-1])
    
def p_lessthan(p):
    'expression : expression LT expression'
    p[0] = Lessthan(p[1], p[3])
    
def p_greaterthan(p):
    'expression : expression GT expression'
    p[0] = Greaterthan(p[1], p[3])

def p_leq(p):
    'expression : expression LEQ expression'
    p[0] = LEQ(p[1], p[3])

def p_geq(p):
    'expression : expression GEQ expression'
    
def p_equalto(p):
    'expression : expression EQUALTO expression'
    p[0] = EqualTo(p[1], p[3])

def p_neq(p):
    'expression : expression NEQ expression'
    p[0] = NEQ(p[1], p[3])

def p_index(p):
    '''
    expression : expression LBRACKET expression RBRACKET
               | list LBRACKET expression RBRACKET
               | STRING LBRACKET expression RBRACKET
               | STRING1 LBRACKET expression RBRACKET
    '''
    p[0] = Index(p[1], p[3]) 

def p_list(p):
    'list : LBRACKET RBRACKET'
    p[0] = []

def p_list2(p):
    '''
    list : LBRACKET expression COMMA
         | LBRACKET expression RBRACKET
    '''
    p[0] = [p[2]]

def p_list3(p):
    '''
    list : list expression RBRACKET
         | list expression COMMA
    '''
    p[0] = p[1] + [p[2]]

def p_list_expression(p):
    'expression : list'
    p[0] = List(p[1])
    
    
def p_cons(p):
    'expression : expression CONS expression'
    p[0] = Cons(p[1], p[3])
    
def p_in(p):
    'expression : expression IN expression'
    p[0] = In(p[1], p[3])
    
def p_tuple(p):
    '''
    tuple : LPAREN expression COMMA RPAREN
          | LPAREN expression COMMA
    '''
    p[0] = [p[2]]

def p_tuple1(p):
    'tuple : tuple expression COMMA'
    p[0] = p[1] + [p[2]]

def p_tuple2(p):
    '''
    tuple : tuple expression RPAREN
          | tuple expression COMMA RPAREN
    '''
    p[0] = p[1] + [p[2]]
    
def p_tuple3(p):
    'expression : tuple'
    p[0] = Tuple(p[1])
    
def p_tuple_index(p):
    'expression : TUPLEINDX expression expression'
    p[0] = TupleIndex(p[2], p[3])
    
def p_print(p):
    'print : PRINT LPAREN expression RPAREN SEMICOLON'
    p[0] = Print(p[3])

def p_assign(p):
    '''
    assignment : NAME EQUALS expression SEMICOLON
               | NAME LBRACKET expression RBRACKET EQUALS expression SEMICOLON
    '''
    if p[1] not in names:
        names[p[1]] = None
    if len(p) == 5:
        p[0] = Assign(p[1], p[3]) 
    else:
        p[0] = Assign([p[1], p[3]], p[6])
    
def p_conditional(p):
    'conditional : IF LPAREN expression RPAREN block'    
    p[0] = Conditional(p[3], p[5]) 
    
def p_conditional_else(p):
    'conditional : IF LPAREN expression RPAREN block ELSE block' 
    p[0] = ConditionalElse(p[3], p[5], p[7])
    
def p_loop(p):
    'loop : WHILE LPAREN expression RPAREN block'
    p[0] = Loop(p[3], p[5])
    
def p_block(p):
    'block : LBLOCK statements RBLOCK'
    p[0] = Block(p[2])

def p_block_statements(p):
    '''
    statements : statements statement
               | statement
    '''
    if (len(p) == 2):
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''
    statement : empty
              | print
              | assignment
              | conditional
              | loop
    '''
    p[0] = p[1]
    
def p_empty(p):
   'empty :'
   pass

def p_funcDef(p):
    '''
    function : FUN NAME funcVar EQUALS block expression SEMICOLON
    '''
    if p[2] not in funcnames:
        funcnames[p[2]] = None
    p[0] = FunctionDef(p[2], p[3], p[5], p[6])
    
def p_funcCall(p):
    '''
    functionCallVars : NAME LPAREN expression RPAREN
                     | NAME LPAREN expression COMMA
                     | NAME LPAREN RPAREN
    '''
    if len(p) == 4:
        x = [p[1]]
    else:
        x = [p[1], p[3]]
    p[0] = x

def p_funcCall2(p):
    '''
    functionCallVars : functionCallVars expression COMMA
                     | functionCallVars expression RPAREN
    '''
    p[0] = p[1] + [p[2]]
    
    
def p_funcCall3(p):
    'functionCall : functionCallVars'
    p[0] = p[1]
    
def p_funcCallExpr(p):
    'expression : functionCall'
    funcVarValues = p[1].pop(0)
    p[0] = FunctionCall(funcVarValues, p[1])
    
def p_funcCallStat(p):
    'statement : functionCall'
    funcVarValues = p[1].pop(0)
    p[0] = FunctionCall(funcVarValues, p[1])
    
def p_funcVarList(p):
    '''
    funcVar : LPAREN NAME RPAREN
            | LPAREN NAME COMMA
            | LPAREN RPAREN
    '''    
    if len(p) == 3:
        x = []
    else:
        names[p[2]] = None
        x = [p[2]]
    p[0] = x
    
def p_funcVarList2(p):
    '''
    funcVar : funcVar NAME COMMA
            | funcVar NAME RPAREN
    '''
    names[p[2]] = None
    p[0] = p[1] + [p[2]]
    
    
def p_error(p):
    print("SYNTAX ERROR")
    sys.exit()
    

file_name = sys.argv[1]
f = open(file_name)

parser = yacc.yacc()



def main():
    #tokenize()
    result = parser.parse(f.read(), debug = 1)
    for item in result:
        item.eval()
        
    

if __name__ == "__main__":
    main()
'''

def parse(inp):
    result = parser.parse(inp, debug = 1)
    return result
        
def main():
    for line in f:
        inp = line
        tokenize(inp)
        result = parse(inp)
        print(result)
        if result is not None:
            print("Evaluation:", result.eval())
    

if __name__ == "__main__":
    main()
'''