function solution(players, callings) {
  
  let obj = {}
  for (let i=0; i<players.length; i++) {
    obj[players[i]] = i
  }

  let idx = 0;
  for (let calling of callings) {
    idx = obj[calling]
    obj[calling] -= 1; // 세미콜론 필수
    obj[players[idx-1]] += 1; // 세미콜론 필수
    [players[idx],players[idx-1]] = [players[idx-1],players[idx]];
  };

  return players;
}


console.log(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))