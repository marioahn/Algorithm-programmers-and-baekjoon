def solution(a, b, n):
    cnt = 0
    
    while a<=n:
        cnt += (n//a)*b
        n = n%a + (n//a)*b
    
    return cnt

print(solution(2,1,20))
