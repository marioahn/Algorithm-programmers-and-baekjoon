# 1트: 근데, x[n]이 같은 경우는 못했음 - sorted에서, 람다안에 if문 어떻게 쓸까?
    # result = sorted(strings, key=lambda x: x[n])

def solution(strings, n):
    result = sorted(strings, key=lambda x: (x[n],x))
    return result


print(solution(["sun", "bed", "car"],1))
print(solution(["abce", "abcd", "cdx"],2))
