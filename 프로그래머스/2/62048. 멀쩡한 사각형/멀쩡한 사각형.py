import math

# 규칙찾기..
def solution(w,h):
    return (w*h)-(w+h-math.gcd(w,h))