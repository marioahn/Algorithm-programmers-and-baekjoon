# 아래 조건에 하나라도 걸리면, 가다가 마는게 아니라 아예 그 명령 수행 x
# 즉, 해당 명령의 '경로'가 이상하지 않는지 확인해야 함
    # 주어진 방향으로 이동할 때 공원을 벗어나는지 확인
    # 주어진 방향으로 이동 중 장애물을 만나는지 확인

# 1. s의 좌표 찾기

def solution(park, routes):
    way_dict = {'N': [-1,0], 'S': [1,0], 'W': [0,-1], 'E': [0,1]}

    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                sx, sy = i, j

    for route in routes:
        tx, ty = sx, sy # 임시
        flag = True
        for k in range(int(route[-1])):
            tx += way_dict[route[0]][0]
            ty += way_dict[route[0]][1]
            if (tx<0 or tx>=len(park)):
                flag= False
                break
            if (ty<0 or ty>= len(park[0])):
                flag= False
                break
            if park[tx][ty] == 'X':
                flag= False
                break

        if flag:
            sx, sy = tx, ty # 그제서야 이동시킴

    return [sx,sy]

# print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
# print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))