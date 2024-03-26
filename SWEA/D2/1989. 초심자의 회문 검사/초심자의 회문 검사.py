T = int(input())

for tc in range(1,T+1):
    # 1. way1
    chr = input()
    if chr == chr[::-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
    
    # 2. way2
    # chr2 = list(chr)
    # chr2.reverse()
    # chr2 = ''.join(chr)

    # 3. way3
    # for i in range((len(chr)//2)+1):
    #     if i == (len(chr))//2:
    #         print(1)
    #     if chr[i] == chr[-i-1]:
    #         continue
    #     else:
    #         print(0)
    #         break

