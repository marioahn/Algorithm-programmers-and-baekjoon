# 1. 약수개수
    # https://velog.io/@dmsgur7112/Python-%EC%95%BD%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0
# 2. limit넘기는 것은 -> limit-2로 변환(아니면 2고정?)

def divisor(n): # 16 -> [1,2,4,8,16]
    cnt = 0
    for i in range(1,int(n**(1/2))+1):
        if n % i == 0:
            cnt += 1
            if i < (n//i): # 1,16 / 2,8은 쌍인데, 4는 한개이므로 이 조건 필요
                cnt += 1

    return cnt

def solution(number, limit, power):
    sum = 0
    for k in range(1,number+1):
        if divisor(k) <= limit:
            sum += divisor(k)
        else:
            sum += power

    return sum
    # 한 줄 코딩 - 근데, cf(i)를 2번 호출하게 되므로, 더 비효율적이긴 함
    # return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])



print(solution(5,3,2))
print(solution(10,3,2))