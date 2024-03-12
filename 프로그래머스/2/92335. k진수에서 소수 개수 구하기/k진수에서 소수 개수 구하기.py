# n을 0을 기준오르 split? 어차피 소수는 0 절대 못 들어가잖아
# 근데, n이 최대 100만자네.. 되려나
# 중복숫자도 cnt해줘야 함
def convert(num, base):
    T = "0123456789"  # k가 11이상이었으면, ABCDEF도 붙여줘야 함
    q, r = divmod(num, base)
    # 몫이 0이 될때까지
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def is_prime(num):
    if num == 1: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for k in range(3,int(num**(1/2))+1,2):
        if num % k == 0:
            return False
    return True

def solution(n, k):
    cnt = 0
    convert_k = convert(n,k)
    split_list = convert_k.split('0')
    print(split_list)
    for ele in split_list:
        if len(ele) >= 1 and is_prime(int(ele)):
            cnt += 1


    return cnt

print(solution(437674,3))
# print(solution(110011,10))
