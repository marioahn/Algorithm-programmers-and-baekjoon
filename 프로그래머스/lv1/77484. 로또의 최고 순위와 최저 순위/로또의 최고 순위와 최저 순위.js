// function order(number) {
//   if (number === 6) {
//     return 1;
//   }
//   if (number === 5) {
//     return 2;
//   }
//   if (number === 4) {
//     return 3;
//   }
//   if (number === 3) {
//     return 4;
//   }
//   if (number === 2) {
//     return 5;
//   }
//   if (number === 1) {
//     return 6;
//   }
//   if (number === 0) {
//     return 6;
//   }
// }

// function solution(lottos, win_nums) {
//   // step1: 최저부터 - 0인 경우 모두 continue(로또번호는 1부터이므로 자동으로 걸러짐)
//   // step2: 최고순위 -> minCnt + zeroCnt
//   let minCnt = 0;
//   let zeroCnt = 0;
//   for (let i = 0; i < lottos.length; i++) {
//     if (win_nums.indexOf(lottos[i]) >= 0) {
//       minCnt++;
//     }
//     if (lottos[i] === 0) {
//       zeroCnt++;
//     }
//   }
//   return [order(minCnt + zeroCnt), order(minCnt)];
// }
function solution(lottos, win_nums) {

  let minAnswer = 0
  let zeroCnt = 0
  let minRank = 0
  let maxRank = 0
  for (let i=0; i<6; i++) {
    if (win_nums.indexOf(lottos[i]) >= 0) {
      minAnswer ++
    }
    if (lottos[i] === 0) zeroCnt ++
  }

  // minRank
  minAnswer === 1 || minAnswer === 0? minRank = 6 : minRank = 7 - minAnswer

  // maxRank
  minAnswer + zeroCnt === 1 || minAnswer + zeroCnt === 0? maxRank = 6 : maxRank = 7 - (minAnswer + zeroCnt)

  // console.log(7 - (minAnswer + zeroCnt), minRank) // 최고, 최저 순

  return [maxRank, minRank]
}