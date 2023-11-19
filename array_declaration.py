from ply import lex, yacc

# lexer token

tokens = (
    'Array_Name',
    'Left_Bracket',
    'Right_Bracket',
    'Equal_To_Sign',
    'Number',
    'Comma_Sign',
)

t_Left_Bracket = r'\['
t_Right_Bracket = r'\]'
t_Equal_To_Sign = r'='
t_Comma_Sign = r','
t_ignore = ' \t\n'

def t_Array_Name(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'Array_Name'
    return t

def t_Number(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# parser tab

def p_array_declaration(p):
    '''
    array_declaration : Array_Name Left_Bracket array_dims Right_Bracket Equal_To_Sign array_values
    '''
    # handles the parsed data as needed

    print("Array declaration has been parsed successfully!")

def p_array_dims(p):
    '''
    array_dims : Number
               | Number Comma_Sign Number
    '''
    # handles the parsed data as needed

    pass

def p_array_values(p):
    '''
    array_values : Number
                 | array_values Comma_Sign Number
    '''
    # handles the parsed data as needed

    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# for taking user input

while True:
    try:
        user_input = input("Enter array declaration or 'exit' (to quit): ")
       
        if user_input.lower() == 'exit':
            break

        lexer.input(user_input)
        result = parser.parse(lexer=lexer)

        print(result)

    except Exception as e:
        print(f"Error: {e}")



# Example Input: a[1, 2]=1, 2, 3, 4