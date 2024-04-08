# 1.
# 이건 goal에 "도달"이라기보다는 얼음판 위에서 미끄러져서 goal"벽"에 닿을 수 있냐 없냐임
# G주위(=사방위)에 D 혹은 벽이 없으면 일단 절-대 도달할 수 없음
# *이때, 도달할 수 없는 경우 -1를 설정해줘야 하는데,
    # 뺑뺑이 돌게 되는 경우를 생각해야 한다 -> while이 안 끝날 수 있으므로
    # 흠. visited설정해서? -> 근데 다른 경로에서 해당 지점 방문하는 경우?
        # 각 루트별로 visited설정하는 것도 번거로울 듯
    # ? 아. 각 지점에 ncnt를 입력시켜놓고, 현재의 ncnt가 이전의 ncnt보다 크면 진입x
        # 이렇게 하면 복잡하게 visited설정안해도 될듯
        # -> 아니다. 원본 바꿀바에 그냥 visited 걍 만들어서 표시하자 1,0대신에 방문횟수로
from collections import deque

def bfs(start,maps):
    width, height = len(maps[0]), len(maps)
    visited = [[float('inf')]*width for _ in range(height)]
    visited[start[0]][start[1]] = 0 # 재방문 방지

    q = deque()
    q.append([start[0],start[1],0]) # 초기값 + 초기 cnt
    ways = [[0,-1],[0,1],[-1,0],[1,0]] # 좌우상하
    while q:
        x, y, cnt = q.popleft()
        if maps[x][y] == "G":
            return cnt # bfs이므로 최솟값 ok
        
        for way in ways:
            nx, ny = x,y
            while True: 
                nx, ny = nx+way[0], ny+way[1] # 여기에!
                
                if not((0<=nx<height) and (0<=ny<width)): # 벽전까지만 ok
                    nx, ny = nx-way[0], ny-way[1] # -임
                    if cnt < visited[nx][ny]:
                        # cnt += 1 # ? +1맞나?
                        visited[nx][ny] = cnt+1
                        q.append([nx,ny,cnt+1])
                    break
                
                if maps[nx][ny] == "D": # *이게 벽끝조건보다 선행되어야 함
                    nx, ny = nx-way[0], ny-way[1]
                    if cnt < visited[nx][ny]:
                        visited[nx][ny] = cnt+1 # ? +1맞나?
                        q.append([nx,ny,cnt+1])
                    break
                

    return -1 # 위에서 return안되면 G도달 못했다는 뜻


def solution(board):
    # 1. R,G좌표 찾기
    r = ''
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                r = [i,j]

    return bfs(r,board)

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])) # 7
print(solution([".D.R", "....", ".G..", "...D"])) # -1