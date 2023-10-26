import sys

input = sys.stdin.readline

sum = 0
while 1:
    a = int(input())
    if a == -1:
        print(sum)
        break
    else:
        sum += a
