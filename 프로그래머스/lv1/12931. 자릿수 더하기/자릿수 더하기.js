function solution(n) { // n = 123
  let answer = 0;
  let tmp = String(n) // tmp = '123'

  for (let i=0; i<tmp.length; i++) {
    answer += Number(tmp[i])
  }

  return answer;
}