// 2트: 아니지 이건 bfs아닌가??
  // 또한, x->y가 아니라 y->x로 해보자
  // 그러면, if (y % 2 === 0)같은 조건을 더 명확하게 처리할 수 있음 
  // 중간과정을 더 자세하게 가를 수 있다! - 1트의 위 조건들은 엄밀히 말하면, 정확하진 않았다
function solution(x,y,n) {
  let stack = [[y,0]]
  // let answer = 0

  while (stack.length) {
    let [check, cnt] = stack.shift()
    if (check === x) {
      return cnt
    }

    if (check % 2 === 0) {
      stack.push([check/2,cnt+1])
    }
    if (check % 3 === 0) {
      stack.push([check/3,cnt+1])
    }
    if (check - n >= x) {
      stack.push([check-n,cnt+1])
    }
  }

  return -1
}

console.log(solution(10,40,5));
console.log(solution(10,40,30));
console.log(solution(2,5,4));