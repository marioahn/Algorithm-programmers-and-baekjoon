# def solution(x):
#     sum = 0
#     for ele in str(x):
#         sum += int(ele)
    
#     return False if (x % sum) else True


def solution(n):
    return n%sum(int(x) for x in str(n)) == 0