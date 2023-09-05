// fibonachi함수 재귀로 어떻게 하더라

function solution(n) {
  let fibonachi = [0,1]

  while (n >= 2) {
    fibonachi.push((fibonachi.at(-2)+fibonachi.at(-1))%1234567)
    n -= 1
  }
  
  return fibonachi.at(-1)
}

console.log(solution(6))