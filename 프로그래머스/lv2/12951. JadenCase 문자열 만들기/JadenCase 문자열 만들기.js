// 3트
function solution(s) {
  let answer = ''
  let stack = ''

  for (let i =0; i<s.length; i++) {
    if (s[i] !== ' ') {
      if (stack === '') { // 공백 다음의 첫 문자인 경우
        stack += s[i].toUpperCase() 
      } else {
        stack += s[i].toLowerCase()
      }
    } else { // s[i]가 ' ' -> 공백이면
      answer += stack + ' '
      stack = ''
    }
  }

  answer += stack // 마지막 단어 추가

  return answer
}


console.log(solution("3people unFollowed me"))
console.log(solution("for the last week"))