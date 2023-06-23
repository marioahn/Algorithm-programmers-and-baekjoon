/*
let a = 'ab'
a = a.replace('a','cd')
console.log(a) // cdb
*/
function solution(rny) {
  var answer = '';
  for (let i=0; i<rny.length; i++) {
    if (rny[i] === 'm') {
      answer += 'rn'
    } else answer += rny[i]
  }

  return answer;
}