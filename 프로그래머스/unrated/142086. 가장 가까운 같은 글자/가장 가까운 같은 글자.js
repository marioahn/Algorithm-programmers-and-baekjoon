// 이미 있는지 없는지 정보를 어케 알아내는가? 새 배열에 담아두기
  // 또한, 가장 최근의 index정보까지 담는다!? 일석이조??
  // key-value 객체로?

function solution(s) {
  let bucket = {}
  let answer = []
  
  for (let i =0; i<s.length; i++) {
    if (bucket[s[i]] === undefined) {
      bucket[s[i]] = i 
      answer.push(-1)
    } else {
      answer.push(i-bucket[s[i]])
      bucket[s[i]] = i 
    }
  }
  return answer
}