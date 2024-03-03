# 사과는 상자단위로만 판매하며, 상자를 꽉 채우지 못하면 버리기
# 이익이 발생하지 않는 경우 -> 0
# score를 정렬하고, 상자안에 안 들어가는 낮은 점수대 사과는 버리기

def solution(k, m, score):
    result = 0

    score.sort()
    score = score[len(score)%m:] # 상자안에 안 들어가는 저품질 사과는 버리기

    for k in range(0,len(score),m): # m=4 -> 0,4,8 ...
        result += score[k]*m

    return result

print(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))