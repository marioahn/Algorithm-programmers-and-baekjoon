def solution(s):
    to_list = s.split(" ")
    answer = ''
    
    for i in range(len(to_list)):
        for j in range(len(to_list[i])):
            if (j%2 == 0):
                answer += to_list[i][j].upper()
            else: answer += to_list[i][j].lower()
        answer += " " # 공백
    
    answer = answer[:-1] # 마지막 공백 빼기
    
    return answer