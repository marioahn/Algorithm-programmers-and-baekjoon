function solution(s) {
  let answer = [];
  
  for (let i = 0; i < s.length; i++) {

      let abc = -1

      for (let j = i - 1; j >= 0; j--) {

          if (s[j] === s[i]) {
              abc = i - j
              break
          }
      }
      answer.push(abc)
  }
  return answer;
}