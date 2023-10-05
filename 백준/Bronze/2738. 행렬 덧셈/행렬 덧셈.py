x, y = map(int, input().split())  # x행 y열
a, b = [], []  # 빈 배열 세팅

# 0. 입력
for i in range(x):  # 처음은 a꺼
    a.append(list(map(int, input().split())))
for i in range(x):  # 두번째는 b꺼
    b.append(list(map(int, input().split())))
# 1. 더해서 출력
for i in range(x):
    for j in range(y):
        print(a[i][j]+b[i][j], end=" ")
    print()  # 줄바꿈
