# 제한사항
    # 1 ≤ k ≤ tangerine의 길이 ≤ 100,000
    # 1 ≤ tangerine의 원소 ≤ 10,000,000
# 흠.. 먼가 과정 줄일 수 있지 않을까 싶은데..
# def solution(k, tangerine):
#     just_maxcheck = max(tangerine)
#     dict = {x: 0 for x in range(1, just_maxcheck+1)}
#     for ele in tangerine:
#         dict[ele] += 1

#     for_sort_list = []
#     for i in range(1,just_maxcheck+1):
#         for_sort_list.append([i,dict[i]])
#     for_sort_list.sort(reverse=True, key=lambda x:x[1])

#     types = 0
#     for ele in for_sort_list:
#         types += 1
#         k -= ele[1]
#         if k<=0:
#             return types
# 추가적으로, 종류의 '수'만 cnt하면 된다
# 즉, 어떤 종류들이 골라지는지는 상관이 x;;
# 1트에서처럼 [key,value]가 필요없는 것
def solution(k, tangerine):
    just_maxcheck = max(tangerine)
    # 0번인덱스 = 허수, 1번인덱스 = 1번크기
    bucket = [0 for _ in range(0,just_maxcheck+1)]
    
    for ele in tangerine:
        bucket[ele] += 1
    bucket.sort(reverse=True)    

    types = 0
    for ele2 in bucket:
        types += 1
        k -= ele2
        if k<=0:
            return types
    
print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4,[1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2,[1, 1, 1, 1, 2, 2, 2, 3]))