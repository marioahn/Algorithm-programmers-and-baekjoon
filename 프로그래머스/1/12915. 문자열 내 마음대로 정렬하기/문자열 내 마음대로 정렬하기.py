# 1트: 근데, x[n]이 같은 경우는 못했음 - sorted에서, 람다안에 if문 어떻게 쓸까?
    # result = sorted(strings, key=lambda x: x[n])
    # 엥; (x[n],x) 하니까 되네 -> 무슨 뜻인가?
    # 아. 그러니까, x[n]기준으로 정렬하고 / 두번째 요소로 x자체를 비교해서 한다는 것
        # 두번째 요소는 그니까 말 그대로, 단어자체 사전순 비교 뜻임ㅇㅇ.
        # 애초에 strings를 한번 sort하고 위 실패코드 썼으면 되는거기도 함

def solution(strings, n):
    result = sorted(strings, key=lambda x: (x[n],x))
    return result


print(solution(["sun", "bed", "car"],1))
print(solution(["abce", "abcd", "cdx"],2))
