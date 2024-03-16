def solution(d, budget):
    d.sort()
    
    cnt = 0
    for ele in d:
        if (budget-ele) >=0:
            budget -= ele
            cnt += 1
        else:
            break
    return cnt


print(solution([1,3,2,5,4], 9))