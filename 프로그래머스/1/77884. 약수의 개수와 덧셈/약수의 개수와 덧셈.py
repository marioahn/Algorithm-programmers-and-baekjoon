def cnt_divisor(n):
    cnt = 1
    for k in range(2,n+1):
        if n%k == 0:
            cnt += 1
    return cnt
    

def solution(left, right):
    answer = 0
    for k in range(left, right+1):
        if (cnt_divisor(k) % 2 == 0):
            answer += k
        else: answer -= k
    
    return answer