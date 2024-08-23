# 문자를 내림차순으로 정리
# 단, 소문자 > 대문자
# 대소문자 구분 -> 근데 파이썬은 sorted가 알아서 해주네..

def solution(s):
    return ''.join(sorted(s,reverse=True))
                          
def solution(s):
    return ''.join(sorted(s,reverse=True))