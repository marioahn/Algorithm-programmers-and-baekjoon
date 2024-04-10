# 1. 콜라츠 수열 구하기 - 리스트에 담기
# 각 idx는 x좌표가 되는 셈 / list[idx]는 y좌표가 되고.
# 사다리꼴: (밑변+윗변)*높이/2
# 각 구간 적분 계산 -> 라이브러리? 
    # 근데, 하나의 함수로 이어진 곡선의 아래면적 구하는 것도 아니고
    # *각각의 구간은 사다리꼴인데, 이걸 적분 계산이 되는건가..?
# 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간이 주어지면, -1
# final: 소숫점없으면 int로, 아니면 0.5 -> float형으로 // 나누기2이므로 소숫점은 0.5만 나옴
def collatz_sequence(n): # 콜라츠수열
    arr = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
            arr.append(n)
        else:
            n = n*3+1
            arr.append(n)

    return arr


def solution(k, ranges):
    collatz_arr = collatz_sequence(k)
    collatz_len = len(collatz_arr)

    collatz_section_integral = []
    for i in range(collatz_len-1):
        collatz_section_integral.append((collatz_arr[i]+collatz_arr[i+1])/2)
    
    result = []
    for ele in ranges:
        a, b = ele[0], ele[1]
        if (a==0 and b==0): 
            result.append(sum(collatz_section_integral))
        elif a == collatz_len-1+b:
            result.append(0.0)
        elif a > collatz_len-1+b:
            result.append(-1.0)
        else:
            result.append(sum(collatz_section_integral[a:collatz_len-1+b]))

    # float.is_integer()로 소숫점 있으면 float, 없으면 int로
    # result = [x for x in result if x.is_integer()==True else int(x)] # 문법 잘못;;
    result = [int(x) if x.is_integer() else x for x in result]
    
    return result


print(solution(5,[[0,0],[0,-1],[2,-3],[3,-3]])) # [33.0,31.5,0.0,-1.0]
print(solution(3,[[0,0],[1,-2],[3,-3]])) # [47.0,36.0,12.0]