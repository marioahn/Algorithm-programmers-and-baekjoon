# 파이썬으로만 할 수 있는 깔끔한 방법이 있을것 같은데 흠
# O(N**2)로 밖에 안되나 - 
def solution(s):
    stack = [] # idx찾을 용도(임시)
    result = []

    for ele in s:
        if ele not in stack:
            result.append(-1)
            stack.append(ele)
        else:
            result.append(stack[::-1].index(ele)+1)
            stack.append(ele)

    return result


print(solution("banana")) # [-1, -1, -1, 2, 2, 2]
print(solution("foobar")) # [-1, -1, 1, -1, -1, -1]