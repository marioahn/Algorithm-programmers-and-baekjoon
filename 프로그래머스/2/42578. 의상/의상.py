# 모자가 2종류, 코트가 1종류라면?
    # (x1,a,b) / (x2,c) <- 이렇게 x1,x2를 한개씩 넣어줘야 한다
    # x의 의미: blank. 한 종류의 의상만 쓸 수도 있으므로
    # x1x2,x1c, ax2,ac, bx2,bc -> 여기서 x1x2는 빼야 함
    # 따라서 return (k1+1)*(k2+1)-1! 
# clothes를 한방에 dict로 바꾸는 메서드 없을까
# from functools import reduce
from math import prod


def solution(clothes):
    dict = {}

    for clothe in clothes:
        if clothe[1] not in dict:
            dict[clothe[1]] = 1
        else:
            dict[clothe[1]] += 1
    
    value_list = list(dict.values())
    value_list = [x+1 for x in value_list]
    return prod(value_list)-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))