# 1트 - 실패
    # 공통요소를 처음부터 제거하고 시작했는데,
    # 문제의 핵심은 lost의 수를 최대로 줄이는 것
    # 근데, 아래코드처럼 하면
    # print(solution(5,[1,2,3],[3,4,5]))를 대처할 수가 없음..
    # 
# def solution(n, lost, reserve):
#     # 1. lost, reserve에 공통 요소 제거
#     for i in lost:
#         if i in reserve:
#             lost.remove(i)
    
#     # 0. 정렬
#     lost.sort()
#     reserve.sort()
    
#     # 2. reserve순회하면서, lost커버쳐주기 -> lost 최대한 줄이기
#     for j in reserve:
#         if ((j-1) in lost):
#             lost.remove(j-1)
#         elif ((j+1) in lost):
#             lost.remove(j+1)

#     return n-len(lost)


# ---
# 2트 - 실패..(25/30)
    # 뭐가 또 부족한가..
    # 어떤 반례가 있나? - 아 이번엔 또 반대로, 같은건 처리안했네 ㅋㅋ
    # -> 근데 여전히 (27/30)임..
    # 아. 공통요소빼는게 맞네 다시 생각해보니까..
        # 자기가 도난당하면, 다른 사람 못 빌려주잖아..

# def solution(n, lost, reserve):
#     # 0. 정렬
#     lost.sort()
#     reserve.sort()
    
#     # 1. reserve순회하면서, lost커버쳐주기 -> lost 최대한 줄이기
#     for j in reserve:
#         if ((j-1) in lost): # j+1보다 j-1먼저 하는게 중요
#             lost.remove(j-1)
#         elif ((j) in lost): # 이거 추가
#             lost.remove(j)
#         elif ((j+1) in lost):
#             lost.remove(j+1)

#     return n-len(lost)


# ---
# 3트 - 1트의 공통요소 제거 코드 추가 & lost커버쳐줄때, j in lost조건 빼기
def solution(n, lost, reserve):
    # 0. 정렬
    lost.sort()
    reserve.sort()

    
    # 1-0. for문에서 lost.remove(i)하면 for문이 제대로 돌아가겠냐..?
        # 근데, 얕은복사로 해야, 원본도 안 바뀜
    tmp = lost[:] # tmp=lost하면 안됨
    # 1. lost, reserve에 공통 요소 제거    
    for i in lost:
        if i in reserve:
            tmp.remove(i)
            reserve.remove(i) # 이걸 1트에서 안했었음
    
    # 2. reserve순회하면서, lost커버쳐주기 -> tmp 최대한 줄이기
    for j in reserve:
        if ((j-1) in tmp):
            tmp.remove(j-1)
        elif ((j+1) in tmp):
            tmp.remove(j+1)

    return n-len(tmp)


print(solution(3,[3],[1])) # 2
print(solution(5,[1,2,3],[3,4,5])) # 3
print(solution(5,[4,5],[3,4])) # 4
print(solution(5,[1,2,3],[1,2,3])) # 5