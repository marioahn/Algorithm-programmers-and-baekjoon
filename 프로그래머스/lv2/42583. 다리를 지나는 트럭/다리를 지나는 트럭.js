// 흠;;
// 트럭이 들어온지 몇초 지났는지를 세는 stack2를 하나 더 만들까?
// 만약, 아래에서 stack.push가 되면, stack2도 1을 푸쉬하는 것
// 매.초.마다 stack2는 항상 모든 요소가 늘어가고, 만약 length를 초과하면 stack1을 없애기.

function solution(bridge_length, weight, truck_weights) {
  let stack = []
  let onStack = []
  let cnt = 0
  let stackSum = 0

  while (truck_weights.length || stack.length) {
    cnt ++; // 매초
    
    onStack = onStack.map(item => item+1)
    if (onStack[0] === bridge_length) {
      stackSum -= stack[0]
      stack.shift()
      onStack.shift()
    }
    
    if (truck_weights[0]+stackSum <= weight) {
      stackSum += truck_weights[0]
      stack.push(truck_weights.shift()) // 빼고, 넣기
      onStack.push(0)
    };
  }

  return cnt
}

// console.log(solution(2,10,[7,4,5,6]))
console.log(solution(4,2,[1, 1, 1, 1])) // 10
console.log(solution(5,5,[1,1,1,1,1,2,2])) // 14
console.log(solution(7,7,[1,1,1,1,1,3,3])) // 18
console.log(solution(5,5,[1,1,1,1,1,2,2,2,2])) // 19
console.log(solution(5,5,[2, 2, 2, 2, 1, 1, 1, 1, 1])) // 19