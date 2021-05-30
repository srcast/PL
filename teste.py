import sys

import ply.yacc as yacc
import re
import sys

from trab2_lex import tokens


#Production rules
def p_File(p): #############################################
    "File : Inic"
    p[0] = p[1]

def p_Inic(p):
    "Inic : DeclVar Inic"
    p[0] = p[1] + p[2]

def p_Inic_vazio(p):
    "Inic : "
    p[0] = ""

def p_DeclVar_int(p):
    "DeclVar : INT RestoDeclInt"
    p[0] = p[2]

def p_DeclVar_char(p):
    "DeclVar : FLOAT RestoDeclFloat"
    p[0] = p[2]


def p_RestoDeclInt_id(p):
    "RestoDeclInt : ID OpcDeclInt"
    p.parser.registos.update({p[1]: p.parser.soma})
    p.parser.tipos.update({p[1]: 'int'})
    p.parser.soma += 1
    p[0] = "PUSHI " + p[2]

def p_RestoDeclInt_idarray(p):
    "RestoDeclInt : IDARRAY RestoArrayInt"
    nome = re.match(r'[a-zA-Z][a-zA-Z]*', p[1])
    tamanho = re.search(r'\d+', p[1])
    p.parser.registos.update({nome.group(): p.parser.soma})
    p.parser.tipos.update({nome.group(): 'int'})
    p.parser.soma += int(tamanho.group())
    p[0] = "PUSHN " + tamanho.group() + "\n" + p[2]

def p_RestoArrayInt_igual(p):
    "RestoArrayInt : IGUAL OpcDeclInt"
    p[0] = p[2]

def p_RestoArrayInt_pv(p):
    "RestoArrayInt : PV"
    p[0] = ""




def p_OpcDeclInt_igual(p):
    "OpcDeclInt : IGUAL SegueIgual"
    p[0] = p[2]

def p_OpcDeclInt_pv(p):
    "OpcDeclInt : PV"
    p[0] = "0\n"


def p_RestoDeclFloat_id(p):
    "RestoDeclFloat : ID OpcDeclFloat"
    p.parser.registos.update({p[1]: p.parser.soma})
    p.parser.tipos.update({p[1]: 'float'})
    p.parser.soma += 1
    p[0] = "PUSHF " + p[3]

def p_RestoDeclFloat_idarray(p):
    "RestoDeclFloat : IDARRAY RestoArrayFloat"
    nome = re.match(r'[a-zA-Z][a-zA-Z]*', p[1])
    tamanho = re.search(r'\d+', p[1])
    p.parser.registos.update({nome.group(): p.parser.soma})
    p.parser.tipos.update({nome.group(): 'float'})
    p.parser.soma += int(tamanho.group())
    p[0] = "PUSHN " + tamanho.group() + "\n" + p[2]

def p_RestoArrayFloat_igual(p):
    "RestoArrayFloat : IGUAL OpcDeclFloat"
    p[0] = p[2]

def p_RestoArrayFloat_pv(p):
    "RestoArrayFloat : PV"
    p[0] = ""


def p_OpcDeclFloat_igual(p):
    "OpcDeclFloat : IGUAL SegueIgual"
    p[0] = p[2]

def p_OpcDeclFloat_pv(p):
    "OpcDeclFloat : PV"
    p[0] = "0.0\n"

def p_SegueIgual_num(p):
    "SegueIgual : NUM PV"
    p[0] = p[1] + "\n"

def p_SegueIgual_real(p):
    "SegueIgual : REAL PV"
    p[0] = p[1] + "\n"

#error rule for syntax errors
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def p_error(p):
    if p == None:
        token = "end of file"
    else:
        token = f"{p.type}({p.value}) on line {p.lineno}"

    print(f"Syntax error: Unexpected {token}")

#build the parser
parser = yacc.yacc()

parser.registos = {}
parser.tipos = {}
parser.arraysTam = {}
parser.soma = 0
parser.somaIf = 0
parser.somaDoWhile = 0

f = open("teste.txt", "r")

res = open("res.txt", "w")

#reading input
for linha in f:
    resultado = parser.parse(linha)
    res.write(str(resultado))

for elem in parser.registos:
    print(elem + ": " + str(parser.registos.get(elem)))

for elem in parser.tipos:
    print(elem + ": " + str(parser.tipos.get(elem)))

for elem in parser.arraysTam:
    print(elem + ": " + str(parser.arraysTam.get(elem)))