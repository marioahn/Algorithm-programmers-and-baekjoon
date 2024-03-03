# def solution(n, m, section):
#     cnt = 0

#     cleaning = [0 for _ in range(m)]
#     bucket = [0 for _ in range(n)]
#     # bucket에서 훼손구역 1로 표시하기
#     for ele in section:
#         bucket[ele-1] = 1

# 		# cleaning
#     for i in range(n):
#         if bucket[i] == 1:
#             bucket[i:i+m] = cleaning
#             cnt += 1
    
#     return cnt

# print(solution(8,4,[2, 3, 6]))

# 레퍼런스
def solution(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer