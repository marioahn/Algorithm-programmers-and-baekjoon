N = int(input())
minNumber = 1001
for _ in range(N):
    a, b = map(int, input().split())
    if a <= b:
        minNumber = min(minNumber, b)

if minNumber == 1001:
    print(-1)
else:
    print(minNumber)
