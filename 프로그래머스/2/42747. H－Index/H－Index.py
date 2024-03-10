# 논문 n편 중, h번 이상 인용된 논문이 h편 이상일 때의 h값과,
    # 그 때, h번 이상 인용된 논문의 개수 중 최대값을 리턴
# 해당하는 값을 못 찾으면 논문 전체 개수를 리턴
def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] <= i+1:
            return max(citations[i],i)

    return len(citations)


print(solution([3, 0, 6, 1, 5]))
print(solution([6,5,4,1,1,1,0]))
print(solution([6,5,4,4,1,1,1,0]))
print(solution([1, 4, 5])) # 2가 나와야 함