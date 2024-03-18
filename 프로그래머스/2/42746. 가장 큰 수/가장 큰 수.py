# 다중조건 정렬
# 제한조건
    # numbers의 길이는 1 이상 100,000 이하입니다.
    # * numbers의 원소는 0 이상 1,000 이하입니다.
        # 한자리, 두자리, 세자리수끼리 비교해서 정렬시켜야 함
    # 3, 39, 394, 392 이 비교가 성공해야 함 -> 394,39,392 
        # 여기서 3은 어디로 -> 각 요소 *3해서 비교해서 앞 3자리 큰걸로 가져오면 됨
    # x*3[0:3]을 정렬조건으로 해야하지 않나? 그리고, 각 number을 slicing하는것도 엄청난 소모아닌가
        # 왜 x*3으로 되는지 -> 직접 해보면 비교가 가능

# 1트
# def solution(numbers):
#     result = ''
#     numbers = list(map(str,numbers)) # 문자열로 바꿔야 문제에서 원하는 식의 정렬이 됨

#     numbers.sort(key=lambda x: x*3, reverse=True) # 왜 이렇게만 해도 되는가?

#     if numbers[0] == '0': return '0'
#     return ''.join(numbers) 

# --
# 2트
# 2트 - 1트보다 이게 훨씬 나은 듯
    # 비교기법: comparator: a,b두 수를 가져다두고 비교해서 하나씩 swap하면서 모든 비교가 이루어지는 방식
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  

def solution(numbers):
    n = [str(x) for x in numbers]
    # functools.cmp_to_key()의 인자로는 콜.백.함수 자체가 들어가야 함ㅇㅇ.
    # sorted에서 정렬기준인 key내용 안에 위에서 만든 comparator를 넣으면 됨
    # 진짜 거의 커스텀만든 느낌이네 ㅎㄷㄷ;;
    n = sorted(n, key=functools.cmp_to_key(comparator), reverse=True)
    
    answer = str(int(''.join(n)))
    return answer



print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0,0,0])) # 000이 아니라 0이 나와야 함