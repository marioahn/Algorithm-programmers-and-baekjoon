# str.isalpha() -> 주어진 문자열이 알파벳으로만 구성되어있는가?
# 근데, 풀고나서 생각난건데, 첫글자가 숫자든 아니든 상관없었네..
# 어차피 '3'.upper()한다고 에러나는건 아니니까..
def solution(s):
    s = s.lower() # 일단 싹 다 lower
    s = s.split(' ')

    result = ''
    for ele in s:
        if ele.isalpha(): # True면
            result += ele[0].upper() + ele[1:]
        else:
            result += ele
        result += ' '

    return result[:-1] # 마지막 공백제거

print(solution("3people unFollowed me"))