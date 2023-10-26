N = int(input())
A, B = map(int, input().split())

sum = A//2 + B

if sum >= N:
    print(N)
else:
    print(sum)
