""" Super ugly, but works kind of """


def get_first_char(line):
    return len(line) - len(line.lstrip())


def validate_indent(text):
    lines = text.split('\n')[2:]
    lines[0] = lines[0].replace('code', '    ')
    lines[0] = lines[0].replace('{', ' ')
    first_indent = get_first_char(lines[0])
    indent_stack = [first_indent]
    for line in lines:
        if line.strip() == '':
            continue
        if line.strip() == '}':
            indent_stack.pop(-1)
            continue
        if line.find('{') == -1:
            if get_first_char(line) != indent_stack[-1]:
                return False
            if line.find('}') != -1:
                if line.find('}') != (len(line) - 1):
                    indent_stack.pop()
                    return False
        else:
            open_bracket = line.find('{')
            line =  ' ' * open_bracket + line[open_bracket + 1: ]
            indent_stack.append(get_first_char(line) + 1)
    return True


if __name__ == '__main__':
    assert validate_indent("""parameter (list int);
    storage (list int);
    code { ABC;
           DEF; { GHI;
                  JKL;
                }
    }
    """) == True

    assert validate_indent("""parameter (list int);
    storage (list int);
    code { ABC;
           DEF; { GHI;
                 JKL;
                }
    }
    """) == False
