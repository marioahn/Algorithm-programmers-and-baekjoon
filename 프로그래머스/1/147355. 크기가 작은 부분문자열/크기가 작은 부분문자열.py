def solution(t, p):
    cnt = 0
    for k in range(len(t)-len(p)+1):
        if int(t[k:k+len(p)]) <= int(p):
            cnt += 1
    
    return cnt
