# 가로확인 -> 세로확인: 이때 ,가로회전?
    # 걍 처음 입력값 받아서 arr만들고(이건 가로기준이지)
    # arr2를 만들어서 세로값을 가로줄처럼 받은 것 만들고
    # check 반복문 돌려서 arr, arr2동시 검사
    # *근데 이러한 방식은 너무 원시적 -> n길이 길어지면 시간多
        # -> 규칙 없으려나

for tc in range(1,11):
    find_len = int(input())

    arr_row = []
    for _ in range(8):
        arr_row.append(list(input()))

    # 세로 -> 가로회전
        # ''.join말고, list를  하는 이유는 아래에서 reverse()돌리기 위해 - str은 reverse() x
    arr_column = [list(arr_row[j][i] for j in range(8)) for i in range(8)]

    cnt = 0
    for i in range(8): # 행
        for j in range(8-find_len+1):
            row_str = arr_row[i][j:j+find_len]
            column_str = arr_column[i][j:j+find_len]

            tmp1, tmp2 = row_str[:], column_str[:] # 원본 변화 방지
            tmp1.reverse()
            tmp2.reverse()
            if row_str == tmp1:
                cnt += 1
            
            if column_str == tmp2:
                cnt += 1

    print(f'#{tc} {cnt}')