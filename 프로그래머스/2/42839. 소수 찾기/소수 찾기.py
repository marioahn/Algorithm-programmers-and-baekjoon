# 1. 소수찾기 함수 만들기
# 2. '순열'뽑기
    # 몇개 뽑을것인가? -> len(numbers)만큼 반복하기
# 단, 중복은 미리 제거해야하며
# 011 = 11임을 명심
from itertools import permutations
import math

def is_prime(num):
    if num == 2: return 1
    if num == 1: return 0
    if num % 2 == 0: return 0
    
    for k in range(3,math.floor(num**(1/2))+1,2):
        if num % k == 0:
            return 0
    return 1


def solution(numbers):
    cnt = 0
    numbers = list(numbers)

    permutation_set = set() # ()는 tuple임
    for i in range(1, len(numbers)+1):
        np_k = list(map(list,permutations(numbers,i)))
        np_k2 = list(map(''.join, np_k)) # join(인자) 안써도 됨. map함수 안에서는
        # ['12', '13', '21', '23', '31', '32'] 
        for ele in np_k2:
            permutation_set.add(int(ele))


    for permutation in permutation_set:
        if is_prime(permutation):
            cnt += 1

    return cnt


print(solution('17'))
print(solution('011'))
