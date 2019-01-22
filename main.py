from objects import Unit, Nat, Int, Bool, Pair

tokens = (
    # reserved words
    'NUMBER',
    'DROP',
    'FAILWITH',
    'DUP',
    'SWAP',
    'PUSH',
    # 'LAMBDA' not implemented

    ### Generic Comparison
    'EQ',
    'NEQ',
    'LT',
    'GT',
    'LE',
    'GE',

    ### Boolean Operations
    'OR',
    'AND',
    'XOR',
    'NOT',

    ### Integer Operations
    'NEG',
    'ABS',
    'ADD',
    'SUB',
    'MUL',
    'EDIV',

    ###
    'UNIT',
    'NAT',
    'STRING',
    'INT',
    'BOOL',
    'BYTES',

    'TRUE',
    'FALSE',

    # # types
    # 'timestamp',
    # 'mutez',
    # "contract 'param",
    # 'address',
    # 'operation',
    # 'key',
    # 'key_hash',
    # 'signature',
)

# Tokens

t_DROP        = 'DROP'
t_SWAP        = 'SWAP'
t_DUP         = 'DUP'
t_UNIT        = 'UNIT'
t_FAILWITH    = 'FAILWITH'
t_PUSH        = 'PUSH'

### Generic Comparison
t_EQ            = 'EQ'
t_NEQ           = 'NEQ'
t_LT            = 'LT'
t_GT            = 'GT'
t_LE            = 'LE'
t_GE            = 'GE'

### Boolean Operations
t_OR            = 'OR'
t_AND           = 'AND'
t_XOR           = 'XOR'
t_NOT           = 'NOT'

### Integer Operations
t_NEG           = 'NEG'
t_ABS           = 'ABS'
t_ADD           = 'ADD'
t_SUB           = 'SUB'
t_MUL           = 'MUL'
t_EDIV          = 'EDIV'

t_NAT         = 'nat'
t_STRING      = 'string'
t_INT         = 'int'
t_BOOL        = 'bool'
t_BYTES       = 'bytes'

t_TRUE        = 'True'
t_FALSE       = 'False'

def t_NUMBER(t):
    r'-?\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# dictionary of names
names = { }
stack = []

def p_statement_drop(t):
    'statement : DROP'
    stack.pop(-1)

def p_statement_dup(t):
    'statement : DUP'
    stack = stack + stack[-1:]

def p_statement_swap(t):
    'statement : SWAP'
    stack[0], stack[1] = stack[1], stack[0]

def p_statement_unit(t):
    'statement : UNIT'
    stack.append(Unit)

def p_bool(t):
    '''bool : TRUE
        | FALSE '''
    t[0] = t[1]

def p_statement_value(t):
    '''value : NUMBER
        | bool '''
    t[0] = t[1]

def p_statement_generic_comparison(t):
    '''statement : EQ
        | NEQ
        | LT
        | GT
        | LE
        | GE '''
    assert isinstance(stack[-1], Int)
    generic_comparison = t[1]
    if generic_comparison == 'EQ':
        stack[-1] = Bool(stack[-1] == 0)
    elif generic_comparison == 'NEQ':
        stack[-1] = Bool(stack[-1] != 0)
    elif generic_comparison == 'LT':
        stack[-1] = Bool(stack[-1] < 0)
    elif generic_comparison == 'GT':
        stack[-1] = Bool(stack[-1] > 0)
    elif generic_comparison == 'LE':
        stack[-1] = Bool(stack[-1] <= 0)
    elif generic_comparison == 'GE':
        stack[-1] = Bool(stack[-1] >= 0)

def p_boolean_comparison(t):
    '''statement : OR
        | AND
        | XOR '''
    bool_comparison = t[1]
    first = stack.pop(-1)
    second = stack.pop(-1)
    if isinstance(first, Bool) and isinstance(second, Bool):
        first = first.value
        second = second.value
        if bool_comparison == 'OR':
            stack.append(Bool(first or second))
        elif bool_comparison == 'AND':
            stack.append(Bool(first and second))
        elif bool_comparison == 'XOR':
            stack.append(Bool(first != second))
    elif isinstance(first, Nat) and isinstance(second, Nat):
        if bool_comparison == 'OR':
            stack.append(first.or(second))
        elif bool_comparison == 'AND':
            stack.append(first.and(second))
        elif bool_comparison == 'XOR':
            stack.append(first.xor(second))
    else:
        # TODO: explain error better
        print('invalid stack state')


def p_integer_operations(t):
    '''statement : NEG
         | ABS
         | ADD
         | SUB
         | MUL
         | EDIV '''
    integer_operator = t[1]
    value = stack.pop(-1)
    assert type(value) in (Nat, Int)
    if integer_operator == 'NEG':
        stack.append(value.neg())
    elif integer_operator == 'ABS':
        stack.append(value.abs())
    elif integer_operator == 'ADD':
        value2 = stack.pop(-1)
        stack.append(value.add(value2))
    elif integer_operator == 'SUB':
        value2 = stack.pop(-1)
        stack.append(value.add(value2.neg()))
    elif integer_operator == 'MUL':
        value2 = stack.pop(-1)
        stack.append(value.mul(value2))
    elif integer_operator == 'EDIV':
        value2 = stack.pop(-1)
        value1, value2 = value.ediv(value2)
        stack.append(Pair(value1, value2))

def p_boolean_not(t):
    'statement : NOT'
    bool_comparison = t[1]
    first = stack.pop(-1)
    assert isinstance(first, Bool)
    stack.append(first.flip())

def p_statement_type(t):
    '''TYPE : NAT
        | STRING
        | INT
        | BOOL
        | BYTES '''
    t[0] = t[1]

def p_statement_push(t):
    'statement : PUSH TYPE value'
    if t[2] == 'nat':
        value = Nat(t[3])
    if t[2] == 'int':
        value = Int(t[3])
    elif t[2] == 'bool':
        value = Bool(t[3])
    if value:
        stack.append(value)
    else:
        print('type not implemented')

def p_statement_failwith(t):
    'statement : FAILWITH'
    top = stack[-1]
    print(f'fail with {top}')
    print('new stack\n\n')
    stack = []

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('stack > ')   # Use raw_input on Python 2
    except EOFError:
         break
    parser.parse(s)
    print(stack)
