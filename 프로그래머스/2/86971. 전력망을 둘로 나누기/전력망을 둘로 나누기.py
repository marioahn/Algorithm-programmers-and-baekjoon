# 그런데, 3분할 되는 경우는 없는가? -> 문제에선 2분할만 예정한 듯 보임
    # "당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할..."
# 흠;; 그냥.. dfs인가..? -> 정확히는 bfs
#  wires목록중에 요소 1개 없애도록 순회 돌고 - 맨 밖에서
    # 안에서 bfs함수 돌리는 것
    # bfs는 check만 하도록
# wire들의 연결 정보는 dict에 key-value에 저장하는게 나을듯
    # *근데 이 부분의 코드가 잘 안 짜짐 - key로 value값 찾아서 들어가지만 다시 나오는 경우가 특히.
    # https://wikidocs.net/196182보고 힌트깨달음 -> 일단 연결되었으면 다 value에 적어주면 되겠구나
        # 이에 따르면 이번 그래프는 '무방향'그래프
    # *[1,2]면 -> 1:2, 2:1이렇게 두개 하는거임 swap해서! - 있으면 추가x식으로~

    # 걍 dict하지말고({1:2} x) -> [1,2]해서 in으로 찾을까?
# visisited배열 선언해서, key, value둘다 접근한 경우 false->true로 바꿈
from collections import deque


def bfs(grp, length): # 인자로 뭐를 넣어야 할까
    connected = 0
    visited = [False] * (length+1) # 1인덱스가 1송전탑 방문여부
    queue = deque()
    now_key = list(grp.keys())[0]
    if not grp[now_key]:
        return length-1 # 여기서 끝
    visited[now_key] = True # key: 방문표시
    connected += 1

    queue.append(grp[now_key]) # [3,4,5]리스트 형태로 들어감 / 첫 시작

    while queue:
        now_values = queue.popleft()

        for value in now_values:
            if not visited[value]: # False상태면
                visited[value] = True
                connected += 1
                queue.append(grp[value])
        
    return abs(2*connected-length) # 2a-length가 a-b값임


def solution(n, wires):
    result = []

    for i in range(len(wires)):
        tmp = wires[:]
        tmp.pop(i)

        graph = {x: [] for x in range(1,n+1)} # key는 1부터 시작
        
        for [one,two] in tmp: # 이렇게도 되네 [one,two] zz
            if two not in graph[one]:
                graph[one].append(two)
            if one not in graph[two]:
                graph[two].append(one)
        result.append(bfs(graph,n))
    
    return min(result)

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4,[[1,2],[2,3],[3,4]]))
print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))