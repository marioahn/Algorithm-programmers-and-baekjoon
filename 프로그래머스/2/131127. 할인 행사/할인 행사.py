# 기본만 일단 해볼까..
def solution(want, number, discount):
    day_cnt = 0
    dict = {key: value for key, value in zip(want, number)}

    for k in range(len(discount)-9):
        tmp = discount[k:k+10]
        flag = True
        for ele in want:
            if dict[ele] != tmp.count(ele):
                flag = False
                break
        
        if flag: day_cnt += 1

    return day_cnt

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))