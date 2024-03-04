# # 그런데, 최고등수/최저등수를 result에 추가하는 과정이 너무 번잡해보임 -> 더 simple?
# def solution(lottos, win_nums):
#     result = []
#     lotto_rank = [6,5,4,3,2] # 6점이 1등(1 idx), 2점이 5등(5 idx)
#     zero_cnt = lottos.count(0)
#     basic = 0
#     for lotto in lottos:
#         if lotto == 0: continue
#         if lotto in win_nums:
#             basic += 1   

#     # index()는 찾는 값이 없으면 -1이 아니라 에러
#     # find()는 -1 반환 -> 근데, find쓰자고 lotto_rank를 문자열로 바꾸는건 좀..
#             # 더 스마트한 방식 생각해보기 -> not in사용하기
#     # 1) 최고등수
#     if (basic+zero_cnt)>= 6:
#         result.append(1)
#     elif (basic+zero_cnt) not in lotto_rank:
#         result.append(6)
#     else:
#         result.append(lotto_rank.index(basic+zero_cnt)+1) # 최고
#     # 2)최저등수
#     if basic not in lotto_rank:
#         result.append(6)
#     else:
#         result.append(lotto_rank.index(basic)+1)

#     return result


# print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19])) # 3,5
# print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25])) # 1 6
# print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35])) # 1 1
# print(solution([1,7,7,7,7,7], [1,2,3,4,5,6]))


# 레퍼런스 -> 더 simple
def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    zero_cnt = lottos.count(0)
    basic = 0
    for x in win_nums:
        if x in lottos:
            basic += 1
    
    return [rank[zero_cnt+basic], rank[basic]]