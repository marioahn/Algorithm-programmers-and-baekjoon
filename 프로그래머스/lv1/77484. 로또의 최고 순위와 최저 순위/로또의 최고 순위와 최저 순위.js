function order(number) {
  if (number === 6) {
    return 1;
  }
  if (number === 5) {
    return 2;
  }
  if (number === 4) {
    return 3;
  }
  if (number === 3) {
    return 4;
  }
  if (number === 2) {
    return 5;
  }
  if (number === 1) {
    return 6;
  }
  if (number === 0) {
    return 6;
  }
}

function solution(lottos, win_nums) {
  // step1: 최저부터 - 0인 경우 모두 continue(로또번호는 1부터이므로 자동으로 걸러짐)
  // step2: 최고순위 -> minCnt + zeroCnt
  let minCnt = 0;
  let zeroCnt = 0;
  for (let i = 0; i < lottos.length; i++) {
    if (win_nums.indexOf(lottos[i]) >= 0) {
      minCnt++;
    }
    if (lottos[i] === 0) {
      zeroCnt++;
    }
  }
  return [order(minCnt + zeroCnt), order(minCnt)];
}