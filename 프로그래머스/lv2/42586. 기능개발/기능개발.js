// stack, obj 동시 이용하면 될듯?  - obj? -> ㄴㄴ 걍 간단하네
// 작업끝나기까지 남은 일수 쭉 정리하고, -> 5, 10, 1, 1, 20, 1
// -> 처음부터 순회해서 stack에 저장 - stack[-1]보다 큰거 나오면 stack.length cnt하고
// 스택 비우기

function solution(progresses, speeds) {
  let completed = [];

  for (let i=0; i<speeds.length; i++) {
    let days = Math.ceil((100-progresses[i])/speeds[i])
    completed.push(days)
  };

  let answer = [];
  
  let stack = [completed[0]];
  for (let j=1; j<completed.length; j++) {
    if (stack[0] < completed[j]) {
      answer.push(stack.length)
      stack = [completed[j]]
    } else {
      stack.push(completed[j])
    }
  };

  if (stack) answer.push(stack.length)

  return answer;
}

console.log(solution([93, 30, 55],[1, 30, 5]));
// [ 7, 3, 9 ]
console.log(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])); 
// [ 5, 10, 1, 1, 20, 1 ]