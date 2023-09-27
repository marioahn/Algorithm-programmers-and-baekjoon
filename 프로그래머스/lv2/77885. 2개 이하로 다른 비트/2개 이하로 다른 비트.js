// 흠.. 보면 패턴이 보인다
// 1. 짝수를 2진법으로 나누면, 1의자리수는 무조건 0이기 때문에, f(x)는 x+1이 된다
  // 그 다음수는 나머지는 모두 똑같고, 1의 자리수만 0에서 1이 되기 때문이다
// 2. 홀수가 약간 골 때린다
  // x를 4로 나눈 나머지가 1인 경우의 f(x) = x+1이다
    // f(1) = 2, f(5) = 6, f(9) = 10, f(13) = 14, f(17) = 18
  // x를 4로 나눈 나머지가 3인 경우는?
    // 01부분을 10으로 나누면 된다
    // 1011 -> 1101로, 10011 -> 10101, 10111 -> 11011
    // 만약, 0이 없다면? 예로 들어서 11의 경우? 맨 앞에 0을 만들고, 바꾸면 된다
    // 11 -> 011 => '101'가 f(x)의 답이다 / 0111 -> 1011

function solution(numbers) {
  let result = []

  for (let number of numbers) {
    if (number % 2 === 0 || number % 4 === 1) result.push(number+1)
    if (number % 4 === 3) {
      if (number.toString(2).indexOf('0') === -1) { // 111같은 경우면 0111 => 1011로
        let tmp = '0'+number.toString(2)
        let tmp2 = '10'+ tmp.substr(2)
        result.push(parseInt(tmp2,2))
      } else { // 10011 -> 10101로 바꿔야 함
        let tmp = number.toString(2)
        for (let i=tmp.length-1; i>=0; i--) {
          if (tmp[i-1]+tmp[i] === '01') {
            tmp = tmp.substr(0,i-1)+'10'+tmp.substr(i+1)
            break
          }
        }
        result.push(parseInt(tmp,2))
      }
    }
  }
  return result
}

console.log(solution([2,7]))