def solution(arr, divisor):
    arr.sort()
    result = []
    for ele in arr:
        if ele % divisor == 0:
            result.append(ele)
    
    return result if len(result) != 0 else [-1]


print(solution([5, 9, 7, 10],5))