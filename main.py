from arithmetic_operations import expr


if __name__ == '__main__':
    expression = b"1 + ( 3 - 2 ) * ( 2 - 1 ) "
    program_state = {'cur': 0}
    val = expr(expression, program_state)
    print(val)