from itertools import combinations

def solution(number):
    cnt = 0
    for tmp_list in combinations(number, 3):
        if sum(tmp_list) == 0:
            cnt += 1
            
    return cnt