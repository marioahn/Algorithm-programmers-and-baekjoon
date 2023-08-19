function solution(a, b, n) {
  let result = 0
  while (n >= a) {
    result += parseInt(n/a)*b
    n = n - parseInt(n/a)*a + parseInt(n/a)*b
    
  }

  return result
}

console.log(solution(3,1,20))