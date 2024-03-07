def solution(n):
    pibo = [0,1]

    for k in range(1,n):
        pibo.append(pibo[k-1]+pibo[k])

    return pibo[-1] % 1234567


print(solution(5))