# 1트 - 실패(7/20)
    # survey와 choices를 같이 순회하면서 점수 표를 만들고,
    # 비교하면서 유형 return (점수 같으면 사전 순)
    # [R T] / [C F] / [J M] / [A N]
    # 1 2 3 4 5 6 7 
    # 앞에것 3 - 2 - 1
    # 뒤에것 1 - 2 - 3
    # 4점은 continue
# ? 어 근데, 같은 유형의 점수가 2번 나오면? 덮어씌우면 되나 그냥?
    # '검사 결과는 모든 질문의 성격 유형 점수를 더하여' 문제에 나와있었음;;
    # 이거 반영해서 코드수정ㄱㄱ
def solution(survey, choices):
    answer = ''
    # 아래처럼 초기값 넣어줘야 survey반복문 돌릴 때, 존재않는 key에러가 안남
    dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0,}
    # choice[i]의 점수가 5이상이면 뒤의 문자 / 3이하면 앞의 문자점수
    score = [3,2,1, 0, 1,2,3]

    for k in range(len(survey)):
        if choices[k] >= 5:
            dict[survey[k][1]] += score[choices[k]-1]
        elif choices[k] <= 3:
            dict[survey[k][0]] += score[choices[k]-1]

    # =조건 넣으면, 사전순도 같이 처리되도록ㅇㅇ.
    answer += 'R' if dict['R'] >= dict['T'] else 'T'
    answer += 'C' if dict['C'] >= dict['F'] else 'F'
    answer += 'J' if dict['J'] >= dict['M'] else 'M'
    answer += 'A' if dict['A'] >= dict['N'] else 'N'
    
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])) # "TCMA"
print(solution(["TR", "RT", "TR"],[7, 1, 3])) # "RCJA"