# 드래그 -> 직사각형형태
# 드래그 거리: |rdx - lux| + |rdy - luy|의 최솟값 return
# 바탕화면에는 적어도 하나의 파일이 있다 -> 이 경우도 제대로 출력되는지 확인
# 행의 최초'#', 최후'#' / 열의 최초'#', 최후'#'를 찾으면 될듯 하다
def solution(wallpaper):
    # l = low, h = high
    xl,yl,xh,yh = 0,0,0,0

    x_list, y_list = [], []
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            x_list.append(i)
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                y_list.append(j)
    
    xl, xh = x_list[0], x_list[-1]+1 # min, max할 필요도 없을듯
    yl, yh = min(y_list), max(y_list)+1

    return [xl,yl,xh,yh]

print(solution([".#...", "..#..", "...#."]))

# 레퍼런스 코드 - 큰 차이는 없지만, 훨신 간결 - 내 코드는 한눈에 안 들어옴
# def solution(wall):
#     a, b = [], []
#     for i in range(len(wall)):
#         for j in range(len(wall[i])):
#             if wall[i][j] == "#":
#                 a.append(i)
#                 b.append(j)
#     return [min(a), min(b), max(a) + 1, max(b) + 1]

