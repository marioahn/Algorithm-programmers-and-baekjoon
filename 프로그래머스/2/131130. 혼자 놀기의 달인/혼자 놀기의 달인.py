# 만약 1번 상자 그룹을 제외하고 남는 상자가 없으면 그대로 게임이 종료되며,
    # 이 때 획득하는 점수는 0점이다!
# 2개 이상 그룹으로 나뉘게 되면, len(group_i) 상위 2개 곱 return

# group화를 하기전에, 걍 모두 -1씩 해주는게 idx작업하기 편할듯
# 또한, 중복그룹은 제거 - 뽑아낸 상자는 0으로 바꾸고, while sum(cards) != 0으로
def solution(cards):
    cards = [card-1 for card in cards]
    all_box = []
    
    i = 0
    while i<len(cards):
        if cards[i] == -1:
            i += 1
            continue
        else:
            # *와 진짜 이 부분 ㅈㅈㅈㅈㅈㄴ오래 걸렸다.. 머리 너무 굳어버림 ㅠ
            box = []
            now, next_i = i, cards[i] # 초기값
            while cards[now] != -1:
                box.append(cards[now])
                tmp = now
                now, next_i = next_i, cards[next_i]
                cards[tmp] = -1

            all_box.append(box)
    
    all_box.sort(key=lambda x: len(x),reverse=True) # 길이 큰 그룹순으로 정렬
    
    if len(all_box) == 1:
        return 0
    else:
        return len(all_box[0])*len(all_box[1])


print(solution([8,6,3,7,2,5,1,4]))