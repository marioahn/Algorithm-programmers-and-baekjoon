// 두 수 m과 n이 있을 때, m * n = 최대공약수(GCD) * 최소공배수(LCM)
  // 최대공약수 구하는게 더 빠를거 같다
  // m,n은 1이상 1000000이하의 자연수 -> 유클리드 호제법으로 구하자

// 유클리드호제법: big > small인 경우 -> 중간에 small리턴하는거임 ㅇㅇ주의!!
function gcd(big,small) {
  let remainder = big % small
  if (remainder===0) return small
  return gcd(small,remainder)
}

function solution(n, m) {
  let gcdNum = 0
  if (n>=m) {
    gcdNum = gcd(n,m)
  } else {
    gcdNum = gcd(m,n)
  }

  return [gcdNum, n*m/gcdNum]
}

