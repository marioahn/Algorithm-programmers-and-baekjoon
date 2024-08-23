# def solution(a, b):
#     # return sum([i*j for i in a for j in b]) # 이중포문이기 때문에 x
#     # return sum([lambda key=i,j: for i in a for j in b]) # 문법오류
#     sum = 0
#     for k in range(len(a)):
#         sum += a[k]*b[k]
#     return sum

# def solution(a,b):
#     return sum([x*y for x,y in zip(a,b)])

# solution = lambda x,y: sum(x*y for x,y in zip(a,b)) -> 에러

solution = lambda a, b: sum(x*y for x, y in zip(a,b))