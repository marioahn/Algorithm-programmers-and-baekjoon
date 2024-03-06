def solution(s):
    s = list(map(int,s.split(' ')))
    
    return f"{min(s)} {max(s)}"

print(solution("1 2 3 4"))