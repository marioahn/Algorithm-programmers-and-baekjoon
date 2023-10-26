# 서로 나누었을 때 나머지가 같게 하려면
# 세 수가 모두 같아야 함

N = int(input())
for _ in range(N):
    a, b, c = map(int, input().split())
    print(min(a, b, c))
