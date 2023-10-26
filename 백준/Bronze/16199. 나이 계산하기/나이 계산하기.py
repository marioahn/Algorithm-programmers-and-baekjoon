y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

# step1: 만 나이
if m2 > m1 or (m2 == m1 and d2 >= d1):
    print(y2-y1)  # 생일 지남
else:  # 생일 안 지남
    print(y2-y1-1)

# step2: 세는 나이
print(y2-y1+1)
# step3: 연 나이
print(y2-y1)
