import time

import ply.lex as lex
import ply.yacc as yacc

from objects import (Unit, Nat, Int, Bool,
        Map, BigMap, Timestamp, Mutez,
        NoneType, Pair, String, Bytes, Set, List, Or, Lambda,
        Operation, deep_compare)
from check_indents import validate_indent

tokens = (
    # reserved words
    'NUMBER',
    'TEXT',
    'DROP',
    'FAILWITH',
    'FAIL',
    'DUP',
    'SWAP',
    'PUSH',
    'LAMBDA',
    'EXEC',
    'DIP',

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
    'ITER',
    # 'SIZE',

    ### Map Operations
    'EMPTY_MAP',
    'GET',
    # 'MEM',
    # 'UPDATE',
    'MAP',
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
    'IF_CONS',
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
    'TRUE',
    'FALSE',
    'PAIR_CONSTRUCTOR',

    # # types
    'TIMESTAMP',
    'MUTEZ',
    # "contract 'param",
    'ADDRESS',
    'OPERATION',
    # 'key',
    # 'key_hash',
    # 'signature',

    ### Special Operations
    'STEPS_TO_QUOTA',
    'NOW',

    'LPARENS',
    'RPARENS',
    'LBRACKET',
    'RBRACKET',
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
t_DIP         = 'DI*P'

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

### Map Operations
t_EMPTY_MAP     = 'EMPTY_MAP'
t_MAP           = 'MAP'
t_GET           = 'GET'
t_ITER          = 'ITER'
t_IF_CONS       = 'IF_CONS'

### Option Operations
t_SOME          = 'SOME'
t_NONE          = 'NONE'

### Union Operations
t_LEFT          = 'LEFT'
t_RIGHT         = 'RIGHT'

### List Operations
t_CONS          = 'CONS'
t_NIL           = 'NIL'

### Special Operations
t_STEPS_TO_QUOTA = 'STEPS_TO_QUOTA'
t_NOW            = 'NOW'

t_NAT         = 'nat'
t_STRING      = 'string'
t_INT         = 'int'
t_BOOL        = 'bool'
t_BYTES       = 'bytes'
t_OPERATION   = 'operation'
t_ADDRESS     = 'address'
t_MUTEZ       = 'mutez'
t_TIMESTAMP   = 'timestamp'

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

def p_execution(t):
    '''execution : compound_statement
            | compound_statement SCOLON
            | body'''
    global remaining_steps
    # stmt is allowed for the repl
    t[0] = t[1]
    for stmt in t[0]:
        stmt(stack)
        remaining_steps -= 1

def p_compound_statement(t):
    '''compound_statement : stmt
            | compound_statement SCOLON stmt'''
    if len(t) == 2:
        t[0] = [t[1]]
    elif type(t[1]) == list:
        t[0] = t[1] + [t[3]]
    else:
        t[0] = [t[1], t[3]]

def p_body(t):
    '''body : LBRACKET compound_statement SCOLON RBRACKET
            | LBRACKET compound_statement RBRACKET
            | LBRACKET RBRACKET'''
    if len(t) >= 4:
        t[0] = t[2]
    else:
        t[0] = NoneType

def p_lambda_statement(t):
    '''stmt : LAMBDA type type body'''
    lam_func = Lambda(t[2], t[3], t[4])
    def add_lambda(stack):
        stack.append(lam_func)
    t[0] = add_lambda

def p_statement_drop(t):
    'stmt : DROP'
    def exec_drop(stack):
        stack.pop(-1)
        return stack
    t[0] = exec_drop

def p_statement_dup(t):
    'stmt : DUP'
    def exec_dup(stack):
        stack.append(stack[-1])
        return stack
    t[0] = exec_dup

def p_statement_swap(t):
    'stmt : SWAP'
    def exec_swap(stack):
        stack[-1], stack[-2] = stack[-2], stack[-1]
        return stack
    t[0] = exec_swap

def p_statement_unit(t):
    'stmt : UNIT'
    def exec_unit(stack):
        stack.append(Unit)
        return stack
    t[0] = exec_unit

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
    generic_comparison = t[1]
    def exec_generic(stack):
        assert isinstance(stack[-1], Int)
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
        return stack
    t[0] = exec_generic

def p_boolean_comparison(t):
    '''stmt : OR
        | AND
        | XOR  '''
    bool_comparison = t[1]
    def exec_bool_comparison(stack):
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
            print('Invalid Stack State')
        return stack
    t[0] = exec_bool_comparison

def p_compare_operation(t):
    'stmt : COMPARE'
    def exec_compare(stack):
        top = stack.pop(-1)
        if type(top) in (Int, Nat):
            value2 = stack.pop(-1)
            stack.append(value.compare(value2))
        elif isintance(top, String):
            value = stack.pop(-1)
            stack.append(value.compare(value2))
        else:
            print('Invalid Stack State')
        return stack
    t[0] = exec_compare

def p_integer_operations(t):
    '''stmt : NEG
         | ABS
         | ADD
         | SUB
         | MUL
         | EDIV
         | LSL
         | LSR '''
    integer_operator = t[1]
    def exec_integer_op(stack):
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
            print('Invalid Stack State')
        return stack
    t[0] = exec_integer_op

def p_size_operation(t):
    'stmt : SIZE'
    size_operation = t[1]
    def exec_size_op(stack):
        first = stack.pop(-1)
        assert type(first) in (String, Set, List, Map)
        stack.append(first.size())
    t[0] = exec_size_op

def p_string_operations(t):
    '''stmt : CONCAT
            | SLICE'''
    string_operation = t[1]
    def exec_string_op(stack):
        if string_operation == 'CONCAT':
            first = stack.pop(-1)
            second = stack.pop(-1)
            assert isinstance(first, String) and isinstance(second, String)
            stack.append(first.concat(second))
        elif string_operation == 'SLICE':
            first = stack.pop(-1)
            second = stack.pop(-1)
            third = stack.pop(-1)
            assert isinstance(first, Nat) and isinstance(second, Nat) and isinstance(third, String)
            stack.append(third.slice(first, second))
    t[0] = exec_string_op

def p_pair_operations(t):
    '''stmt : PAIR
            | CAR
            | CDR '''
    pair_operation = t[1]
    def exec_pair_operation(stack):
        first = stack.pop(-1)
        if pair_operation == 'PAIR':
            second = stack.pop(-1)
            p = Pair(first.type, type(second))
            p((first.value, second.value))
            stack.append(p)
            return
        if not isinstance(first, Pair):
            print('Invalid Stack State')
            return
        if pair_operation == 'CAR':
            stack.append(first.left)
        elif pair_operation == 'CDR':
            stack.append(first.right)
        return stack
    t[0] = exec_pair_operation

def p_set_operations(t):
    '''stmt : EMPTY_SET type
            | MEM
            | UPDATE '''
    set_operation = t[1]
    if len(t) == 3:
        set_type = t[2]
    else:
        set_type = None
    def exec_set_op(stack):
        if set_operation == 'EMPTY_SET':
            stack.append(Set(set_type))
        elif set_operation == 'MEM':
            top = stack.pop(-1)
            stack_set = stack.pop(-1)
            assert type(stack_set) in (Set, Map)
            assert isinstance(top, stack_set.list_type)
            stack.append(stack_set.contains(top))
        elif set_operation == 'UPDATE':
            elt = stack.pop(-1)
            bool = stack.pop(-1)
            stack_set = stack.pop(-1)
            stack.append(stack_set.update(elt, bool))
        return stack
    t[0] = exec_set_op

def p_map_operations(t):
    '''stmt : EMPTY_MAP type type
            | MAP body
            | ITER body
            | GET'''
    map_operation = t[1]
    second_arg = t[2]
    if len(t) == 4:
        third_arg = t[3]
    else:
        third_arg = None
    def exec_map_op(stack):
        if map_operation == 'EMPTY_MAP':
            stack.append(MAP(second_arg, third_arg))
        elif map_operation == 'MAP':
            values = stack.pop(-1)
            if type(values) == List:
                list_values = values.value
                list_type = values.list_type
                new_list = []
                for value in list_values:
                    # TODO: add item get method and set type in getter
                    ministack = stack + [list_type(value)]
                    for arg in second_arg:
                        ministack = arg(ministack)
                    new_list.append(ministack.pop(-1))
                values.value = new_list
                stack.append(values)
        elif map_operation == 'ITER':
            values = stack.pop(-1)
            if type(values) in (List, Map, Set):
                list_values = values.value
                list_type = values.list_type
                for value in list_values:
                    # TODO: add item get method and set type in getter
                    stack.append(list_type(value))
                    for arg in second_arg:
                        arg(stack)
        elif map_operation == 'GET':
            key = stack.pop(-1)
            mapping = stack.pop(-1)
            assert isinstance(top, mapping.key_type)
            stack.append(mapping.get(key))
        return stack
    t[0] = exec_map_op

def p_if_cons(t):
    'stmt : IF_CONS body body'
    first_body = t[2]
    second_body = t[3]

    def exec_if_cons(stack):
        top = stack.pop(-1)
        assert isinstance(top, List)
        if top.size() == 0:
            for arg in second_body:
                stack = arg(stack)
        else:
            stack.append(top)
            for arg in first_body:
                stack = arg(stack)

def p_option_operations(t):
    '''stmt : SOME
            | NONE type '''
    option_op = t[1]
    def exec_option_op(stack):
        top = stack.pop(-1)
        if option_op == 'SOME':
            stack.append(Some(top))
        else:
            stack.append(NoneType(t[2]))
        return stack
    t[0] = exec_option_op

def p_union_operations(t):
    '''stmt : LEFT type
            | RIGHT type '''
    value_type = t[2]
    side = t[1]
    def exec_union_op(stack):
        top = stack.pop(-1)
        new_or = Or(type(top), value_type, side=side)
        new_or.add_value(top)
        stack.append(new_or)
        return stack
    t[0] = exec_union_op

def p_list_operations(t):
    '''stmt : CONS
            | NIL type '''
    list_op = t[1]
    if len(t) == 3:
        list_type = t[2]
    else:
        list_type = None
    def exec_list_op(stack):
        if list_op == 'NIL':
            stack.append(List(list_type))
        else:
            top = stack.pop(-1)
            list = stack.pop(-1)
            assert isinstance(list, List)
            stack.append(list.cons(top))
        return stack
    t[0] = exec_list_op

def p_boolean_not(t):
    'stmt : NOT'
    def exec_not(stack):
        first = stack.pop(-1)
        if type(first) in (Bool, Nat, Int):
            stack.append(first.flip())
        else:
            # TODO: better error
            print('Invalid Stack State')
        return stack
    t[0] = exec_not

def p_exec(t):
    'stmt : EXEC'
    def func_exec(stack):
        arg = stack.pop(-1)
        lam_func = stack.pop(-1)
        assert isinstance(lam_func, Lambda)
        assert deep_compare(arg, lam_func.input_type)
        ministack = [arg]
        for func in lam_func.body:
            ministack = func(ministack)
        assert len(ministack) == 1
        assert isinstance(ministack[0], lam_func.return_type)
        stack.append(ministack[0])
        return stack
    t[0] = func_exec

def p_special_operations(t):
    '''stmt : STEPS_TO_QUOTA
            | NOW '''
    command = t[1]
    def exec_special(stack):
        if command == 'STEPS_TO_QUOTA':
            stack.append(remaining_steps)
        else:
            stack.append(Timestamp(int(time.time())))
        return stack
    t[0] = exec_special

def p_statement_type(t):
    '''type : NAT
        | STRING
        | INT
        | BOOL
        | BYTES
        | OPERATION
        | ADDRESS
        | LPARENS LPAIR type type RPARENS '''
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
    elif t[1] == 'operation':
        t[0] = Operation
    elif t[1] == 'timestamp':
        t[0] = Timestamp
    elif t[1] == 'address':
        t[0] = Address
    elif t[1] == 'mutez':
        t[0] = Mutez
    elif t[1] == '(':
        t[0] = Pair(t[3], t[4])

def p_dip(t):
    'stmt : DIP body'
    body = t[2]
    i_count = len(t[1]) - 2
    def exec_dip(stack):
        top = []
        for _ in range(i_count):
            top.append(stack.pop(-1))
        for arg in body:
            stack = arg(stack)
        stack.extend(top[::-1])
        return stack
    t[0] = exec_dip

def p_statement_push(t):
    'stmt : PUSH type value'
    stack_type = t[2]
    val = t[3]
    def exec_push(stack):
        value = None
        if stack_type == Nat:
            value = Nat(val)
        elif stack_type == Int:
            value = Int(val)
        elif stack_type == Bool:
            value = Bool(val)
        elif stack_type == String:
            value = String(val)
        elif isinstance(stack_type, Pair):
            value = stack_type((val[0], val[1]))
        if value:
            t[0] = ['PUSH', stack_type, value]
            stack.append(value)
        else:
            print('type not implemented')
        return stack
    t[0] = exec_push

def p_statement_failwith(t):
    '''stmt : FAILWITH
            | FAIL'''
    cmd = t[1]
    def exec_failwith(stack):
        if cmd == 'FAILWITH':
            top = stack[-1]
        else:
            top = Unit
        print(f'fail with {top}')
        print('new stack\n\n')
        return []

    t[0] = exec_failwith

def p_error(t):
    print('syntax error')
    if t:
        print(f'{t.value}')

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Process Contract Interaction')
    parser.add_argument('--file', type=str)
    parser.add_argument('--repl', type=bool, const=True, nargs='?', default=True)
    parser.add_argument('--storage', const=True, nargs='?', default='Nat(1)')
    parser.add_argument('--parameter', const=True, nargs='?', default='Nat(2)')
    args = parser.parse_args()
    lexer = lex.lex()

    stack = []
    QUOTA = 1000
    remaining_steps = QUOTA

    repl = True
    parser = yacc.yacc()

    if args.file:
        storage = eval(args.storage)
        parameter = eval(args.parameter)
        p = Pair(storage.type, parameter.type)
        stack = [p((parameter, storage))]
        with open(f'contracts/{args.file}', 'r') as f:
            validate_indent(f.read())
            f.seek(0)

            first_line = next(f)
            second_line = next(f)
            assert first_line.split(' ')[0] == 'parameter'
            assert second_line.split(' ')[0] == 'storage'
            parameter_type = ' '.join(first_line.strip().split()[1:])[:-1]
            storage_type = ' '.join(second_line.strip().split()[1:])[:-1]

            print('parameter:', parameter_type)
            print('storage:', storage_type)

            # TODO: parse for indentation
            # TODO: this is a kludge
            code = next(f).replace('code', '', 1)
            code = '     ' + code.replace('{', '', 1) + f.read()
            code = code[::-1].replace('}', '', 1)[::-1]

            parser.parse(code)
            print(stack[::-1])
    if repl != 'F':
        while True:
            try:
                open = False
                s = input('stack > ')
                while s.count('{') > s.count('}'):
                    more = input()
                    s += more
            except EOFError:
                 break
            parser.parse(s)
            print(stack[::-1])
