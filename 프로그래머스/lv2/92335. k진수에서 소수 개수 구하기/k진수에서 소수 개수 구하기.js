// 보통은 최소 사이드 한쪽에 0을 끼고 있어야 함
// 단, 'P처럼 소수 양쪽에 아무것도 없는 경우' 경우도 있음. 마지막에 이거 처리해주기
  // -> k진수로 n을 변환시킨게 121 뭐 이런 경우일듯
// 먼저, 소수구하는 로직 만들고,
// stack으로 왼쪽부터 쭉 밀고가면서 소수 검증 - 0만나면
function isPirme(num) {
  if (num === 1) return false
  if (num === 2) return true
  if (num % 2 === 0) return false
  for (let i=3; i<=Math.sqrt(num); i+=2) {
    if (num % i === 0) return false
  }
  return true
}

function solution(n, k) {
  let cnt = 0
  let stack = ''

  let changed = n.toString(k)
  let length = changed.length

  // 먼저, 0이 아예 없으면 그냥 그거 통째로 소수 검사
  if (changed.indexOf(0) < 0 && isPirme(Number(changed))) {
    return 1
  }
  
  for (let i=0; i<length; i++) {
    if (changed[i] !== '0') stack += changed[i]
    else {
      if (isPirme(Number(stack))) {
        cnt ++
        stack = ''
      } else { stack = '' }
    }
  }

  // changed마지막이 0이 아니면, 위 로직대로라면 stack에 +만되고, 소수 검사는 못함
  if (stack) {
    if (isPirme(Number(stack))) {
      cnt++
    }
  }

  return cnt
}

console.log(solution(437674,3))
console.log(solution(110011,10))
console.log(solution(11,10))