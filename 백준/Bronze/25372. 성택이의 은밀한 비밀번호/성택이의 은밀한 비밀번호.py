# N = int(input())
# for _ in range(N):
#     a = input()
#     if len(a) >= 6 and len(a) <= 9:
#         print('yes')
#     else:
#         print('no')
# 위 코드 리팩토링하기

N = int(input())
for _ in range(N):
    if 9 >= len(input()) >= 6:
        print('yes')
    else:
        print('no')
