def solution(x, n):
    answer = [x]
    for k in range(2,n+1):
        answer.append(x*k)
    return answer        
        