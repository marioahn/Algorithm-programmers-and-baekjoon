# 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자
def solution(s):
    to_list = s.split(' ')
    answer = ''
    
    for i in range(len(to_list)):
        for j in range(len(to_list[i])):
            if (j%2) == 0:
                answer += to_list[i][j].upper()
            else:
                answer += to_list[i][j].lower()
        answer += ' ' # 각 단어마다 공백 추가
    
    answer = answer[:-1] # 마지막 공백 빼주기

    return answer


print(solution("try hello world")) # "TrY HeLlO WoRlD"