import sys
input = sys.stdin.readline

# 유클리드 호제법
def gcd(x, y):
    while y:
        if x > y:
            x, y = y, x
        y %= x
    return x

# 입력 및 출력
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    gcd_num = gcd(a, b)
    print(a * b // gcd_num, gcd_num)