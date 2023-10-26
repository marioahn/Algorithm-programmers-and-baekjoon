N, W, H, L = map(int, input().split())

result = (W//L)*(H//L)
if N >= result:
    print(result)
else:
    print(N)
