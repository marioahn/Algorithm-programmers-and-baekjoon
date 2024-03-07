# 흠.. 공통 최소공배수는 일단, 공통 최대공약수 구하고,
    # 각자를 그 값으로 나누고
    # 공통최대공약수 * 각 요소들곱하기면 됨
# for문 돌리면서 arr 모든 요소랑 동시에 나눠지는 최댓값n이 공최대공약수
    # 몇번 돌릴지? -> min(arr)까지

# python은 reduce함수 따로 import해와야하넹..


# 1트 - 전부 틀림;;(처음 예제케이스만 맞고)
    # 아 아니구나;; [2,6,7] -> 이거 답이 그럼 84? ㄴㄴ 42임
    # 모.든게 최대공약수로 나눠져야하는게 아님
    # 2개이상만 나눠져도 ok였던 거임..
# from functools import reduce

# def solution(arr):
#     common_num = 0
#     for k in range(1,min(arr)+1):
#         flag = True
#         for ele in arr:
#             if ele % k !=0:
#                 flag = False
#                 break
#         if flag==True:
#             common_num = k
    
#     return reduce(lambda x,y: x*y, arr) // (common_num**(len(arr)-1))

# print(solution([2,6,8,14])) # 168
# print(solution([3,6,9,5])) # 810 ?? -> 90이 나와야 함
# print(solution([2,6,7])) # 84?? -> 42가 나와야 함

# 2트
def solution(arr):
    common = max(arr)

    while 1:
        tmp_cnt = 0
        for ele in arr:
            if common % ele == 0:
                tmp_cnt += 1
            else:
                break
                
        # 배열 arr의 모든 값을 약수로 가지게 되는 경우 종료
        if tmp_cnt == len(arr):
            break
        common += 1
            
    return common

print(solution([2,6,8,14])) # 168
print(solution([3,6,9,5])) # 810 ?? -> 90이 나와야 함
print(solution([2,6,7])) # 84?? -> 42가 나와야 함
