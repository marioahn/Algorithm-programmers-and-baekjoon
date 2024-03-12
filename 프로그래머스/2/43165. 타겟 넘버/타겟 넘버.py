# dfs로. bfs도 되는건가??
# 생각해보니까, 트리형식으로 2개로 나눠서 내려가는거니까 bfs같기도?(1,-1)
answer = 0


def dfs(arr, level, sum, target):
    global answer
    if level == len(arr):
        if sum == target:
            answer += 1
        return

    for ele in [1, -1]:
        dfs(arr, level + 1, sum + (arr[level]) * ele, target)


def solution(numbers, target):
    global answer
    dfs(numbers, 0, 0, target)
    return answer


# print(solution([1, 1, 1, 1, 1], 3))
# print(solution([4, 1, 2, 1], 4))
