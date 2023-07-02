function solution(n) {
  let primeArr = []

  // 1)n이 홀수가 될때까지 나누기
  while (n%2 == 0) {
    primeArr.push(2) // 2가 중복으로 들어갈 수 있으니 마지막에 ...new Set(arr)!
    n = n/2
  }

  // 2)이제 n은 홀수 -> 이미 2의 배수를 판별했기때문에 2씩 증가시킬 수 있음
  for (let i=3; i*i<=n; i=i+2) {
      while (n%i===0) {
        primeArr.push(i)
        n = n/i
      }
  }

  // 3)최후의 수가 된 경우 - 즉, 1과 자기자신(<-소수)만 인수인 상태
  if (n>2) { // 1)작업을 통해
    primeArr.push(n)
  }
  
  return [... new Set(primeArr)]
}
