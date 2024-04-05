# 1
# dfs로 걍 하자. 도착하면 칸수 세고, min으로 계속 갱신시키고
# 그리고, 중요한건 레버를 가지고 있는 상태에서 e에 도착해야 탈출임
# 'e'칸이 방문된적 있다면 ok. 
# 흠.. 종료조건은 어떻게 하지 그럼. 영원히 뺑뺑이는 안되잖아
# 예제2보고 생각좀 해보자
# 잠깐. 왜 돌아와도 되는 경우가 생기는가? - 왜 start,exit중복  접근가능 조건이?
    # 구석에 열쇠가지러 가고 중간지점인 start거쳐서 end가는 경우!
    # 그럼 visited로는 안되겠는데?
# 와 레버조건 하나 추가된거 뿐인데 구도가 아예 달라지네
    # * -> 아니다. 다시 생각해보니, 아예 달라지는건 아님
    # * 다만, 종료조건 등이 추가되는 것 뿐 / visited안 쓰고
# 아 종료조건 -> 일단 어찌되었든한 지점에서 4방향으로 갈 수 밖에 없잖아
    # -> 근데 이때 4방향 모두 지나갈 수 없다면? 현재 지점은 똑같을 것임
    # 한번더 dfs재귀 들어갔는데 현재 상태가 똑같다면 return식으로 첫 줄에 적든지
    # etc..
    # 근데 최종 종료는 어떻게 할지..가로,세로 최대길이는 100이니까
        # *level이 20000이하로? ->너무 에바; -> 폐기

# todo 아. 아니다. 이렇게 하지말고, 단계를 2개로 나누면 된다
    # 1)Start에서 레버로 가는 최단 경로
    # 2)레버에서 End로 가는 최단 경로
    # * 근데 여전히, 갈 수 없는 경로 혹은 종료조건은 how? -> 걍 레버, 혹은 end를 못 찍으면 -1이지
    # 아. 그냥 bfs로 가면 될듯 한데? 인자에 level인자 추가해주면 몇번째 칸인지도 확인 가능
    # 해당칸이 레버면 ok인거지 ㅇㅇ. -> bfs기본인데;; 어이구
    # 쨋든, 이렇게 하면 왔다갔다 조건도 따로 고려할 필요는 없을듯?
from collections import deque

# 여기에서는 visited가 필요함 -> 뺑글뺑글 돌아가므로
# 전체적으로 봤을 때는 visited를 하면 안되는 것처럼 보이지만, 부분적으로 봤을 때는 설정해야 한다
ways = [[0,1],[0,-1],[1,0],[-1,0]]
def bfs(sx,sy,target_str,maps, cnt): # 시작지점 및 목표 문자('L',혹은 'E') & 원본
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    visited[sx][sy] = True
    q = deque()
    q.append([sx,sy,0]) # [x,y]형태로

    while q:
        x,y,tmp_cnt  = q.popleft()
        for way in ways: # 4번
            tmp = tmp_cnt
            nowx, nowy = x+way[0], y+way[1]
            if (0<=nowx<len(maps)) and (0<=nowy<len(maps[0])) and visited[nowx][nowy] == False:
                if maps[nowx][nowy] == 'X': continue
                else:
                    if maps[nowx][nowy] == target_str:
                        cnt += (tmp+1)
                        return cnt
                    visited[nowx][nowy] = True
                    q.append([nowx,nowy, tmp+1])
    
    return 0

def solution(maps):
    # s, k, e 좌표 찾기
    start, key = '', ''
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = [i,j]
            if maps[i][j] == 'L':
                key = [i,j]

    cnt = 0
    # Step1: start -> key
    cnt += bfs(start[0],start[1],'L',maps, 0)
    if cnt == 0: # 레버로 못 가는 경우, -1 바로 return
        return -1 
    
    # Step2: key -> end
    step_two = bfs(key[0],key[1],'E',maps, 0)
    if step_two == 0:
        return -1
    else:
        cnt += step_two
        return cnt


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOXE"]))
print(solution(["SOOOL","OOOOX","OOOOO","OOOOO","EOOOO"]))

print(solution(["LXOOSO","XOOOOO","OOOOOO","XOOOOO","EXOOOO"]))