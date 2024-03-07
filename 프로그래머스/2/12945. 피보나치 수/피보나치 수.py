def solution(n):
    pibo = [0,1]
    for k in range(1,n):
        pibo.append(pibo[k-1]+pibo[k])

    return pibo[-1] % 1234567

print(solution(5))

# 레퍼런스
    # 피보나치 아래처럼 swap이용해서 할 수도 있네 ㅎㄷㄷ / 공간차지 안해서 좋은듯
# def fibonacci(num):
#     a, b = 0, 1
#     for i in range(num):
#         a, b = b, a+b
#     return a
