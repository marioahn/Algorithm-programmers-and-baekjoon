def solution(data, col, row_begin, row_end):
    # 조건에 따라 데이터 정렬: col번째 컬럼 오름차순, 같으면 첫 번째 컬럼 기준 내림차순
    sorted_data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    
    # 누적 XOR 값을 계산하기 위한 초기 값 설정
    hash_value = 0
    
    # row_begin부터 row_end까지 각 행에 대해 연산 수행
    for i in range(row_begin-1, row_end):
        # 현재 행의 S_i 계산
        S_i = sum(x % (i + 1) for x in sorted_data[i])
        # 누적 XOR 연산 수행
        hash_value ^= S_i
    
    return hash_value

# 테스트 출력
print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3))