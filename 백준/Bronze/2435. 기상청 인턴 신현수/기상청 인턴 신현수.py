n, k = map(int, input().split()) # 날짜의 수, 연속적인 날짜
temp_li = list(map(int, input().split())) # 측정한 온도 리스트
total_temp = [] # 온도의 합 리스트
for i in range(n - k + 1):
  total = 0
  for j in range(i, i + k):
    total += temp_li[j]
  total_temp.append(total)
print(max(total_temp))