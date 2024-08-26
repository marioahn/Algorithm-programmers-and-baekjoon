# 걍 3중포문밖에 생각이 안 나는데
def solution(number):
    cnt = 0
    for i in range(len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if (number[i]+number[j]+number[k]) == 0:
                    cnt +=1 

    return cnt


print(solution([-2, 3, 0, 2, -5])) # 2
print(solution([-3, -2, -1, 0, 1, 2, 3])) # 5
