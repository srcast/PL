import ply.lex as lex

reservadas = {
    "float": "FLOAT",
    "int": "INT",
    "printf": "PRINT",
    "scanf": "SCAN",
    "do": "DO",
    "while": "WHILE",
    "if": "IF",
}

tokens = ['NUM', 'REAL', 'ID', 'IGUAL', 'PV', 'VIR', 'ADD', 'SUB',
          'MUL', 'DIV', 'PE', 'PD', 'ENDID', 'CE', 'CD', 'GT', 'GE', 'LT',
          'LE', 'EQ', 'DIF', 'TEXT']

tokens += list(reservadas.values())

t_NUM = r'\d+'
t_REAL = r'[+\-]?\d*\.\d+'
t_IGUAL = r'='
t_PV = r';'
t_VIR = r','
t_ADD = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_PE = r'\('
t_PD = r'\)'
t_ENDID = r'&\w+'
t_CE = r'\{'
t_CD = r'\}'
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_EQ = r'=='
t_DIF = r'!='


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')  # Check for reserved words
    return t


def t_TEXT(t):
    r'"[\W\w]*"'
    t.type = reservadas.get(t.value, 'TEXT')  # Check for reserved words
    return t


t_ignore = " \t\n"


def t_error(t):
    print("Carácter ilegal: ", t.value[0])
    t.lexer.skip(1)


# build the lexer
lexer = lex.lex()
