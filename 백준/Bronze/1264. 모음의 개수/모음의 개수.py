bucket = ['a', 'e', 'i', 'o', 'u']  # 아 이것도 필요 없음.. in문법쓸거니까
while True:
    strings = input()
    if strings == '#':
        break
    cnt = 0
    for string in strings:
        if string in 'aeiouAEIOU':
            cnt += 1
    print(cnt)
