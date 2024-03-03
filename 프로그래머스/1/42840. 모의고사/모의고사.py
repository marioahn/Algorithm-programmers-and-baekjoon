# 최다정답자가 여러 명일 경우, 한 번에 어떻게 출력할지?

def solution(answers):
    result = []
    one, one_count = [1,2,3,4,5], 0
    two, two_count = [2,1,2,3,2,4,2,5], 0
    three, three_count = [3,3,1,1,2,2,4,4,5,5], 0

    for k in range(len(answers)):
        if one[k%5] == answers[k]:
            one_count += 1
        if two[k%8] == answers[k]:
            two_count += 1
        if three[k%10] == answers[k]:
            three_count += 1
    
    max_num = max(one_count,two_count,three_count)

    if one_count == max_num: result.append(1)
    if two_count == max_num: result.append(2)
    if three_count == max_num: result.append(3)

    return result