# 제한사항
    # 1 ≤ k ≤ tangerine의 길이 ≤ 100,000
    # 1 ≤ tangerine의 원소 ≤ 10,000,000
# 흠.. 먼가 과정 줄일 수 있지 않을까 싶은데..

def solution(k, tangerine):
    just_maxcheck = max(tangerine)
    dict = {x: 0 for x in range(1, just_maxcheck+1)}
    for ele in tangerine:
        dict[ele] += 1

    for_sort_list = []
    for i in range(1,just_maxcheck+1):
        for_sort_list.append([i,dict[i]])
    for_sort_list.sort(reverse=True, key=lambda x:x[1])

    types = 0
    for ele in for_sort_list:
        types += 1
        k -= ele[1]
        if k<=0:
            return types


print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4,[1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2,[1, 1, 1, 1, 2, 2, 2, 3]))