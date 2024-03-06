# 조금 더 다듬어보자
def solution(players, callings):

    dict = {name: idx for idx,name in enumerate(players)}

    for calling in callings:
        rank = dict[calling]
        dict[calling] = rank-1

        # calling앞에 있는 사람을 players배열에서 찾아서 등수1개 올리기
        dict[players[rank-1]] = rank
        players[rank-1], players[rank] = players[rank], players[rank-1]
    
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))