import ply.lex as lex

tokens = ['INT', 'FLOAT', 'NUM', 'REAL', 'ID', 'IGUAL', 'PV', 'VIR', 'ADD', 'SUB',
          'MUL', 'DIV', 'PRINT', 'PE', 'PD', 'ASPAS', 'SCAN', 'ENDID',
          'CE', 'CD', 'GT', 'GE', 'LT', 'LE', 'EQ', 'DIF', 'DO', 'WHILE', 'TEXTO',
          'OR']

t_INT = r'int'
t_FLOAT = r'float'
t_NUM = r'\d+'
t_REAL = r'[+\-]?\d*\.\d+'
t_TEXTO = '"[\W\w]*"'
t_ID = r'\w+'
t_IGUAL = r'='
t_PV = r';'
t_VIR = r','
t_ASPAS = r'"'
t_ADD = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_PRINT = r'^printf' #----------------------
t_PE = r'\('
t_PD = r'\)'
t_SCAN = r'^scanf' #----------
t_ENDID = r'&\w+'
t_CE = r'\{'
t_CD = r'\}'
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_EQ = r'=='
t_DIF = r'!='
t_DO = r'do'
t_WHILE = r'while'
t_OR = r'||'


t_ignore = " \t\n" #--------------------

def t_error(t):
    print("Carácter ilegal: ", t.value[0])
    t.lexer.skip(1)

#build the lexer
lexer = lex.lex()