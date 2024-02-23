# def solution(n):
#     # 3항 연산자
#     sqrt = n**(1/2)
#     return (sqrt+1)**2 if type(sqrt)==int else -1 # 11.0은 int가 아니라 안됨

def solution(n):
    sqrt = n**(1/2)
    return (sqrt+1)**2 if (sqrt%1 == 0) else -1