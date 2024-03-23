# 제한조건:
    # 3 ≤ maps의 길이 ≤ 100 / 3 ≤ maps[i]의 길이 ≤ 100
    # maps[i]는 'X' 또는 1 과 9 사이의 자연수로 이루어진 문자열
    # 지도는 직사각형 형태

# flood fill문제 같은데, 기초문제인듯
    # start는 0,0에서 시작한다 치고 언제 멈추는가? -> sx,sy가 맵끝(우측하단)에 도달할 때?
    # 이중포문, dfs가 아니라 bfs로 풀어야 함
from collections import deque

def solution(maps):
    width, height = len(maps[0]), len(maps)
    visited = [[0]*width for _ in range(height)]
    directions = [[0,1],[1,0],[0,-1],[-1,0]] # 우하좌상

    result = []
    for i in range(height):
        for j in range(width):
            sum = 0
            if maps[i][j] != 'X' and visited[i][j] == 0:
                q = deque()
                q.append([i,j])
                visited[i][j] = 10
                sum += int(maps[i][j])

                while q:
                    x, y = q.popleft()
                    for dx,dy in directions:
                        nowx, nowy = x+dx, y+dy
                        if 0 <= nowx < height and 0 <= nowy < width and maps[nowx][nowy] != 'X':
                            if not visited[nowx][nowy]:
                                visited[nowx][nowy] = 1
                                sum += int(maps[nowx][nowy])
                                q.append([nowx,nowy])
            
            if sum != 0:
                result.append(sum)
                        
                

    return sorted(result) if len(result) != 0 else [-1]


print(solution(["X591X","X1X5X","X231X", "1XXX1"])) # [1,1,27]
print(solution(["XXX","XXX","XXX"])) # [-1]