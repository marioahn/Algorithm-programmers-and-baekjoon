# 1. nums숫자중, 3개를 고르는 '조합' -> sum
# 2. 소수인지 판별
import math
from itertools import combinations

def is_prime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    cnt = 0
    perm = list(combinations(nums,3))

    for ele in perm:
        if is_prime(sum(ele)): # True면
            cnt += 1

    return cnt