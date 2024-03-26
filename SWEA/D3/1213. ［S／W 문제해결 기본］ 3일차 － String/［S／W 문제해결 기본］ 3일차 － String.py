for tc in range(1,11):
    num = int(input())
    pattern = input()
    text = input()

    # cnt, p_len = 0, len(pattern)
    # for i in range(len(text)-p_len+1):
    #     if text[i:i+p_len] == pattern:
    #         cnt += 1

    # print(f'#{tc} {cnt}')
    print(f'#{tc} {text.count(pattern)}')

