function solution(s) {
  let [tryCnt, zeroCnt] = [0, 0];
    
  while (s !== '1') {
    let len = s.length
    let tmpCnt = 0
    for (let i=0; i<len; i++) {
      if (s[i] === '0') tmpCnt ++
    }

    s = (len-tmpCnt).toString(2)
    tryCnt ++ 
    zeroCnt += tmpCnt
  }

  return [tryCnt, zeroCnt]
}

console.log(solution("110010101001"))
console.log(solution("01110"))
console.log(solution("1111111"))