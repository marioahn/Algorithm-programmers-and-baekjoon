def solution(cards1, cards2, goal):

    # 아래처럼 0 안 넣어주면, 아래 사례에서 cards2가 길이가 0이되고,
        # elif문에서 cards2[0] -> list index out of range에러가 발생
    cards1.append(0)
    cards2.append(0)
    
    for k in range(len(goal)):
        if goal[k] == cards1[0]:
            cards1.pop(0)
        elif goal[k] == cards2[0]:
            cards2.pop(0)
        else:
            return 'No'
    
    return 'Yes'


print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))