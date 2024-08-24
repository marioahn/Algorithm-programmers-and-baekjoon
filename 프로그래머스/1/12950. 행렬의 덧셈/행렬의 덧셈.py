# 이렇게하면 여러 행렬을 동시에 더하는 코드로 수정하기도 쉬울 듯
# '*'튜플 언팩킹을 활용하여, x라는 변수를 한개만 이용해서 두개의 튜플을 받아들여 처리
def solution(arr1,arr2):
    return [list(map(sum, zip(*x))) for x in zip(arr1, arr2)]

# print(solution([[1,2], [2,3]], [[3,4],[5,6]]))
# [[4, 6], [7, 9]]