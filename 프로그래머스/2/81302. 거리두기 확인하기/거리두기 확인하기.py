# 일단 노가다로 풀어보자 -> 다른 사람은 어떻게 짰을지 꼭꼮꼭 확인
# p만나면 본진: 상하좌우 2칸씩 밑 대각1칸씩이 가용범위
# 1.가용범위 전부 탐색? 
    # 1)상하좌우
    # 2)대각이동(4개)
# 2.->일단 자기 주위 1칸(동서남북4개, 대각4개) 탐색
    # 단, 대각 탐색은 동서남북탐색해서, x가 있는지 없는지로
    # * 아니지. 대각쪽도 엄밀히는 2칸 이동임. 걍 직진2칸할때 같이 2칸으로 묶어서 하는게 나음
        # 괜히 순서로 하면 조건이 복잡하기도 하고, 대각으로 직진은 안되니까
        # flood fill개념에 맞게
from collections import deque

def keep_distance(arr):
    interviewers = []
    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'P':
                interviewers.append([i,j])

    # interviewers좌표에서 맨해튼거리가 2인경우까지만 추가할 것
        # 문제: 대각의 경우 중복탐색되는 경우도 있을 수 있음(왼쪽위 지점: 왼쪽->위 & 위쪽->왼)
        # 다만, 대기실은 5*5이며, 대기실의 개수도 5개밖에 안되며, 정확성 테스트 제한도 10초나 되므로 넘어감
            # 걍 P의 시작점만 안 가도록!
            # *->아이고; 안 쓰면 안 끝남 무한 반복임;; 무조건 써줘야 함
    
    directions = [[0,-1], [0,1],[-1,0],[1,0]] # 좌,우,상,하
    q = deque()
    for interviewer in interviewers:
        visited = [[0]*5 for _ in range(5)]
        visited[interviewer[0]][interviewer[1]] = 1 # 초기상태 기입
        q.append(interviewer)
        while q:
            sx, sy = q.popleft()
            for dx, dy in directions:
                nowx, nowy = sx+dx, sy+dy
                if abs(nowx-interviewer[0])+abs(nowy-interviewer[1]) > 2:
                    continue # break하면 for문 아예 끝나서 x
                else:
                    # 진입 조건들
                    if (0<= nowx <= 4) and (0<= nowy <= 4) and (arr[nowx][nowy] != 'X') and not visited[nowx][nowy]:
                        if arr[nowx][nowy] == 'P':
                            return 0 # False로 끝
                        else: 
                            visited[nowx][nowy] = 1
                            q.append([nowx,nowy])
                            
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(keep_distance(place))
    return answer


# print(keep_distance(["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]))
# print(keep_distance(["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]))
# print(keep_distance(["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"]))
# print(keep_distance(["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"]))
# print(keep_distance(["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]))

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))


# 레퍼런스
    # 또 너무 복잡하게 생각했네..
    # 5*5고정이므로 그냥 아래처럼 해도 됨..
    # 이게 실전이었으면 나는 무조건 떨어졌음 & 선.택.과 집.중이 필요한데, 나는 이 부분을 전혀 못했음
    # 처음에 아이디어 방향을 잘못 잡기도 했던 듯 싶다 흠..
# def check(place):
#     for irow, row in enumerate(place):
#         for icol, cell in enumerate(row):
#             if cell != 'P':
#                 continue
#             if irow != 4 and place[irow + 1][icol] == 'P':
#                 return 0
#             if icol != 4 and place[irow][icol + 1] == 'P':
#                 return 0
#             if irow < 3 and place[irow + 2][icol] == 'P' and place[irow + 1][icol] != 'X':
#                 return 0
#             if icol < 3 and place[irow][icol + 2] == 'P' and place[irow][icol + 1] != 'X':
#                 return 0
#             if irow != 4 and icol != 4 and place[irow + 1][icol + 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol + 1] != 'X'):
#                 return 0
#             if irow != 4 and icol != 0 and place[irow + 1][icol - 1] == 'P' and (place[irow + 1][icol] != 'X' or place[irow][icol - 1] != 'X'):
#                 return 0
#     return 1

# def solution(places):
#     return [check(place) for place in places]