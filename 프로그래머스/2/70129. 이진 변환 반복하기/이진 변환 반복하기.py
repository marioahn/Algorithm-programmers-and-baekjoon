
# s의 길이는 1 이상 150,000 이하
# s에는 '1'이 최소 하나 이상 포함되어 있다
# '10'이 되면 그냥 바로 cnt +=1, zero_cnt +=1 하고 종료시키기


# 1트 - 시간초과 실패(7/11)
    # s는 최대 150,000인데 계속 s를 가지고 변환시키는게 비효율적
# def solution(s):
#     try_cnt, zero_cnt = 1, 1
#     # count함수, replaceALL을 쓸건데, 너무 길지않나
#         # 이중포문, 시간복잡도(2*(N**2)인셈인데)
#     while s != '10':
#         zero_cnt += s.count('0')
#         s = s.replace('0','') # 이 부분 수정 필요
#         s = bin(len(s))[2:]
#         try_cnt += 1

#     return [try_cnt, zero_cnt]

# --------------------

# 1-2트 - 시간초과 실패(7/11)
    # 똑같네.. 근본적인 해결책은 아닌듯
def solution(s):
    try_cnt, zero_cnt = 0, 0

    while s != '1':
        tmp_zero = s.count('0')
        zero_cnt += tmp_zero #
        tmp_len = len(s)-tmp_zero # 

        s = bin(tmp_len)[2:]
        try_cnt += 1

    return [try_cnt, zero_cnt]


print(solution("110010101001"))