# 시간제한
    # n은 1 이상 1,000 이하 -> n이 1000이면 요소의 개수는 500,500 -> 조심
    # 그래서 조합 뽑아서 max값 뽑는건 x / dfs도 마찬가지
# 그림의 모양은 정삼각형(피라미드)모양이지만, 각 층을 왼쪽으로 밀어서 직각삼각형 만든다고 치자
# 그러면, 각층의 맨 왼쪽부터 오른쪽은 행렬의 좌표로 치환할 수 있다
    # 1층 꼭대기는 [0,0]이고, 2층의 맨 왼쪽은 [1,0]인 셈

# def solution(n):
#     result = [[0 for _ in range(x)] for x in range(1,n+1)]

#     # rotation횟수는 = n (n이 4면 4번돈다 - 순서: 아래->오른쪽->왼쪽위)
#     x,y, value = -1,0, 0 # 좌표, 좌표에 들어갈 값
#     for i in range(n):
#         if i % 3 == 0:
#             for j in range(n-i):
#                 x, value = x+1, value+1
#                 result[x][y] = value
#         elif i % 3 == 1:
#             for j in range(n-i):
#                 y, value = y+1, value+1
#                 result[x][y] = value
#         else:
#             for j in range(n-i):
#                 x,y, value = x-1,y-1, value+1
#                 result[x][y] = value
    
#     return sum(result,[]) # 2차원 -> 1차원풀기
def solution(n):
    dx=[0,1,-1];dy=[1,0,-1]
    b=[[0]*i for i in range(1,n+1)]
    x,y=0,0;num=1;d=0
    while num<=(n+1)*n//2:
        b[y][x]=num
        ny=y+dy[d];nx=x+dx[d];num+=1
        if 0<=ny<n and 0<=nx<=ny and b[ny][nx]==0:y,x=ny,nx
        else:d=(d+1)%3;y+=dy[d];x+=dx[d]
    return sum(b,[])
print(solution(5))