# 1 ≤ order의 길이 ≤ 1,000,000
# 기.존 상자는 1,2,3,4,5 순서대로 있음
# 1트.. 실패 및 너무 장황해서 다시
# def solution(order):
#     cnt = 0
#     main_container = [x+1 for x in range(len(order))]
#     main_container.reverse() # pop하기 위해
#     order.reverse()
#     sub_container = [] # stack

#     while 1:
#         while 1:
#             sub_container.append(main_container.pop())
#             if sub_container[-1] == order[-1]:
#                 order.pop()
#                 cnt += 1
#                 break
#     return cnt

# 2트 - 레퍼런스
def solution(order):
    stack = []
    index = 0 # order관리

    for num in range(1, len(order) + 1): # 아.여기가 메인컨테이너 그 자체네
        stack.append(num) # 난 메인컨테이너 리스트 위에서 선언하고 했는데, 훨씬 간편하다;;
        
        # 2개 조건 중, 선제조건은 stack이 비어있으면x
        while stack and stack[-1] == order[index]:
            stack.pop()
            index += 1


    return index


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))