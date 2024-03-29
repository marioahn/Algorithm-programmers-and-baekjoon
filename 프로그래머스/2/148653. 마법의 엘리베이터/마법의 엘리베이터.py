# 제한사항: 1 ≤ storey ≤ 100,000,000
#  -1, +1, -10, +10, -100, +100 등과 같이,
    # 절댓값이 10c (c ≥ 0 인 정수) 형태인 정수들이 적힌 버튼
# 16 -> 10보단, 20으로 올라가서 0내려가는게 나음
# 아 근데 맨 첫 자리는 살짝 다를 수도? -> 첫 자리 뿐만 아니라,
    # "5"인 경우 그 다음 자리수에 따라 올릴지 내릴지 정해야 한다
    # "45" vs "55" -> 전자는 내.려야 하지만,
        # 55는 올리든, 내리든 상관없지만
        # 65는 무조건 올려야하고
        # 45,35..는 무조건 내려야 함

# 흠;; 근데 변수를 너무 많이 쓰는데 -> 최적화 해보기
def solution(storey):
    original = storey
    storey = [int(x) for x in str(storey)]
    storey.reverse()
    storey.append(0)
    
    # 1의 자리부터 시작할 것
    cnt = 0
    i = 0
    while i < len(storey)-1:
        if storey[i] >= 6:
            original += (10-storey[i])
            cnt += (10-storey[i])
            storey[i+1] += 1 # 이때만 갱신
        elif storey[i] <= 4:
            original -= storey[i]
            cnt += storey[i]
        else: # 5면
            cnt += 5
            if storey[i+1]>=5:
                original += 5
                storey[i+1] += 1 # 이때만 갱신
            else:
                original -= 5

        original //= 10
        i += 1

    # 마지막 경우 처리: 만약 700인경우 1000되고 0되는게 이득
    return cnt+storey[-1]

print(solution(16))
print(solution(2554))
print(solution(367)) # 10
print(solution(667)) # 10이 나와야 함: 670 -> 700 -> 1000 -> 0