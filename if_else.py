import ply.lex as lex
import ply.yacc as yacc

# lexer token

tokens = (
    'ID',
    'Equal_To_Sign',
    'Left_Parenthesis',
    'Right_Parenthesis',
    'Left_Braces',
    'Right_Braces',
    'IF',
    'ELSE',
    'Double_Equal_To_Sign',
    'Lesser_Than_Sign',
    'Greater_Than_Sign',
    'Addition',
    'Subtraction',
    'Multiplication',
    'Division',
    'Number',
    'Assignment',
    'Semicolon_Sign',
    'AND',
    'And_And_Sign',
    'OR',
    'Or_Or_Sign',
    'Not_Equal_To_Sign',
)

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_Left_Parenthesis = r'\('
t_Right_Parenthesis = r'\)'
t_Left_Braces = r'\{'
t_Right_Braces = r'\}'
t_Equal_To_Sign = r'='
t_Double_Equal_To_Sign = r'=='
t_Lesser_Than_Sign = r'<'
t_Greater_Than_Sign = r'>'
t_Addition = r'\+'
t_Subtraction = r'-'
t_Multiplication = r'\*'
t_Division = r'/'
t_Number = r'\d+'
t_Assignment = r'<-'
t_Semicolon_Sign = r';'
t_AND = r'&'
t_And_And_Sign = r'&&'
t_OR = r'\|'
t_Or_Or_Sign = r'\|\|'
t_Not_Equal_To_Sign = r'!='

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# parser tab

def p_start(p):
    '''start : if_else_statement
    '''
    p[0] = p[1]
    pass

def p_if_else_statement(p):
    '''
    if_else_statement : IF Left_Parenthesis condition Right_Parenthesis Left_Braces statements Right_Braces
                      | IF Left_Parenthesis condition Right_Parenthesis Left_Braces statements Right_Braces ELSE Left_Braces statements Right_Braces
    '''
    if len(p) == 8:
        p[0] = 'if(' + p[3] + '){' + p[6] + '}'
    else:
        p[0] = 'if(' + p[3] + '){' + p[6] + '}else{' + p[10] + '}'

    print("If-Else Statement has been parsed successfully!")


def p_condition(p):
    '''
    condition : expression Lesser_Than_Sign expression
              | expression Greater_Than_Sign expression
              | expression Double_Equal_To_Sign expression
              | expression AND expression
              | expression And_And_Sign expression
              | expression OR expression
              | expression Or_Or_Sign expression
              | expression Not_Equal_To_Sign expression
    '''
    p[0] = p[1] + p[2] + p[3]
    pass

def p_statements(p):
    '''
    statements : statement
               | statements statement
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[0]
    pass

def p_statement(p):
    '''
    statement : Assignment_Statement Semicolon_Sign
              | if_else_statement
              | Expression_Statement Semicolon_Sign
    '''
    if len(p) == 2:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]
    pass

def p_Assignment_Statement(p):
    '''
    Assignment_Statement : ID Assignment expression
    '''
    p[0] = p[1]
    pass

def p_Expression_Statement(p):
    '''
    Expression_Statement : expression
    '''
    p[0] = p[1]
    pass

def p_expression(p):
    '''
    expression : ID
               | Number
               | expression Addition expression
               | expression Subtraction expression
               | expression Multiplication expression
               | expression Division expression
               | expression Equal_To_Sign expression
               | expression Not_Equal_To_Sign expression
               | expression Double_Equal_To_Sign expression
               | Left_Parenthesis expression Right_Parenthesis
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        if p[1] == '(':
            p[0] = '(' + p[2] + ')'
        else:
            p[0] = p[1] + p[2] + p[3]
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# for taking user input 

Input = input("Enter your code:\n")
lexer.input(Input)
parser.parse(lexer=lexer)


# Example Input: if (x == 0 && y != 5 ) {a = 10;}
