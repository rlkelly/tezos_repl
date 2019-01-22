import ply.yacc as yacc

from objects import (Unit, Nat, Int, Bool,
        NoneType, Pair, String, Bytes, Set, List, Or, Lambda)


tokens = (
    # reserved words
    'NUMBER',
    'TEXT',
    'DROP',
    'FAILWITH',
    'DUP',
    'SWAP',
    'PUSH',
    'LAMBDA',
    'EXEC',

    'LBRACKET',
    'RBRACKET',

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
    'LSL',
    'LSR',
    'COMPARE',

    ### String Operations
    'CONCAT',
    'SIZE',
    'SLICE',
    # 'COMPARE',

    ### Pair Operations
    'PAIR',
    'CAR',
    'CDR',

    ### Set Operations
    'EMPTY_SET',
    'MEM',
    'UPDATE',
    # 'ITER', # TODO: implement TODO
    # 'SIZE',

    ### Map Operations
    'EMPTY_MAP',
    'GET',
    # 'MEM',
    # 'UPDATE',
    # MAP body,
    # ITER body,
    # 'SIZE',

    ### Option Operations
    'SOME',
    'NONE',
    # IF_NONE bt bf

    ### Union Operations
    'LEFT',
    'RIGHT',
    # 'IF_LEFT',
    # 'IF_RIGHT',

    ### Operations on Lists
    'CONS',
    'NIL',
    # 'IF_CONS',
    # 'MAP',
    # 'SIZE',
    # 'ITER' body

    ###
    'UNIT',
    'NAT',
    'STRING',
    'INT',
    'BOOL',
    'BYTES',
    'LPAIR',
    'PAIR_CONSTRUCTOR',

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

    'LPARENS',
    'RPARENS',
    'SCOLON',
)

# Tokens

t_DROP        = 'DROP'
t_SWAP        = 'SWAP'
t_DUP         = 'DUP'
t_UNIT        = 'UNIT'
t_FAILWITH    = 'FAILWITH'
t_PUSH        = 'PUSH'
t_LAMBDA      = 'LAMBDA'
t_EXEC        = 'EXEC'

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
t_LSL           = 'LSL'
t_LSR           = 'LSR'
t_COMPARE       = 'COMPARE'

### String Operations
t_CONCAT        = 'CONCAT'
t_SIZE          = 'SIZE'
t_SLICE         = 'SLICE'
# t_COMPARE       = 'COMPARE'

### Pair Operations
t_PAIR          = 'PAIR'
t_CAR           = 'CAR'
t_CDR           = 'CDR'

### Set Operations
t_EMPTY_SET     = 'EMPTY_SET'
t_MEM           = 'MEM'
t_UPDATE        = 'UPDATE'

### Option Operations
t_SOME          = 'SOME'
t_NONE          = 'NONE'

### Union Operations
t_LEFT          = 'LEFT'
t_RIGHT         = 'RIGHT'

### List Operations
t_CONS          = 'CONS'
t_NIL           = 'NIL'

t_NAT         = 'nat'
t_STRING      = 'string'
t_INT         = 'int'
t_BOOL        = 'bool'
t_BYTES       = 'bytes'

t_TRUE        = 'True'
t_FALSE       = 'False'
t_TEXT        = '".*"'
t_LBRACKET    = '{'
t_RBRACKET    = '}'
t_LPARENS     = '\('
t_RPARENS     = '\)'
t_LPAIR       = 'pair'
t_PAIR_CONSTRUCTOR = 'Pair'
t_SCOLON      = ';'

def t_comment(t):
    r"[ ]*\043[^\n]*"  # \043 is '#'
    pass

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

stack = []

def p_execution(t):
    '''execution : compound_statement
            | compound_statement SCOLON
            | body'''
    # stmt is allowed for the repl
    t[0] = t[1]

def p_compound_statement(t):
    '''compound_statement : stmt
            | compound_statement SCOLON stmt'''
    if len(t) <= 2:
        t[0] = t[1]
    else:
        print(t[1], t[3])
        t[0] = [t[1], t[3]]

def p_body(t):
    '''body : LBRACKET compound_statement RBRACKET
            | LBRACKET RBRACKET'''
    print(len(t))
    if len(t) == 4:
        t[0] = t[2]
    else:
        t[0] = NoneType
def p_lambda_statement(t):
    '''stmt : LAMBDA TYPE TYPE body'''
    print('body', t[1], t[2], t[3], t[4])
    stack.append(Lambda(t[2], t[3], t[4]))

def p_statement_drop(t):
    'stmt : DROP '
    stack.pop(-1)

def p_statement_dup(t):
    'stmt : DUP '
    stack = stack + stack[-1:]

def p_statement_swap(t):
    'stmt : SWAP '
    stack[0], stack[1] = stack[1], stack[0]

def p_statement_unit(t):
    'stmt : UNIT '
    stack.append(Unit)

def p_bool(t):
    '''bool : TRUE
        | FALSE '''
    t[0] = t[1]

def p_statement_value(t):
    '''value : NUMBER
        | bool
        | TEXT
        | LPARENS PAIR_CONSTRUCTOR value value RPARENS '''
    if t[1] == '(':
        t[0] = (t[3], t[4])
    else:
        t[0] = t[1]

def p_statement_generic_comparison(t):
    '''stmt : EQ
        | NEQ
        | LT
        | GT
        | LE
        | GE  '''
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
    '''stmt : OR
        | AND
        | XOR  '''
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
            stack.append(first.bit_or(second))
        elif bool_comparison == 'AND':
            stack.append(first.bit_and(second))
        elif bool_comparison == 'XOR':
            stack.append(first.bit_xor(second))
    else:
        # TODO: explain error better
        print('invalid stack state')

def p_compare_operation(t):
    '''stmt : COMPARE '''
    top = stack.pop(-1)
    if type(top) in (Int, Nat):
        value2 = stack.pop(-1)
        stack.append(value.compare(value2))
    elif isintance(top, String):
        value = stack.pop(-1)
        stack.append(value.compare(value2))
    else:
        print('Invalid Stack State')

def p_integer_operations(t):
    '''stmt : NEG
         | ABS
         | ADD
         | SUB
         | MUL
         | EDIV
         | LSL
         | LSR  '''
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
        stack.append(value.ediv(value2))
    elif integer_operator == 'LSL':
        value2 = stack.pop(-1)
        assert isinstance(value, Nat)
        stack.append(value.lsl(value2))
    elif integer_operator == 'LSR':
        value2 = stack.pop(-1)
        assert isinstance(value, Nat)
        stack.append(value.lsr(value2))
    else:
        # TODO: better error
        print('invalid stack state')

def p_string_operations(t):
    '''stmt : CONCAT
            | SIZE
            | SLICE  '''
    if t[1] == 'CONCAT':
        first = stack.pop(-1)
        second = stack.pop(-1)
        assert isinstance(first, String) and isinstance(second, String)
        stack.append(first.concat(second))
    elif t[1] == 'SIZE':
        first = stack.pop(-1)
        assert type(first) in (String, Set, List) # TODO: Factor this to seperate call
        stack.append(first.size())
    elif t[1] == 'SLICE':
        first = stack.pop(-1)
        second = stack.pop(-1)
        third = stack.pop(-1)
        assert isinstance(first, Nat) and isinstance(second, Nat) and isinstance(third, String)
        stack.append(third.slice(first, second))

def p_pair_operations(t):
    '''stmt : PAIR
            | CAR
            | CDR  '''
    pair_operation = t[1]
    first = stack.pop(-1)
    if pair_operation == 'PAIR':
        second = stack.pop(-1)
        stack.append(Pair(first, second))
        return
    if not isinstance(first, Pair):
        print('invalid stack state')
        return

    if pair_operation == 'CAR':
        stack.append(first.left)
    elif pair_operation == 'CDR':
        stack.append(first.right)

def p_set_operations(t):
    '''stmt : EMPTY_SET TYPE
            | MEM
            | UPDATE  '''
    if t[1] == 'EMPTY_SET':
        stack.append(Set(t[2]))
    elif t[1] == 'MEM':
        top = stack.pop(-1)
        stack_set = stack.pop(-1)
        assert isinstance(stack_set, Set)
        assert isinstance(top, comparison_set.set_type)
        stack.append(stack_set.contains(top))
    elif t[1] == 'UPDATE':
        elt = stack.pop(-1)
        bool = stack.pop(-1)
        stack_set = stack.pop(-1)
        stack.append(stack_set.update(elt, bool))

def p_option_operations(t):
    '''stmt : SOME
            | NONE TYPE  '''
    top = stack.pop(-1)
    if t[1] == 'SOME':
        stack.append(Some(top))
    else:
        stack.append(NoneType(t[2]))

def p_union_operations(t):
    '''stmt : LEFT TYPE
            | RIGHT TYPE  '''
    top = stack.pop(-1)
    new_or = Or(type(top), t[2], side=t[1])
    new_or.add_value(top)
    stack.append(new_or)

def p_list_operations(t):
    '''stmt : CONS
            | NIL TYPE  '''
    if t[1] == 'NIL':
        stack.append(List(t[2]))
    else:
        top = stack.pop(-1)
        list = stack.pop(-1)
        assert isinstance(list, List)
        stack.append(list.cons(top))

def p_boolean_not(t):
    'stmt : NOT '
    bool_comparison = t[1]
    first = stack.pop(-1)
    if isinstance(first, Bool):
        stack.append(first.flip())
    elif type(first) in (Nat, Int):
        stack.append(first.bit_not())
    else:
        # TODO: better error
        print('invalid stack state')

def p_exec(t):
    'stmt : EXEC'
    arg = stack.pop(-1)
    lam_func = stack.pop(-1)
    assert isinstance(lam_func, Lambda)
    assert deep_compare(arg, lam_func.inputs)

def p_statement_type(t):
    '''TYPE : NAT
        | STRING
        | INT
        | BOOL
        | BYTES
        | LPARENS LPAIR TYPE TYPE RPARENS '''
    if t[1] == 'nat':
        t[0] = Nat
    elif t[1] == 'string':
        t[0] = String
    elif t[1] == 'int':
        t[0] = Int
    elif t[1] == 'bool':
        t[0] = Bool
    elif t[1] == 'bytes':
        t[0] = Bytes
    elif t[1] == '(':
        t[0] = Pair(t[3], t[4])

def p_statement_push(t):
    'stmt : PUSH TYPE value '
    value = None
    if t[2] == Nat:
        value = Nat(t[3])
    elif t[2] == Int:
        value = Int(t[3])
    elif t[2] == Bool:
        value = Bool(t[3])
    elif t[2] == String:
        value = String(t[3])
    elif isinstance(t[2], Pair):
        value = t[2]((t[3][0], t[3][1]))
    if value:
        t[0] = ['PUSH', t[2], t[3]]
        stack.append(value)
    else:
        print('type not implemented')

def p_statement_failwith(t):
    'stmt : FAILWITH '
    top = stack[-1]
    print(f'fail with {top}')
    print('new stack\n\n')
    stack = []

def p_error(t):
    print('syntax error')
    if t:
        print(f'{t.value}')

if __name__ == '__main__':
    parser = yacc.yacc()
    while True:
        try:
            open = False
            text = ''
            s = input('stack > ')   # Use raw_input on Python 2
            # while s != '':
            #     text += s
            #     s = input()
        except EOFError:
             break
        parser.parse(s)
        print(stack[::-1])
