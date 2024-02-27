# '순열'
a, b = map(int,input().split())

from itertools import permutations

arr0 = list(range(1,a+1))

arr = list(permutations(arr0,b)) # 첫 인자로 list가 들어가야 함
# arr: [(1,), (2,), (3,)] -> tuple을 벗겨내야 함 how?
    # -> 그냥 반복문으로 인자 뽑아내면 됨

for ele in arr:
    for ele2 in ele:
        print(ele2, end=' ')
    print()