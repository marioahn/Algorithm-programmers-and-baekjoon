// 2트: 레퍼런스 코드 참조해서 다시 풀이
function solution(word) {
  // 초기값 - ex) AAA는 3이며, AAE는 5**2+5**1+5**0 + '3'이다
  // 그니까, AAE는 3자리수의 원형인 3에서부터 규칙에 따라 추가되므로, cnt의 초깃값을 word.length로 잡는다
  let cnt = word.length 
  let alphabets = ['A','E','I','O','U']
  let interval = [781, 156, 31, 6, 1]

  for (let i=0; i<word.length; i++) {
    cnt += alphabets.indexOf(word[i]) * interval[i]
  }

  return cnt
}

console.log(solution('AAAAE'))