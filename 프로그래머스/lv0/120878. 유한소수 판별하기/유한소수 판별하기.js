// 1. 일단 기약분수로 만들어야 함 how?
  // 기약분수: 분자, 분모의 최대공약수로 서로 나눠주면 기약분수가 된다
  // 방법: gcd함수 이용
// 2. (나눈 후)분모의 소인수(=소수인 인수)가 2와 5만 존재해야 함
  // 판별법 -> 그 수의 제곱근까지 인수 구하는 거 돌려서 ㅇㅇ.
  // why 제곱근? -> 탐색개수 줄이기 위함
// 3. 소인수들을 넣은 배열의 합이 2, 5, 7이 아니면 false

function gcd(big, small) {
  let remain = big % small
  if (remain === 0) return small
  return gcd(small,remain)
}

function primeFactors(n){
  let primeArr = []
  // (1)n분해 작업1 ( n = 20 )
  while (n%2 == 0) {
    primeArr.push(2)
    n = n/2
  } 
  // 이제 n은 홀수 -> 이미 2의 배수를 판별했기때문에 2씩 증가시킬 수 있음

  // (2)n분해 작업2 ->  ( n=20 -> 5가 되었음 )
  for (let i=3; i<=Math.sqrt(n); i+=2) {
    while (n%i==0) {
        primeArr.push(i)
        n = n/i
    }
  }

  // (3)n분해 작업3 ->  ( n은 1이 되었음 -> 아래 코드 작동x)
    // 여기까지 왔음에도 살아남은 n은 그 자체로 소.수인 경우 
  if (n>2) { primeArr.push(n) } 

  return [... new Set(primeArr)] // 중복제거한 배열 return
  
}

function solution(a, b) {
  if (Number.isInteger(a/b)) {return 1}
  let result = 2 // 기본은 2(=기약분수가x)
  // 어라.. 소수..? 소수는 1이하인 건가? 아니면 1.5도 소수..?
  let abGcd = (a>=b) ? gcd(a,b) : gcd(b,a)
  let b2 = b / abGcd
  let arr = primeFactors(b2) // b2의 소수인 인수들을 담은 배열

  let sum = 0
  for (let i=0; i<arr.length; i++) {
    sum += arr[i]
  }

  if (sum === 2) {result = 1}
  if (sum === 5 && arr.length === 1) {result = 1} // 여기 length조건 추가해야함
  if (sum === 7 && arr.length === 2) {result = 1} // 여기도 -> b2가 7인경우 ㅇㅇ.

  return result
}