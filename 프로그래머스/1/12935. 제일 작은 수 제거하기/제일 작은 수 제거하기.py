def solution(arr):
    if len(arr) == 1: return [-1] 
    min_number = min(arr)
    arr.remove(min_number)
    return arr