from collections import Counter


def solution(weights):
    result = 0
    counter = Counter(weights) # 개편하네..
    # 1. 같은 것들의 1:1비교 후 중복제거
    for key, value in counter.items():
        if value >=2:
            result += (value)*(value-1)//2
    weights = set(weights)

    # 2. 2:3 2:4 3:4로 짝꿍 찾기
    for w in weights: # *변수 weight보단 w가 간편하네 이 경우는
        if w*(2/3) in weights: # 150 == 150.0 -> True
            result += counter[w]*counter[w*(2/3)]
        if w*(2/4) in weights: 
            result += counter[w]*counter[w*(2/4)]
        if w*(3/4) in weights: 
            result += counter[w]*counter[w*(3/4)]

    return result