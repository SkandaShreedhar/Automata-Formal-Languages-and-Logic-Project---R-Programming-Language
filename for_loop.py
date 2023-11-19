import ply.lex as lex
import ply.yacc as yacc

# lexer token

tokens = (
    'FOR',
    'IN',
    'Identifier',
    'Number',
    'Colon_Sign',
    'Open_Curly_Braces',
    'Close_Curly_Braces',
    'Open_Parenthesis',
    'Close_Parenthesis'
)

t_Identifier = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_Number = r'\d+'
t_Colon_Sign = r':'
t_Open_Curly_Braces = r'\{'
t_Close_Curly_Braces = r'\}'
t_Open_Parenthesis = r'\('
t_Close_Parenthesis = r'\)'

t_ignore = ' \t\n'

def t_IN(t):
    r'in'
    t.type='IN'
    return t

def t_FOR(t):
    r'for'
    t.type='FOR'
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# parser tab

def p_for_loop(p):
    '''
    for_loop : FOR Open_Parenthesis Identifier IN range Close_Parenthesis Open_Curly_Braces statements Close_Curly_Braces
    '''
    print("The For-Loop Statement Syntax is Valid!")

def p_range(p):
    '''
    range : Number Colon_Sign Number
    '''
    pass

def p_statements(p):
    '''
    statements : statements statement
               | statement
    '''
    pass

def p_statement(p):
    '''
    statement : Identifier
    '''
    pass

def p_error(p):
    print("Syntax error in input!")

lexer = lex.lex()
parser = yacc.yacc()

# for taking user input

user_input = input("Enter your code:\n")

lexer.input(user_input)
TOKEN = [] 
while True:
    token = lexer.token()
    if not token:
        break 
    TOKEN.append(token)

for token in TOKEN:
    print(f"LexToken({token.type}, '{token.value}', {token.lineno}, {token.lexpos})")

try:
    answer = parser.parse(user_input, lexer=lexer)
    print(answer)
except Exception as e:
    print("Invalid statement: ", e)



# Example Input: for(i in 1:10){statements}