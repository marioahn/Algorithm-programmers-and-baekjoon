// 정수 제곱근 판별?
  // 반복문 돌려서 될때까지 하는건 너무 비효율..뭐더라
  // 유클리드 호제법? ㄴㄴ

// function solution(n) {
//   let answer = 0
//   let sqrtN = Math.sqrt(n)
//   Number.isInteger(sqrtN) === true ? answer = Math.pow(sqrtN+1,2) : answer = -1

//   return answer
// }
function solution(n) {

  let sqrtN = Math.sqrt(n)

  return Number(sqrtN) === parseInt(sqrtN) ? (sqrtN+1) ** 2 : -1
}