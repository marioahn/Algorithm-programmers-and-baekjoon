def solution(n):
    result = []
    for k in range(len(str(n))-1,-1,-1):
        result.append(int(str(n)[k]))
    return result
        