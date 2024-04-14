# 1
# 배열은 시간순으로 정렬되어 있지 않을 수 있다
# 과제이름은 중복되지 않는다
# 멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작 -> 대놓고 stack쓰라는 것 같은데?
# 과제가 중간에 끊기면 남은 정보를 담는 dict가 필요할 듯 - 아니면 [과제,남은시간]으로 저장하든지

def solution(plans):
    stack = []
    answer = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h*60 + m
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])
    
    for i in range(len(plans)-1):
        stack.append([plans[i][0], plans[i][2]])
        gap = plans[i+1][1] - plans[i][1]
        while stack and gap:
            if stack[-1][1] <= gap:
                cn, ct = stack.pop()
                gap -= ct
                answer.append(cn)
            else:
                stack[-1][1] -= gap
                gap = 0
                
    answer.append(plans[-1][0])
    
    for i in range(len(stack)):
        answer.append(stack[~i][0])
    return answer