function solution(n) {
  function oneCount(num) {
    let toTwo = num.toString(2)
    let cnt = toTwo.replaceAll('0','').length
    return cnt
  }
  
  let answer = oneCount(n)

  while (1) {
    n += 1
    if (oneCount(n) === answer) {
      return n
    }
  }
}