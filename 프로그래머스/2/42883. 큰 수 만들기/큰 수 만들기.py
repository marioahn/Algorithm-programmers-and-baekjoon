# 단순히 문자니까 1자리수끼리 정렬하고, [0:len-4]하면 안되나?
# ㄴㄴ. 순서를지켜야 함 -> sort하는게 x
# 1트 - x
# def solution(number, k):
#     result = ''

#     number = list(number)
#     number.sort(reverse=True)

#     return ''.join(number[:len(number)-k])

# 2트 - 시간초과로 실패(4/12)
    # *제한: number는 2자리 이상, 1,000,000자리 이하인 숫자
    # "순서"를 지키며, 뽑는 '순열'ㅇㅇ. 이 리스트 중에서 제일 큰거 고르면 될듯?
    # ㄴㄴ -> 순열이 아니라 조합임. '1924' -> '19'는 ok. 근데, '91'이 나오면 안됨
    # 아닌데. 길이가 최대 1,000,000인데 언제 이 모든걸 조합뽑고 있음..
# from itertools import permutations, combinations

# def solution(number, k):
#     number = list(number)

#     n_P_r = list(map(list,list(combinations(number,len(number)-k))))
#     n_P_r2 = list(map(''.join,n_P_r))
    
    
#     return str(max(n_P_r2))



# 3트: dfs로 풀어야하나 - visited로 중복 방지하는 식으로
    # 근데, dfs나 2트의 조합풀이나 깊이가 크게 다를바 없음
    # 제한조건 설정해도 딱히 경우의 수를 줄이는 방법이 생각나지 않음
    # max값을 뽑아내야 하기에, 일단 끝까지 모든 깊이를 들어가야 함
    # -> 폐기


# 4트:
    # dict로 최대숫자 개수 구해서 stack처럼. 혹은 일단 number 앞에서 순회하면서 큰숫자개수 만나면 -1 하면서 가면 될듯?
    # *9가 떨어지면 8만 쭉 고르면.. -> 근데 이건 또 앞에서 이미 걸러졌으면 뒤에서 8개수가 모자를 수도 있음
    # 이것도 고민해야 할듯
    # 아. max_num_stack같은거 만들어서 = [9,8,7,6,5,4,3,2,1] 이렇게 하고 dict에서 value값 떨어지면 stack.pop(0)하는 식으로?
    # key_stack, value_stack 각각?
    # 노노. stack을 잘 짜면 할 수 있었음

# def solution(number, k):
#     length, remain = len(number), len(number)-k
#     stack = [0]


#     for ele in number:
#         if remain and stack[-1] < ele:
#             stack.pop()
#             stack.append(ele)
        
#     return  # 실패..

# number를 순회하면서 stack에 하나씩 넣고, 뒷자리와 비교해서 현재자리가 낮으면?
# stack.pop() -> [while로 반복]-> [while 끝] stack.append(num)해서 교체
# 핵심원리는: 일단 앞에서부터 계속 걸러내가는 것임
    # 뒤의수가 얼마나 크든, 앞의자리가 1이라도 크면 장떙 (20 vs 19)
# k를 소모시키면서 = 낮은 앞 자리수를 최대한 제거하면서 가면 어찌되었든 최대자리가 나오는 것
# def solution(number, k):
#     stack = []  # 스택 초기화

#     for num in number: 
#         # 스택이 비어있지 않고, 스택의 마지막 요소가 현재 숫자보다 작고, 아직 제거할 숫자가 남아있는 경우
#         while stack and stack[-1] < num and k > 0:
#             k -= 1  # 제거할 숫자를 하나 줄임
#             stack.pop()  # 스택의 마지막 요소 제거
#         stack.append(num)  # 현재 숫자를 스택에 추가
    
#     if k != 0:  # 아직 제거할 숫자가 남아있는 경우
#         stack = stack[:-k]  # 스택의 마지막 k개 요소 제거
    
#     return ''.join(stack)  # 스택의 요소를 문자열로 변환하여 반환


# print(solution("1924",2))
# print(solution("1231234",3)) # 3234
# print(solution("4177252841",4))
# print(solution("4177252841",6)) # 7841 / 여기 예시보면 확실히 코드 이해될듯
# print(solution("4177252841",7)) # 841 / 여기 예시보면 확실히 코드 이해될듯

# 레퍼런스
def solution(number, k):
    stack = []

    for num in number:
        while stack and stack[-1] < num and k>0:
            k -= 1
            stack.pop()
        stack.append(num)
    
    # 이 부분이 정확히 언제 쓰이는가? - '10000', 2의 경우
    # 위에서 크기 비교는 '<'였음. <=가 아니란 것
        # 이 경우, 같은 경우는 k는 그대로 남고, stack.pop도 되지 않고 남게 됨
    if k != 0: 
        stack = stack[:-k]
    
    return ''.join(stack)


print(solution("4177252841",8))
print(solution('10000',2))