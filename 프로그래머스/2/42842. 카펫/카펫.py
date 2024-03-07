# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 길다
# 노란색 격자의 가로, 세로를 a, b라고 하면
    # a*b = yellow - (1)
    # (a+2)*(b+2) = brown+yellow
    # -> 2(a+b)+4 = brown - (2)
    # yellow의 약수쌍을 구하고, 이 중에서 (1), (2)를 만족하는 (a+2), (b+2)를 return

def solution(brown, yellow):
    divisor_pair =[]
    # 약수 구하기
    for k in range(1,int((yellow)**(1/2))+1):
        if (yellow) % k == 0:
            divisor_pair.append([k,(yellow)//k])

    for divisor in divisor_pair:
        if (divisor[0]+divisor[1]) == (brown-4)//2:
            return [max(divisor)+2, min(divisor)+2]

print(solution(24,24))
print(solution(4004,999999)) # 1003, 1001