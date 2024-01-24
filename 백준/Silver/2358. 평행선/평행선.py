import sys
n = int(sys.stdin.readline())
c = {}
y = {}
check_x = []
check_y = []
for _ in range(n):
    a,b = map(int , sys.stdin.readline().split(" "))
    check_x.append(a)
    check_y.append(b)
    if a in c:
        c[a].append(b)
    else:
        c[a] = []

    if b in y:
        y[b].append(a)
    else:
        y[b] = []
check_y = list(set(check_y))
check_x = list(set(check_x))

ans = 0
for i in check_x:
    if c[i]:
        ans += 1
for i in check_y:
    if y[i]:
        ans += 1
print(ans)