from parse import match

# 四则运算文法如下，目标：输入表达式(str)，输出值(float或者int)

# 左递归:
'''
<expr> ::= <expr> + <term>
         | <expr> - <term>
         | <term>

<term> ::= <term> * <factor>
         | <term> / <factor>
         | <factor>

<factor> ::= ( <expr> )
           | Num
           
1 + (3 - 2) * (2 - 1)
'''

# 消除左递归后
'''
<expr> ::= <term> <expr_tail>
<expr_tail> ::= + <term> <expr_tail>
              | - <term> <expr_tail>
              | <empty>

<term> ::= <factor> <term_tail>
<term_tail> ::= * <factor> <term_tail>
              | / <factor> <term_tail>
              | <empty>

<factor> ::= ( <expr> )
           | Num
'''

# 返回该表达式的值
def expr(src, program_state) -> int:
    if program_state['cur'] >= len(src): # 处理异常
        print(f"expected complete expression")
        exit(-1)

    lvalue: int = term(src, program_state)
    return expr_tail(lvalue, src, program_state)

def factor(src, program_state)-> int:
    if program_state['cur'] >= len(src): # 处理异常
        print(f"expected complete expression")
        exit(-1)

    if src[program_state['cur']] == ord('('): # ( <expr> )
        match(ord('('), src, program_state)
        return_val = expr(src, program_state)
        # 清除前面空格
        while src[program_state['cur']] == ord(' ') or src[program_state['cur']] == ord('\t'):
            program_state['cur'] += 1
        match(ord(')'), src, program_state)
    else: # Num
        match(5, src, program_state)
        return_val = program_state['cur_num']

    return return_val


def term_tail(left_value, src, program_state) -> int:
    if program_state['cur'] >= len(src): # 处理异常
        return left_value

    if src[program_state['cur']] == ord('*'):
        match(ord('*'), src, program_state)
        value: int = left_value * factor(src, program_state)
        return term_tail(value, src, program_state)
    elif src[program_state['cur']] == ord('/'): # 只有整数
        match(ord('/'), src, program_state)
        value: int = left_value // factor(src, program_state)
        return term_tail(value, src, program_state)
    else:
        return left_value


def term(src, program_state) -> int: # factor term_tail
    if program_state['cur'] >= len(src): # 处理异常
        print(f"expected complete expression")
        exit(-1)

    lvalue: int = factor(src, program_state)
    return term_tail(lvalue, src, program_state)

def expr_tail(left_value, src, program_state) -> int:
    if program_state['cur'] >= len(src): # 处理异常
        return left_value

    if src[program_state['cur']] == ord('+'): #  + term expr_tail
        match(ord('+'), src, program_state)
        value: int = left_value + term(src, program_state)
        return expr_tail(value, src, program_state)
    elif src[program_state['cur']] == ord('-'): #  - term expr_tail
        match(ord('-'), src, program_state)
        value: int = left_value - term(src, program_state)
        return expr_tail(value, src, program_state)
    else: # empty
        return left_value

