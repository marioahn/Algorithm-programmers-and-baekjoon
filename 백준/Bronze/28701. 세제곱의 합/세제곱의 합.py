n = int(input())
answer1 = 0
answer3 = 0

for i in range(1, n+1):
    answer1 += i
    answer3 += i**3

print(answer1)
print(answer1**2)
print(answer3)
