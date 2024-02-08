from itertools import combinations_with_replacement

n = int(input())

# 중복조합
res = 0
for i in combinations_with_replacement(range(n+1), 2):
    res += sum(i)
print(res)