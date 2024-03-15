# 뒷큰수: 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수
# 제한사항 -> O(N**2)는 X
    # 4 ≤ numbers의 길이 ≤ 1,000,000
    # 1 ≤ numbers[i] ≤ 1,000,000
# 아닌가? 근데 방법이 없지 않나? [9,1,5,3,6,2]에서 9는 무.조.건 모든 요소 다 살펴야 -1이 나오잖아
    # ! how............
    # 뭔가 느낌은 스택임이 분명한데. 생각이 안나네..

# 1트: 시간초과로 실패(19/23)
# def solution(numbers):
#     result = []
    
#     for i in range(len(numbers)-1):
#         flag = False
#         for j in range(i+1, len(numbers)):
#             if numbers[i] < numbers[j]:
#                 flag = True
#                 result.append(numbers[j])
#                 break # 필.수
        
#         if flag == False:
#             result.append(-1) # 뒷큰수가 없는 경우
   
#     result.append(-1) # 마지막은 무조건 -1
#     return result

# 2트 - stack
def solution(numbers):
    # 애초에 처음부터 -1쭉 해놓으면 마지막 경우 처리 안해도되네(마지막은 무조건 -1)
    result = [-1] * len(numbers)  
    stack = []
    
    for i, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num: # 여기 while이 핵심중 하나
            result[stack.pop()] = num
        stack.append(i)
    
    return result

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]