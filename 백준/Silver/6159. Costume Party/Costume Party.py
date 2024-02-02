n, s = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
cnt = 0
st, e = 0, n-1
while st < e:
    if arr[st] + arr[e] <= s:
        cnt = cnt + e -st
    else:
        e -= 1
        st -= 1
    st += 1
print(cnt)