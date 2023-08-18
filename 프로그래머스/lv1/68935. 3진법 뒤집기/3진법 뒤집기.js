// {10진수}}.toString(n)를 사용해 10진수를 원하는 n진수로 변환가능
// let n = 125
// let trinary = n.toString(3)
// console.log(trinary, typeof trinary) // 11122 string

function solution(n) {
  let sum = 0
  let trinary = n.toString(3)

  for (let i=0; i<trinary.length; i++) {
    sum += (+trinary[i]) * Math.pow(3,i)
  }
  return sum
}

/* 아래처럼 parseInt(~,num) <ㅡ num에 적힌숫자진법을 10진법으로 바꿔줌
function solution(n) {
    return parseInt(n.toString(3).split('').reverse().join(''), 3);
}
*/