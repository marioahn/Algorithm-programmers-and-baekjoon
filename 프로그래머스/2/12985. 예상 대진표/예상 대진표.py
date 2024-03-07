# 짝수번호는 이기면 -> 다음 번호는 /2
# 홀수번호는 이기면 -> 다음 번호는 (+1)/2
# (1,2) (3,4) (5,6) (7,8)
    # 각 합은 3 7 11 15 -> 즉, 4*n+3이면 같은 팀임
    # 아니네.. 첨 예시에서 A, B= 4, 7 -> 11.......ㅎㅎ;;
    # 근데 어차피, next_stage함수에 의해 다음 스테이지 번호가 정해지고,
    # 같은 팀이면 스테이지 번호가 같음. 즉, a==b조건이면 끝남

def next_stage(num):
    if num % 2: 
        num = (num+1)//2
    else:
        num //= 2
    return num

def solution(n,a,b):
    cnt = 0

    while a!=b:
        cnt += 1
        a, b = next_stage(a), next_stage(b)

    return cnt


print(solution(8,4,7))