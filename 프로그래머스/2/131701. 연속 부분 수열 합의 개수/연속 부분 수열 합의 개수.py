# 길이가 1인 연속수열? -> 뒤에 추가x
# 길이가 2? -> 뒤에 elements[0:1] 추가
# 길이가 3? -> 뒤에 elements[0:2] 추가

def solution(elements):
    # result = elements # 앗;; 이러면 얕은 복사라서 원본/복사본 둘다 바뀜
    result = elements[:]

    
    # k = 길아가 k인 연속수열의 경우, 2부터 시작
    for k in range(2,len(elements)+1):
        tmp = elements + elements[0:k-1]
        for i in range(len(elements)):
            result.append(sum(tmp[i:i+k]))

    return len(set(result))

print(solution([7,9,1,1,4]))