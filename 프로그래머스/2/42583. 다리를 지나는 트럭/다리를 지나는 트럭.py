# bridge_length = 트럭이 다리 건너는 시간인듯
# 1중포문에 while문 조금 곁들여서 가능할 것 같은데 해보기
# 근데, 다리를 건너고 있는 트럭의 '현재 상태'를 어떻게 표현하지?
    # 다리에 올라온(on) 트럭은 매초마다 진행을 해야함
# 아 근데 이러면 'times변수'관리가 좀 힘들거 같은데..

# 그냥 아예 처음부터 while로 시작하고, while의 매 반복은 +1초로 하자
def solution(bridge_length, weight, truck_weights):
    times = 1
    stack, running_stack = [], []

    # while한번에 1초 지남
    while len(truck_weights) != 0 or len(stack) != 0: 
        # step1: stack에 넣기
        if len(truck_weights) != 0 and sum(stack)+truck_weights[0] <= weight:
            running_stack.append(bridge_length) # 아래에서 바로 뺄거니까 +1해서 넣음
            stack.append(truck_weights.pop(0))
        
        # step2: 다리 건너기(진행)
            # 단, 최근에 들어온건 진행 노노 -> 위에서 length+1로 해결함
        running_stack = [running_stack[x]-1 for x in range(len(running_stack))]
        
        # step3: 다 건넌건 빼기
        if running_stack[0] == 0:
            stack.pop(0)
            running_stack.pop(0)
        
        # step4: 시간 세기
        times += 1
            

    return times


print(solution(2,10,[7,4,5,6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))