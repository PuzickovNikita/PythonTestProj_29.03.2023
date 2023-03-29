STOP_SUM = 200
MAX_DIGIT = 9

def gen_res(res_tmp, c):
    for i in range(len(res_tmp)):
        res_tmp[i] = [c] + res_tmp[i]
    return res_tmp

def calc(n, rest, current):
    if n < 0:
        if rest - current == 0:
            return [['.']]
        else:
            return []
    res = []
    # ставим пусто
    res_tmp = calc(n-1, rest, current*10 + n)
    if len(res_tmp) > 0:
        res += gen_res(res_tmp, ' ')
    # ставим плюс
    res_tmp = calc(n - 1, rest - current, n)
    if len(res_tmp) > 0:
        res += gen_res(res_tmp, '+')
    # ставим минус
    res_tmp = calc(n-1, rest - current, -n)
    if len(res_tmp) > 0:
        res += gen_res(res_tmp, '-')

    return res

def process_signs(signs):
    current_number = len(signs) - 1
    res_str = str(current_number)
    sum = 0
    current_digit = current_number - 1
    for sign in signs:
        if sign == ' ':
            res_str += str(current_digit)
            if current_number >= 0:
                current_number = current_number*10 + current_digit
            else:
                current_number = current_number*10 - current_digit
        elif sign == '+':
            res_str += '+' + str(current_digit)
            sum += current_number
            current_number = current_digit
        elif sign == '-':
            res_str += '-' + str(current_digit)
            sum += current_number
            current_number = -current_digit
        elif sign == '.':
            sum += current_number
            return res_str, sum
        current_digit -= 1

    raise TypeError("unexpected signs")

def process(res):
    for signs in res:
        res_str, sum = process_signs(signs)
        print(res_str + '=' + str(sum))

def print_ans(n, sum):
    process(calc(n-1, sum, n))

if __name__ == '__main__':
    print_ans(MAX_DIGIT, STOP_SUM)

