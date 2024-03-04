# 그냥 옹알이 단어 앞에서부터 words에 있는 단어 차례대로 돌리면서 찾고, - index함수
# index함수의 결과로 0이 나오면, -> replace(word,'',1)
    # 또한, 여기서 한번 더 index(word)해서 값이 0이 바로 나오면 연속발음 -> break
# 최종적으로, 옹알이 단어 길이가 0이되면 cnt += 1, 아니면 넘어가고

def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    cnt = 0

    for bab in babbling:
        tmp = 0
        flag = True

        while tmp != len(bab):
            tmp = len(bab)
            for word in words:
                if bab.find(word) == 0:
                    bab = bab.replace(word,'',1)
                    # 연속인 경우
                    if bab.find(word) == 0:
                        flag = False # flag가 False면 절대 cnt+1하지 않는다
            
        if flag == False:
            continue
        if len(bab) == 0:
            cnt += 1

    return cnt

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))