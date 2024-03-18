# 다중조건 정렬
# 제한조건
    # numbers의 길이는 1 이상 100,000 이하입니다.
    # * numbers의 원소는 0 이상 1,000 이하입니다.
        # 한자리, 두자리, 세자리수끼리 비교해서 정렬시켜야 함
    # 3, 39, 394, 392 이 비교가 성공해야 함 -> 394,39,392 
        # ? 여기서 3은 어디로 -> 각 요소 *3해서 비교해서 앞 3자리 큰걸로 가져오면 됨
    # x*3[0:3]을 정렬조건으로 해야하지 않나? 그리고, 각 number을 slicing하는것도 엄청난 소모아닌가
        # ? 왜 x*3으로 되는지 -> 직접 해보면 비교가 가능


def solution(numbers):
    result = ''
    numbers = list(map(str,numbers)) # 문자열로 바꿔야 문제에서 원하는 식의 정렬이 됨

    numbers.sort(key=lambda x: x*3, reverse=True) # 왜 이렇게만 해도 되는가?

    if numbers[0] == '0': return '0'
    return ''.join(numbers) 


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0,0,0])) # 000이 아니라 0이 나와야 함