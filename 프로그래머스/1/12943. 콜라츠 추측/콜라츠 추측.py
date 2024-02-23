def solution(num):
    if num == 1: return 0
    cnt = 0
    while 1:
        num = num//2 if (num%2 == 0) else num*3+1
        cnt += 1
        if num == 1: return cnt
        if cnt == 500: return -1
    


print(solution(6))