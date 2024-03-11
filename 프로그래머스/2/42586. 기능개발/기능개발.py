# 1트 - 이렇게 까지 해야 할 문제인가?
# def solution(progresses, speeds):
#     result = []

#     while len(progresses) != 0:
#         progresses = [x+y for x,y in zip(progresses, speeds)]

#         # 앞에서부터 100이상인것들만 가져오고, 그 개수 추가 & 본체 slicing
#         for idx in range(len(progresses)):
#             if progresses[idx] >= 100:
#                 continue
#             else:
#                 if idx != 0: # 처음이 100이하면 result에 추가되면 안됨
#                     result.append(idx+1)
#                     progresses = progresses[idx+1:]
#                     speeds = speeds[idx+1:]
#                     break

#     return result

# 2. 2트
# 그냥, progresses길이만큼의 새 배열 만들고,
# 요소는 100이 되려면 몇일 기다려야하는지를 넣으면 됨
# 이제 앞에서부터 순회해서 뒤의 수가 앞의 수보다 클때까지만 돌리고 stop
# 그럼 한 방에 패치할 수 있는 기능 수가 나옴 -> 이거 반복
import math


def solution(progresses, speeds):
    deadline = []
    for x,y in zip(progresses, speeds):
        deadline.append(math.ceil((100-x)/y))
    
    if len(deadline) == 1: return [1]

    result = []
    start, end = 0, 0
    for idx in range(len(deadline)-1): # 아 근데, deadline길이가 1개면 안돌아가지
        if deadline[start] >= deadline[idx+1]: # deadline[idx]가 아니라, deadline[start]!
            end += 1
        else:
            result.append(end-start+1)
            start, end = idx+1, idx+1
        if end == len(deadline)-1:
            result.append(end-start+1)
    return result


print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
print(solution([1,2,3,4,5],[1,1,1,1,1]))
print(solution([5,4,3,2,1],[1,1,1,1,1]))
print(solution([0],[100]))
print(solution([98,99,98],[1,1,1])) # [3]가 나와야하는데, 내 처음 코드는 [2,1]이 나옴. 아. 처음에 조건처리가 미흡했다