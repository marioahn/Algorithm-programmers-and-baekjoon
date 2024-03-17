# 제한: 1 ≤ x ≤ y ≤ 1,000,000
# 1트 - 런타임에러
    # 이건 dfs인것 같은데
    # 근데, 효율 너무 안좋음. 재귀 많이 돌아가는 경우 런타임 에러 뜸
    # 조건을 줘서 재귀를 덜 들어가게 할 수는 있을 것 같은데..
    # *특히 y가 매.우. 큰. 경우에 모.든 가능성을 탐.색하게 되어 비효율적이다
# def dfs(cnt, now, plus, target):
#     global result
#     if now > target:
#         return
#     if now == target:
#         result.append(cnt)
#         return 
    
#     dfs(cnt+1, now+plus, plus, target)
#     dfs(cnt+1, now*2, plus, target)
#     dfs(cnt+1, now*3, plus, target)

# def solution(x, y, n):
#     global result
#     result = []
#     dfs(0, x, n, y)

#     return min(result) if len(result) != 0 else -1

# 2트 - x->y가 아니라, y->x로 가면 됨..어우;; 어지러워
    # 어. 아냐.. 예시2에서 바로 cut됨. 최소탐색이 되어야 하는데,
    # 3으로 나누는게 빠를지, 2로 나누는게 빠를지 어떻게 알아..
    # 시도는 좋았다..!
# def solution(x, y, n):
#     count = 0
#     while y > x:
#         if y % 3 == 0:
#             y //= 3
#         elif y % 2 == 0:
#             y //= 2
#         else:
#             y -= n
#             if y < x:  # n을 뺀 결과 x보다 작아지면 변환이 불가능함
#                 return -1
#         count += 1
#     if y < x:  # 최종적으로 y가 x보다 작아진 경우
#         return -1
#     return count


# 3트 - bfs로 풀자..
    # * 애초에 bfs로 풀었어야 하는 문제인데 먼 dfs로 풀고 있었지;;? 다시 정리해야 할듯; 감다죽;;
    # * 단, bfs / dfs 차이 이해하고 이 문제, 시도코드들 다 합쳐서 til로 적기.
    # * 왜 bfs가 더 효율적인가?
    # BFS를 사용하면 x에서 시작하여 y에 도달할 때까지 가능한 모든 경로를 최단 경로 순으로 탐색
        # 너비 우선 탐색은 최단 경로를 보장하기 때문에,
        # 이 문제에서 요구하는 최소 연산 횟수를 정확히 찾을 수 있다
    # 각 단계마다 가능한 모든 다음 상태를 탐색하면서, 
    # 이미 방문한 상태는 다시 방문하지 않도록 함으로써 중복 계산을 방지한다
from collections import deque


# 아래처럼 bfs를 solution안에 넣으면 global dist이런거 안써도 됨
def solution(x,y,n):
    def bfs(x,y,n):
        q = deque()
        dist[x] = 1 # 시작점을 1트라이로
        q.append(x) # 시작점을 q에 추가

        while q:
            x = q.popleft() # x는 시작점ㅇㅇ
            if 0 <= x+n <= 1000000 and dist[x+n] == 0: # not visited
                dist[x+n] = dist[x] + 1 # cnt+1 & visited표시는 덤
                q.append(x+n)
            if 0 <= x*2 <= 1000000 and dist[x*2] == 0: # not visited
                dist[x*2] = dist[x] + 1
                q.append(x*2)
            if 0 <= x*3 <= 1000000 and dist[x*3] == 0: # not visited
                dist[x*3] = dist[x] + 1
                q.append(x*3)

    # bucket개념, dist[key]=value: key는 "값", value는 값에 도달하기 위한 횟수
    dist = [0] * 1000001 # 만약 요소가 0이면, 도달 못한다는 뜻임ㅇㅇ
    bfs(x,y,n)

    return dist[y]-1 

print(solution(10,40,5))
print(solution(10,40,30))