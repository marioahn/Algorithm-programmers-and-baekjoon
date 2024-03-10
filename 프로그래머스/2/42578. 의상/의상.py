# 모자가 2종류, 코트가 1종류라면?
    # (x1,a,b) / (x2,c) <- 이렇게 x1,x2를 한개씩 넣어줘야 한다
    # x의 의미: blank. 한 종류의 의상만 쓸 수도 있으므로
    # x1x2,x1c, ax2,ac, bx2,bc -> 여기서 x1x2는 빼야 함
    # 따라서 return (k1+1)*(k2+1)-1! 
# clothes를 한방에 dict로 바꾸는 메서드 없을까
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

# 레퍼런스1 - 아. 너무 복잡하게 생각했다;;
    # 1)중간에 +1해서 빈종류 생각하기전에, 걍 애초에 시작부터 수를 2로 두면 됨
    # 2)곱하기 걍 반복문써도 되는데 끙;;
# def solution(clothes):
#     clothes_type = {}

#     for c, t in clothes:
#         if t not in clothes_type:
#             clothes_type[t] = 2
#         else:
#             clothes_type[t] += 1

#     cnt = 1
#     for num in clothes_type.values():
#         cnt *= num
#     return cnt - 1

# 레퍼런스2
# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    
#     return cnt