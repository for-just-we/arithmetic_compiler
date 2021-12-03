
# program_state['cur']为当前遍历到的字符在字符串中的索引位置，用dict来记录索引值是因为python不支持引用传值，
# 欢迎大家提出更有效率的方式，当然，我个人还是希望尽量少用全局变量

# 这里next只返回Num类型，空格之后如果是数字就返回数字，否则返回空
def next_token(src: bytes, program_state: dict):
    # skip white space
    # *src -> src[program_state['cur']]
    token = src[program_state['cur']]
    program_state['cur'] += 1

    if token >= ord('0') and token <= ord('9'): # num
        token_val = token - ord('0')

        while src[program_state['cur']] >= ord('0') and src[program_state['cur']] <= ord('9'):
            token_val = token_val * 10 + src[program_state['cur']] - ord('0')
            program_state['cur'] += 1

        program_state['cur_num'] = token_val

    # 清除空格
    while program_state['cur'] < len(src) and (src[program_state['cur']] == ord(' ') or src[program_state['cur']] == ord('\t')):
        program_state['cur'] += 1
    if program_state['cur'] >= len(src): # 处理异常
        return


def match(tk: int, src: bytes, program_state: dict):
    # 清除头部空格
    while program_state['cur'] < len(src) and (
            src[program_state['cur']] == ord(' ') or src[program_state['cur']] == ord('\t')):
        program_state['cur'] += 1
    if program_state['cur'] >= len(src): # 处理异常
        if tk == 5:
            print(f"expected token: Num, however missed")
        else:
            print(f"expected token: {chr(tk)}, however missed")
        exit(-1)

    if tk == 5: # match(Num)
        if src[program_state['cur']] < ord('0') and src[program_state['cur']] > ord('9'):
            print(f"expected token: Num, got: {chr(src[program_state['cur']])}")
            exit(-1)

    elif src[program_state['cur']] != tk:
        print(f"expected token: {chr(tk)}, got: {chr(src[program_state['cur']])}")
        exit(-1)
    next_token(src, program_state)


if __name__ == '__main__':
    expr = b"1 + 2"
