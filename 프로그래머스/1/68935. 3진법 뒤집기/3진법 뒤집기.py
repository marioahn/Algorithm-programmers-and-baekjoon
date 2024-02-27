def solution(k):
    a = []
    while k >= 3:
        a.append(k % 3)
        k = k // 3 # 마지막 넣기
    a.append(k)

    a = a[::-1]
    
    sum = 0
    for k in range(len(a)):
        sum += (3**k)*a[k]
    
    return sum

print(solution(45))