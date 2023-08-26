function solution(s, skip, index) {
  let canWords = Array.from({length: 26}, (value,index) => String.fromCodePoint(index+97)).filter(ele => !(skip.includes(ele)))

  let answer = ''
  for (let i=0; i<s.length; i++) {
    for (let j=0; j<canWords.length; j++) {
      if (s[i] === canWords[j]) {
        answer += canWords[(j+index)%(canWords.length)]
      }
    }
  }
  return answer;
}


console.log(solution("aukks", "wbqd",5))