# 이건 dfs로 가야할 것 같은데 bfs로 방법이 있나?
    # bfs로 limit설정하면서 배달거리 측정이..쉽지않을것 같은데
    # bfs적 접근은 아닌게 - k이하경로로 가는 "최단거리"의 일종임 - (min은 아니지만)
# backtracking필수
# 1번에서 배달을 갈 수 있는 '마을의 개수'
    # arrived배열로 도착하면 True식으로 하면 될듯
    # 근데 경로가 여러개인게 좀 걸리네 흠.. 어제문제랑 비슷한 줄 알았는데
    # 살짝 더 꼰 느낌인데
# 제한은 없음. 단 주의사항 2개
    # 두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다 -> 낮은 도로 선택
    # 임의의 두 마을간에 항상 이동 가능한 경로가 존재합니다 -> 섬같은 마을은 없다는 뜻
        # 즉, 어떠한 경로로든 1번에서 모.든 마을까진 갈 수 있음
        # 단, 리밋제한이 있다는 것을 고려

# 1)일단, 그래프화 시키는게 먼저인데, 이게 잘 안됨 -> 정보만 뽑아내면 dfs돌리면 효율은 어찌되든 끝나는데
# 2)힌트보니까, 플로이드 알고리즘이래 - (vs 다익스트라 - 검색)
    # https://it-garden.tistory.com/247
    # 동빈쓰: https://blog.naver.com/PostView.naver?blogId=ndb796&logNo=221234427842&parentCategoryNo=&categoryNo=128&viewDate=&isShowPopularPosts=false&from=postView
    
# 3) -> 최단거리이므로 "다익스트라" 사용하는 것이 더 바람직!
    # 근데 다시 보니까 그냥 이것저것 고민할 필요도 없이 다익스트라 문제였음..
    # 진짜 너무 오래놨다..
    # 블로그 코드 참조
    # https://blog.naver.com/PostView.naver?blogId=ndb796&logNo=221234424646&redirect=Dlog&widgetTypeCall=true&directAccess=false
    # 예전에도 배웠지만, 너무 스마트한 알고리즘..
import heapq

# heapq는 heap'queue' -> deque할때랑 방식 비슷함
# dijkstra에서 재방문지점(visited)을 설정하면 안되는 이유 및 안 한 이유?
    # 여러 지점을 따라 경로를 이동해야 하므로 중복지점도 다시 지나가야 한다. -> 백트랙킹하면 되지 않느냐?
    # 어차피 "최단경로"(최솟값)를 갱신할 것이기 때문에 지금은 ok
    # adj: 인접
# 무한대: float('inf') or '-inf' - 꼭 float붙여야
def dijkstra(dist,adj): 
    # 출발노드를 기준으로 각 노드들의 최소비용 탐색
    heap = []
    heapq.heappush(heap, [0,1])  # 거리,노드 (1번은 출발마을이니 cost 0)
    while heap:
        cost, node = heapq.heappop(heap)
        for c,n in adj[node]:
            if cost+c < dist[n]:
                dist[n] = cost+c
                heapq.heappush(heap, [cost+c,n])


def solution(N, road, K):
    dist = [float('inf')]*(N+1)  # dist 배열 만들고 최소거리 갱신할 것
    dist[1] = 0  # 1번은 자기자신이니까 거리 0 & 행렬처럼 2중배열x -> 1번에서만 출발할 것이니까
    adj = [[] for _ in range(N+1)]  # 거리&인접노드를 기록할 배열
    for r in road:
        adj[r[0]].append([r[2],r[1]])
        adj[r[1]].append([r[2],r[0]])
    dijkstra(dist,adj)
    return len([i for i in dist if i <=K])

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))

