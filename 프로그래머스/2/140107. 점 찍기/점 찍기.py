# 제한조건 -> 이중포문 x / 피타고라스 이용
    # 1 ≤ k ≤ 1,000,000
    # 1 ≤ d ≤ 1,000,000
def solution(k, d):
    cnt = 0
    for x in range(0,d+1,k):
        y = ((d**2)-(x**2))**(0.5)
        cnt += int(y)//k + 1 # 0부터 시작이니 +1

    return cnt

print(solution(1,5))