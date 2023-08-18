function solution(n) {
  let answer = [];

  for (let i=String(n).length-1; i>=0; i--) {
    answer.push(Number(String(n)[i]))
  }

  return answer
}