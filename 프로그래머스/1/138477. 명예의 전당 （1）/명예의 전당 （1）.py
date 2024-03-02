def solution(k, score):
    # rank는 k길이만을 가질 수 있음
    rank, result = [], []

    for i in range(len(score)):
        rank.append(score[i])
        rank.sort()
        if i < k:
            result.append(rank[0])
        else:
            result.append(rank[-k])
            
    return result

# print(solution(3,[10, 100, 20, 150, 1, 100, 200]))
print(solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
