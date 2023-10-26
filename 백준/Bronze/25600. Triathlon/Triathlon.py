N = int(input())

maxNumber = 0
for _ in range(N):
    a, d, g = map(int, input().split())
    if a == d + g:
        tmp = a * (d + g) * 2
    else:
        tmp = a * (d + g)
    maxNumber = max(maxNumber, tmp)

print(maxNumber)
