import sys

import ply.yacc as yacc
import re
import sys

from trab2_lex import tokens


#Production rules
def p_File(p): #############################################
    "File : Inic BlocoInst"
    p[0] = p[1] + p[2]

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





def p_BlocoInst_inst(p):
    "BlocoInst : Inst BlocoInst"
    p[0] = p[1] + p[2]

def p_BlocoInst_vazio(p): ##############################3
    "BlocoInst : "
    p[0] = ""

def p_Inst_atribuicao(p):
    "Inst : Atribuicao"
    p[0] = p[1]

def p_Inst_print(p):
    "Inst : Printf"
    p[0] = p[1]

def p_Inst_ler(p):
    "Inst : Scanf"
    p[0] = p[1]

def p_Inst_if(p):
    "Inst : If"
    p[0] = p[1]

def p_Inst_dowhile(p):
    "Inst : DoWhile"
    p[0] = p[1]



def p_Atribuicao_id(p):
    "Atribuicao : ID IGUAL RestoAtrib"
    p[0] = p[3] + "STOREG " + str(p.parser.registos.get(p[1])) + "\n"

def p_Atribuicao_idarray(p):
    "Atribuicao : IDARRAY IGUAL RestoAtrib"
    nome = re.match(r'[a-zA-Z][a-zA-Z]*', p[1])
    tamanho = re.search(r'\d+', p[1])
    p[0] = "PUSHGP\n" + "PUSHI " + str(p.parser.registos.get(nome.group())) + "\nPADD\n" + "PUSHI " + tamanho.group() + "\n" + p[3] + "\nSTOREN\n"

def p_RestoAtrib_add(p):
    "RestoAtrib : Exp ADD Exp PV"
    p[0] = p[1] + p[3] + "ADD\n"

def p_RestoAtrib_sub(p):
    "RestoAtrib : Exp SUB Exp PV"
    p[0] = p[1] + p[3] + "SUB\n"

def p_RestoAtrib_exp(p):
    "RestoAtrib : Exp PV"
    p[0] = p[1]


def p_Exp_mul(p):
    "Exp : Exp2 MUL Exp2"
    p[0] = p[1] + p[3] + "MUL\n"

def p_Exp_div(p):
    "Exp : Exp2 DIV Exp2"
    p[0] = p[1] + p[3] + "DIV\n"

def p_Exp_exp2(p):
    "Exp : Exp2"
    p[0] = p[1]

def p_Exp2_id(p):
    "Exp2 : ID"
    p[0] = "PUSHG " + str(p.parser.registos.get(p[1])) + "\n"

def p_Exp2_num(p):
    "Exp2 : NUM"
    p[0] = "PUSHI " + str(p[1]) + "\n"

def p_Exp2_real(p):
    "Exp2 : REAL"
    p[0] = "PUSHF " + str(p[1]) + "\n"





def p_Printf_print(p):
    "Printf : PRINT PE TEXT RestoPrintf"
    p[0] = "PUSHS " + p[3] + "\n" + "WRITES" + "\n" + p[4]

def p_RestoPrintf_pd(p):
    "RestoPrintf : PD PV"
    p[0] = ""

def p_RestoPrintf_vir(p):
    "RestoPrintf : VIR ContPrintf"
    p[0] = p[2]


def p_ContPrintf_id(p):
    "ContPrintf : ID PD PV"
    if(str(p.parser.tipos.get(p[1])) == "int"):
        p[0] = "PUSHG " + str(p.parser.registos.get(p[1])) + "\n" + "WRITEI" + "\n"
    else:
        p[0] = "PUSHG " + str(p.parser.registos.get(p[1])) + "\n" + "WRITEF" + "\n"

def p_ContPrintf_idarray(p):
    "ContPrintf : IDARRAY PD PV"
    nome = re.match(r'[a-zA-Z][a-zA-Z]*', p[1])
    tamanho = re.search(r'\d+', p[1])
    if (str(p.parser.tipos.get(nome.group())) == "int"):
        p[0] = "PUSHGP\n" + "PUSHI " + str(p.parser.registos.get(nome.group())) + "\nPADD\n" + "PUSHI " + tamanho.group() + "\n" + p[3] + "\nLOADN\n" + "WRITEI\n"
    else:
        p[0] = "PUSHGP\n" + "PUSHI " + str(p.parser.registos.get(nome.group())) + "\nPADD\n" + "PUSHI " + tamanho.group() + "\n" + p[3] + "\nLOADN\n" + "WRITEF\n"


def p_Scanf_scanf(p):
    "Scanf : SCAN PE TEXT VIR ENDID RestoScanf"
    nome = p[5]
    if (str(p.parser.tipos.get(nome[1:])) == "int"):
        p[0] = "READ\n" + "ATOI\n" + "STOREG " + str(p.parser.registos.get(nome[1:])) + p[6]
    else:
        p[0] = "READ\n" + "ATOF\n" + "STOREG " + str(p.parser.registos.get(nome[1:])) + p[6]

def p_RestoScanf_pd(p):
    "RestoScanf : PD PV"
    p[0] = "\n"







def p_If_if(p):
    "If : IF Cond CE BlocoInstIf CD"
    parser.somaIf += 1
    p[0] = p[2] + "\nJZ Endif" + str(parser.somaIf) + "\n" + p[4] + "\nEndIf" + str(parser.somaIf) + ":\n"

def p_Cond_exp(p):
    "Cond : PE Conta ExpRel Conta PD"
    p[0] = p[2] + p[4] + p[3]

def p_Cond_conta(p):
    "Cond : Conta"
    p[0] = p[1]

def p_ExpRel_gt(p):
    "ExpRel : GT"
    p[0] = "SUP\n"

def p_ExpRel_ge(p):
    "ExpRel : GE"
    p[0] = "SUPEQ\n"

def p_ExpRel_lt(p):
    "ExpRel : LT"
    p[0] = "INF\n"

def p_ExpRel_le(p):
    "ExpRel : LE"
    p[0] = "INFEQ\n"

def p_ExpRel_eq(p):
    "ExpRel : EQ"
    p[0] = "EQUAL\n"

def p_ExpRel_dif(p): #########################################################
    "ExpRel : DIF"
    p[0] = "EQUAL\n" + "NOT\n"

def p_Conta_pe(p):
    "Conta : PE Conta2 PD"
    p[0] = p[2]

def p_Conta_conta2(p):
    "Conta : Conta2"
    p[0] = p[1]

def p_Conta2_sub(p):
    "Conta2 : Exp SUB Exp"
    p[0] = p[1] + p[3] + "SUB\n"

def p_Conta2_add(p):
    "Conta2 : Exp ADD Exp"
    p[0] = p[1] + p[3] + "ADD\n"

def p_Conta2_exp(p):
    "Conta2 : Exp"
    p[0] = p[1]

def p_BlocoInstIf_inst(p):
    "BlocoInstIf : InstBlocoIf BlocoInstIf"
    p[0] = p[1] + p[2]

def p_BlocoInstIf_vazio(p):
    "BlocoInstIf : "
    p[0] = ""

def p_InstBlocoIf_atr(p):
    "InstBlocoIf : Atribuicao"
    p[0] = p[1]

def p_InstBlocoIf_print(p):
    "InstBlocoIf : Printf"
    p[0] = p[1]

def p_InstBlocoIf_scan(p):
    "InstBlocoIf : Scanf"
    p[0] = p[1]

def p_InstBlocoIf_if(p):
    "InstBlocoIf : If"
    p[0] = p[1]







def p_DoWhile_do(p):
    "DoWhile : DO CE BlocoDoWhile CD WHILE Cond PV"
    parser.somaDoWhile += 1
    p[0] = "DoWhile" + str(parser.somaIf) + ":\n" + p[3] + "\n" + p[6] + "\nEndDoWhile" + str(parser.somaIf) + ":\n"

def p_BlocoDoWhile_inst(p):
    "BlocoDoWhile : InstBlocoDo BlocoDoWhile"
    p[0] =p[1] + p[2]

def p_BlocoDoWhile_vazio(p):
    "BlocoDoWhile : "
    p[0] = ""

def p_InstBlocoDo_atr(p):
    "InstBlocoDo : Atribuicao"
    p[0] = p[1]

def p_InstBlocoDo_print(p):
    "InstBlocoDo : Printf"
    p[0] = p[1]

def p_InstBlocoDo_scan(p):
    "InstBlocoDo : Scanf"
    p[0] = p[1]

def p_InstBlocoDo_if(p):
    "InstBlocoDo : If"
    p[0] = p[1]

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

res.write("STOP")
f.close()
res.close()

for elem in parser.registos:
    print(elem + ": " + str(parser.registos.get(elem)))

for elem in parser.tipos:
    print(elem + ": " + str(parser.tipos.get(elem)))

for elem in parser.arraysTam:
    print(elem + ": " + str(parser.arraysTam.get(elem)))