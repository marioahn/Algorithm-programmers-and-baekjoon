# 0. 끝 처리가 중요할 듯
def solution(s):
    result = 0
    x_cnt, other_cnt = 0, 0

    x = ''
    while s: # *끝 조건 더 다듬기
        x = s[0]
        for k in range(len(s)):
            if s[k] == x:
                x_cnt += 1
            else:
                other_cnt += 1
            
            if x_cnt == other_cnt:
                result += 1
                break # for문 나오기
            if k == len(s)-1: # 끝까지 나왔는데, 위에서 break x? -> 끝내기
                return result+1

        s = s[x_cnt+other_cnt:] # s분리하기
        if len(s) == 1:
            result += 1
            return result
        x_cnt, other_cnt = 0, 0 # 초기화
    
    return result

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
print(solution("abaabab"))