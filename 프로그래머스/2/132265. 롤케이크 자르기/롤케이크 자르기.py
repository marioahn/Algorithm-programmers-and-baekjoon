# 1트 - 당연히 시간초과로 실패(2개빼고 전부x)
# def solution(topping):
#     result = 0
#     for k in range(1,len(topping)-1):
#         if len(set(topping[:k])) == len(set(topping[k:])):
#             result += 1

#     return result


# 2트 - dict, stack, set이용
def solution(topping):
    result = 0

    dict_topping = {}
    for ele in topping:
        if ele not in dict_topping:
            dict_topping[ele] = 1
        else:
            dict_topping[ele] += 1
    
    brother = set()
    for k in range(len(topping)):
        brother.add(topping[k])
        dict_topping[topping[k]] -= 1
        if dict_topping[topping[k]] == 0: # value가 0이면, key 삭제
            del dict_topping[topping[k]]
        if len(brother) == len(dict_topping.keys()):
            result += 1

    return result


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))