# 길이가 1인 연속수열? -> 뒤에 추가x
# 길이가 2? -> 뒤에 elements[0:1] 추가
# 길이가 3? -> 뒤에 elements[0:2] 추가

# 1트 - 아 근데, 너무 오래걸린다..
    # TC20: 통과 (4221.19ms, 72.7MB)
# def solution(elements):
#     # result = elements # 앗;; 이러면 얕은 복사라서 원본/복사본 둘다 바뀜
#     result = elements[:]

    
#     # k = 길아가 k인 연속수열의 경우, 2부터 시작
#     for k in range(2,len(elements)+1):
#         tmp = elements + elements[0:k-1]
#         for i in range(len(elements)):
#             result.append(sum(tmp[i:i+k]))

#     return len(set(result))

# 2트 - 1트 개선
    # (1)처음부터 set으로 / len(elements) -> 변수에 담아서 넣어주기
        # -> 메모리는 엄청 줄음 - TC20: 통과 (4589.91ms, 43.7MB)
    # (2)그럼에도 시간복잡도가 O(N**3)이기 때문에, 더 줄일 수가 없음
        # 2중포문안에 sum함수.
        # -> 따라서 근본적으로 풀이 구조를 바꿔야 함. 이 방식대론 답x

# def solution(elements):
#     # result = elements # 앗;; 이러면 얕은 복사라서 원본/복사본 둘다 바뀜
#     result = set(elements[:])
#     length = len(elements)

    
#     # k = 길아가 k인 연속수열의 경우, 2부터 시작
#     for k in range(2,length+1):
#         tmp = elements + elements[0:k-1]
#         for i in range(length):
#             result.add(sum(tmp[i:i+k]))

#     return len(result)

# print(solution([7,9,1,1,4]))


# 3트 - 레퍼런스
    # 시간복잡도: O(N**2)
    # 댓글: 길이 별로 잘라서 모으는게 아니라, 하나 주인공 잡고 거기서부터 모든 길이를 다 자르는 것
def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)