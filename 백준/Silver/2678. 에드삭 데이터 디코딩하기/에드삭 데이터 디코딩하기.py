def bin_to_float(s: str) -> float:
    s = s[:]
    result = 0.0
    minus = True
    if s[0] == "0":
        minus = False
    pow = [
        2,
        4,
        8,
        16,
        32,
        64,
        128,
        256,
        512,
        1024,
        2048,
        4096,
        8192,
        16384,
        32768,
        65536,
    ]
    if not minus:
        for i in range(1, len(s)):
            if s[i] == '1':
                result += 1/pow[i - 1]
        return result
    else:
        tmp_s = ''
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                tmp_s += '0'
                s = s[:i]
                for j in range(len(tmp_s) - 1, -1, -1):
                    s += tmp_s[j]
                break
            tmp_s += '1'
        
        for i in range(1, len(s)):
            if s[i] == '0':
                result += 1/pow[i - 1]
        return -result


s = "PQWERTYUIOJ#SZK*?F@D!HNM&LXGABCV"
dic = {}
for v, k in enumerate(s):
    dic[k] = f"{bin(v)[2:]:0>5}"


p = int(input())
for tc in range(p):
    c, d, s = input().split()
    d = int(d)
    if c == '?' and d == 0 and s == 'F':
        print('-1.0')
        continue
    tmp = dic[c] + f"{bin(d)[2:]:0>11}"
    if s == "D":
        tmp += "1"
    else:
        tmp += "0"
    answer = f'{bin_to_float(tmp):.16f}'
    new_answer = ''
    
    zero_checker = True
    for i in range(len(answer) - 1, 0, -1):
        if answer[i - 1] == '.':
            new_answer += answer[i]
            continue
        
        if zero_checker:
            if answer[i] == '0':
                continue
            else:
                new_answer += answer[i]
                zero_checker = False
        else:
            new_answer += answer[i]
    new_answer += answer[0]
    
    for i in range(len(new_answer) - 1, -1, -1):
        print(new_answer[i], end='')
    print()