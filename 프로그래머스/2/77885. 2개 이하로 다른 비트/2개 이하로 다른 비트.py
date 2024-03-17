# 비트끼리의 비교를 어떻게 하면 효율적으로 할 수 있을까
    # 이중 포문은 에바인거 같은데
    # 이 부분은 규칙찾아야 할듯
# 흠;; 1011 vs 10101 이런 경우도 포함시켜야 하나? 01011이랑 같으니까. 2개차이남
    # -> yes


# 1트 - 실패(규칙 잘못 찾음)
# def find_bit(n):
    
#     # step1: 비트로 변환해서 쭉 돌림 -> ㄴㄴ 그냥 규칙찾음
#     # n_bit = format(n,'b') # 'o'는 8, 'x'는 16진수
#     if n % 8 == 7: return n+4*((n//8)+1)
#     if n % 8 == 3: return n+2
#     return n+1

# def solution(numbers):
#     result = []
#     for number in numbers:
#         result.append(find_bit(number))
#     return result

# print(solution([13,14,15]))
# print(solution([343])) # [347]이 나와야하는데 엉뚱한 수가 나옴 -> 규칙아예 잘못찾음;;

# 2트
# 블로그 참고;
    # 1) 짝수의 경우
    # 만약, 4라면 이진수로 100이다. 4보다 크면서 2개 이하로 다른 수를 찾으면 101
    # -> 즉, 가장 뒤에 있는 0을 1로 바꾸면 됨 -> +1

    # 2) 홀수의 경우
    # 만약, 7이라면 이진수로 0111 (바꿀때 편의를 위해 앞에 0을 붙인다)
    # 먼저 짝수의 경우처럼 가장 뒤에 있는 0의 인덱스(idx)를 찾아 1로 바꾼다 -> 1111,
    # 그런 다음 idx+1 의 인덱스 값을 0으로 바꾼다 -> 1011이 되고, 이게 바로 답.
def find_bit(num):
    if num % 2 == 0:
        return num+1
    else:
        to_bit = list('0'+format(num,'b'))
        idx = ''.join(to_bit).rfind('0') # rfind 매우 유용!!
        to_bit[idx] = '1'
        to_bit[idx+1] = '0' # 01부분을 10부분으로 바꿔주기ㅇㅇ
        return int(''.join(to_bit),2)

def solution(numbers):
    result = []
    for number in numbers:
        result.append(find_bit(number))

    return result

print(solution([13,14,15])) # 14,15,23
print(solution([343])) # [347]이 나와야하는데 엉뚱한 수가 나옴 -> 규칙아예 잘못찾음;;