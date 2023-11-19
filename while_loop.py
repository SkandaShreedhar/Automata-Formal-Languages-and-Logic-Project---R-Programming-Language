from ply import lex, yacc

# lexer token

tokens = (
    'ID',
    'Left_Parenthesis',
    'Right_Parenthesis',
    'Left_Braces',
    'Right_Braces',
    'While',
    'Double_Equal_To_Sign',
    'EQ',
    'Lesser_Than_Sign',
    'Greater_Than_Sign',
    'Addition',
    'Subtraction',
    'Multiplication',
    'Division',
    'Number',
    'Print',
    'AND',
    'And_And_Sign',
    'OR',
    'Or_Or_Sign',
    'Not_Equal_To_Sign',
)

t_Left_Parenthesis = r'\('
t_Right_Parenthesis = r'\)'
t_Left_Braces = r'\{'
t_Right_Braces = r'\}'
t_Double_Equal_To_Sign = r'=='
t_EQ = r'='
t_Lesser_Than_Sign = r'<'
t_Greater_Than_Sign = r'>'
t_Addition = r'\+'
t_Subtraction = r'-'
t_Multiplication = r'\*'
t_Division = r'/'
t_Number = r'\d+'
t_Print = r'Print'
t_AND = r'&'
t_And_And_Sign = r'&&'
t_OR = r'\|'
t_Or_Or_Sign = r'\|\|'
t_Not_Equal_To_Sign = r'!='

def t_While(t):
    r'While'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'ID'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# parser tab

def p_While_loop(p):
    '''
    While_loop : While Left_Parenthesis condition Right_Parenthesis Left_Braces statements Right_Braces
    '''
    # handles the parsed data as needed
    print("While-Loop has been parsed successfully!")

def p_condition(p):
    '''
    condition : expression Double_Equal_To_Sign expression
              | expression Lesser_Than_Sign expression
              | expression Greater_Than_Sign expression
              | expression And_And_Sign expression
              | expression Or_Or_Sign expression
              | expression Not_Equal_To_Sign expression
    '''
    # handles the parsed data as needed
    pass

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''
    # handles the parsed data as needed
    pass

def p_statement(p):
    '''
    statement : assignment_statement
              | While_loop
              | expression_statement
              | Print_statement
    '''
    # handles the parsed data as needed
    pass

def p_expression_statement(p):
    '''
    expression_statement : expression
    '''
    # handles the parsed data as needed
    pass

def p_assignment_statement(p):
    '''
    assignment_statement : ID EQ expression
    '''
    # handles the parsed data as needed
    pass

def p_Print_statement(p):
    '''
    Print_statement : Print Left_Parenthesis expression Right_Parenthesis
    '''
    # handles the parsed data as needed
    pass

def p_expression(p):
    '''
    expression : ID
               | Number
               | expression Addition expression
               | expression Subtraction expression
               | expression Multiplication expression
               | expression Division expression
               | Left_Parenthesis expression Right_Parenthesis
    '''
    # handles the parsed data as needed
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# Take user input
Input = input("Enter your code:\n")
lexer.input(Input)
parser.parse(lexer=lexer)




#Example Input: While (i < 10) {
#                               Print(i)
#                               i = i + 1
#                               }