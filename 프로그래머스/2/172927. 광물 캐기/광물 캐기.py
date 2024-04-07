# 레퍼런스풀이 - https://yunchan97.tistory.com/48#toc-link-5
# *어째서 이 풀이가 되는가? "최소 피로도이고," 광물은 순서대로 캐야한다
    # 뒤에 어떤 광물들이 있을 줄 알고, 하는가? -> 나는 처음에는 "dfs"로 풀어야 하는 줄 알았다
    # 그러나, 아래처럼 하면 된다. 뒤에 어떤 광물들이 있을 줄 알고? -> 5개씩 자른 unit부분들을
        # 그냥 다이아/철/돌이 많은 순서로 정렬하면 되잖아
        # 광물을 순서대로 캐야한다고만 되어있지, 전체적인 광물 순서를 모른다고 하지는 않았다
        # 따라서, 이렇게 정렬해서 앞에서부터 다이아 -> 철 -> 돌곡괭이 순서대로 소진시키면 문제 없다
    # 즉, 미.리 전체적인 배치를 하는 셈 -> 박수;;

# 결과: 광물의 갯수만큼 반복하니 시간 복잡도는 O(N)
def solution(picks, minerals):
    # 1. 곡괭이*5만큼 캘 수 있으므로 자르기
    mining_capacity = sum(picks)*5
    if len(minerals) > mining_capacity:
        minerals = minerals[:mining_capacity]
    
    # 2. 5개씩 분할하고, dia, iron, stone가격 세주기
    five_units = [[0,0,0] for _ in range(len(minerals)//5+1)]
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            five_units[i//5][0] += 1
        elif minerals[i] == 'iron':
            five_units[i//5][1] += 1
        else:
            five_units[i//5][2] += 1

    # 3. five_units를 정렬 -> 다이아 > 철 > 돌 광석이많은 순서대로
        # 전체적인 곡괭이 배분을 미리하는 셈
    five_units.sort(key=lambda x: (-x[0],-x[1],-x[2]))

    # 4. five_units순회하면서 채굴하고, 피로도 계산하기!
        # 위에서 정렬했으므로, 이제 그냥 순서대로 다이아>철>돌곡괭이 순서대로 쓰면서 가면 됨
    fatigue = 0
    for i in range(len(five_units)):
        dia, iron, stone = five_units[i][0], five_units[i][1], five_units[i][2] # 광석cnt
        if picks[0] > 0: # 다이아 곡괭이 먼저
            fatigue += dia+iron+stone
            picks[0] -= 1
        elif picks[1] > 0:
            fatigue += dia*5+iron+stone
            picks[1] -= 1
        else: # 돌곡괭이만 남았으면
            fatigue += dia*25+iron*5+stone
            picks[2] -= 1

    return fatigue

# [[3, 2, 0], [1, 1, 1]]
print(solution([1, 3, 2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))