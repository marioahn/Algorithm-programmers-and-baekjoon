# 흠.. 그냥 numbers에서 2개뽑는 '조합' 구하고, 그 각각의 합 얻고,
    # 이걸 set으로 바꿔서 중복제거하고, 다시 list화
from itertools import combinations


def solution(numbers):
    combis = list(combinations(numbers,2))
    result = []
    for combi in combis:
        if sum(combi) not in result:
            result.append(sum(combi))
    
    return sorted(result)