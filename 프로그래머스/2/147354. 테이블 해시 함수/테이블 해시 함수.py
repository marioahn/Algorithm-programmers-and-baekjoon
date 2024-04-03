# 단지, col번째 오름정렬이 안되면 첫번째로 내림 -> 정렬조건 2개뿐
# hash값: 다르면 1, 같으면 0 -> 2진법 -> 10진법 결과 return
# between해시값은 그냥 합 구하면 될듯? 1000 1001 인경우, 첫 글자 평균이 1이면 같으니까 0하면 되고, 0이면 0하면되고 etc
# 110, 1100있으면 어케해야하냐 -> 110 ->0110으로 0채워서 마저 비교해야함? 일단 위대로 하면 일단 채우긴 해야할듯

# 1트 - 실패: 비트 연산자의 누적 계산도 잘못 이해했고, 코드도 너무 번잡 ㅠ
# def solution(data, col, row_begin, row_end):
    

#     data2 = sorted(data, key=lambda x: (x[col-1], -x[0])) # -는 내림차순 의미
#     data3 = data2[row_begin-1:row_end]
#     all_s = []

#     div = row_begin
#     for ele in data3:
#         sum = 0
#         for ele2 in ele:
#             sum += ele2 % div  
#         div += 1
#         all_s.append(bin(sum)[2:])

#     # 테이블의 해시 값 구하기
#     max_length = max(len(a) for a in all_s) # *와 파이썬은 함수의 인자에도 컴프리헨션이 되네 ㅋㅋ
#     for i in range(len(all_s)):
#         if len(all_s[i]) < max_length:
#             all_s[i] = '0'*(max_length-len(all_s[i]))+all_s[i]
    

#     # 아. 이렇게 하면 안됨 -> S1~S3이 있으면 순서대로 S1,s2의 결과 -> newS vs S3 이렇게 되어야 함
#     # S1~3을 모-두 한꺼번에 비트연산자 비교하는게 아님 ㅠ
#     hash = ''
#     for j in range(len(all_s[0])):
#         sum2 = 0
#         for i in range(len(all_s)):
#             sum2 += int(all_s[i][j])
        
#         if sum2 % len(all_s) == 0:
#             hash += '0'
#         else:
#             hash += '1'

#     return int(hash,2)
def solution(data, col, row_begin, row_end):
    # 조건에 따라 데이터 정렬: col번째 컬럼 오름차순, 같으면 첫 번째 컬럼 기준 내림차순
    sorted_data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    
    # 누적 XOR 값을 계산하기 위한 초기 값 설정
    hash_value = 0
    
    # row_begin부터 row_end까지 각 행에 대해 연산 수행
    for i in range(row_begin-1, row_end):
        # 현재 행의 S_i 계산
        S_i = sum(x % (i + 1) for x in sorted_data[i])
        print(S_i)
        # 누적 XOR 연산 수행
        hash_value ^= S_i # ^=는 걍 비트연산자 바로 계산해줌 ㅠ 내가 구현할 필요 X..
    
    return hash_value


print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]],2,2,3))