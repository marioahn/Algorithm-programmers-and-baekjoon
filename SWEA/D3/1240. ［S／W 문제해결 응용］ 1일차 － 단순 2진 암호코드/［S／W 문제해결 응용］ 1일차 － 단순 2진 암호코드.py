# 아. 총 자리수는 56개이고, 0~9모두 1로 끝남
# 각 줄에서 1로 끝나는 지점부터 56개 세고,
    # index(거꾸로)
# 그 다음부터 pw dict에서 패턴찾으면 됨
T = int(input())

for tc in range(1,T+1):
    password = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }

    N, M = map(int,input().split())
    pattern = ''
    for _ in range(N):
        row = input()
        if '1' in row:
            pattern = row


    pattern_list = list(pattern)
    pattern_list.reverse()
    last_index = pattern_list.index('1')

    parts = pattern[(-last_index-56):-last_index]
    split_7parts = [parts[i:i + 7] for i in range(0, len(parts), 7)] # 7개씩 쪼개기

    even, odd, i = [], [], 0
    for part in split_7parts:
        if i % 2 == 0:
            even.append(password[part])
        else:
            odd.append(password[part])
        i += 1 

    result = sum(even)*3 + sum(odd)

    if result % 10 == 0:
        print(f'#{tc} {sum(even)+sum(odd)}')
    else:
        print(f'#{tc} {0}')