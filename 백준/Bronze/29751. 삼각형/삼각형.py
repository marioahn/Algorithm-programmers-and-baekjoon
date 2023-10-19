# 소수점 한자리까지 how 표현? -> round!
W, H = map(int, input().split())

print(round(W*H/2, 1))
