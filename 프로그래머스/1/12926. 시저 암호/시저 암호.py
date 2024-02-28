# 아스키 코드밖에 생각이 안 나는데 어떻게 하더라
# 대소문자 구별

def solution(s, n):
    low_str = [chr(x) for x in range(97,123)]
    up_str = [chr(x) for x in range(65,91)]

    result = ''
    for ele in s:
        if ele == ' ':
            result += ele
        else: # n만큼 밀기
            if ele.isupper(): # ele가 대문자라면
                result += up_str[(ord(ele)-65+n)%26]
            else: # 소문자라면
                result += low_str[(ord(ele)-97+n)%26]
            
    return result

print(solution("a B z",4))