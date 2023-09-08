// 2트: 위처럼 하지말고, 그냥 '라운드'로 보자
  // 각각의 번호가 몇 라운드에서 만나는지?
  // 1트는 a,b를 각각 조작하기 때문에 시간이 더 걸리는 것
  // 이 경우는 a,b 대소 판단도 필요 없다!

function solution(n,a,b) {
  
  let cnt = 0

  while (a !== b) {
    a = Math.ceil(a/2)
    b = Math.ceil(b/2)
    cnt ++ 
  }

  return cnt
}

console.log(solution(8,4,7))
console.log(solution(2**20,1,2**20-1))