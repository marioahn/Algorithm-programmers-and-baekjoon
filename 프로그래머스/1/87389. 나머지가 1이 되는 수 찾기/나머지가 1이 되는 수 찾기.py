def solution(n):
    for k in range(1,n):
        if n % k == 1:
            return k