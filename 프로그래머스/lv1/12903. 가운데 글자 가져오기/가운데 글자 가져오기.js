function solution(s) {
  var answer = '';

  const midLeft = s[(s.length/2-1)] // 가운데왼쪽 글자
  const midRight = s[(s.length/2)]

  if (s.length % 2 === 0) {
      answer = midLeft + midRight
  } else {
      answer = s[(Math.floor(s.length/2))]
  }
  return answer;
}