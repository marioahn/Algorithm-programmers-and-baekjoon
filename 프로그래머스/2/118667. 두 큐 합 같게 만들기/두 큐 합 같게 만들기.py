# 제한조건:
    # 1 ≤ queue1의 길이 = queue2의 길이 ≤ 300,000
    # 1 ≤ queue1의 원소, queue2의 원소 ≤ 109

# 처음엔 감을 잘 못잡았지만, queue라는 특성을 자세히 살피면 답이 보인다
# queue: stack과 달리, 선입선출 -> 두개의 큐를 합치고,
# 투포인터로 풀게 되면? -> left,right idx 조정하다 합이 (sum(queue1+queue2)//2)가 되면 끝
    # 투포인터 idx(left, right)까지 구하는 것은 성공했지만..
    # *그걸로 try횟수는 how? -> 너무 번잡
# 마지막으로 result에 아무것도 안 담기면 -1

# 0. 다른 사람 투포인터 풀이: 문제 통과는 되는데 아래 케이스를 통과못함
    # -> [1, 1, 1, 1, 11, 1],[1, 1, 1, 1, 1, 1] - xx -> deque로 풀자
# def solution(queue1, queue2):
#     q = queue1 + queue2
#     target = sum(q) // 2

#     i, j = 0, len(queue1)-1
#     curr = sum(queue1)
#     count = 0

#     while i < len(q) and j < len(q):        
#         if curr == target:
#             return count

#         elif curr < target and j < len(q)-1:
#             j += 1
#             curr += q[j]

#         else:
#             curr -= q[i]
#             i += 1

#         count += 1

#     return -1

# 1트: 파이썬은 deque로 풀면 시간초과 해결이 가능
    # 풀이법도 ez
from collections import deque

def solution(queue1, queue2):
    cnt, sum1, sum2 = 0, sum(queue1), sum(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)

    for _ in range(len(queue1)*3): # 2?
        if sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        elif sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        else:
            return cnt
    
        cnt += 1    

    return -1

print(solution([3, 2, 7, 2],[4, 6, 5, 1])) # 2
print(solution([1, 2, 1, 2],[1, 10, 1, 2])) # 7
print(solution([1, 1],[1, 5])) # -1
print(solution([1, 1, 1, 1, 11, 1],[1, 1, 1, 1, 1, 1])) # 15.!(되긴 되는 거임)
	