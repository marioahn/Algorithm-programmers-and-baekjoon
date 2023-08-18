function solution(n) {
  var answer = '';
  temp = '수박'
  if (n%2 === 0 ) { answer = temp.repeat(n/2)}
  else { answer = temp.repeat(parseInt(n/2))+'수'}
  return answer;
}

// 3 -> 수박수, 5 ->수박수박수 
// 4 -> 수박수박, 6 -> 수박수박수박
console.log(solution(4))
