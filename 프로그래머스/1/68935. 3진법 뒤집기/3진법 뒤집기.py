def solution(n):
    tmp = []
    while n>=3:
        tmp.append(n%3)
        n = n//3
    tmp.append(n)
    
    tmp = tmp[::-1]
    
    sum = 0
    for k in range(len(tmp)):
        sum += (3**k)*tmp[k]
    
    return sum