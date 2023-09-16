// 일단, 쭈욱 해보자
// stack으로 계속 밀고 나가고, 중간에 비우고 반복해야할 듯
  // stack도 obj화 ㅇㅇ -> 아닌가 일단 pop, push한 후에 해보자
  // 어차피, 배열로 만들어도 stack에 각각 어떤 종류가 몇개씩 잇는지 cnt해야하잖아 -> 걍 obj
function solution(want, number, discount) {
  let cnt = 0
  let wantObj = {}
  for (let i=0; i<want.length; i++) {
    wantObj[want[i]] = number[i]
  };

  let stackObj = {}
  for (let k=0; k<10; k++) {
    if (!stackObj[discount[k]]) stackObj[discount[k]] = 1
    else stackObj[discount[k]] += 1
  } // 초기값 담기

  for (let i=0; i<discount.length-10+1; i++) {
    // i=0일때, 즉 처음에 초기값 담은것도 cnt검사는 해야지 ㅇㅇ; 
    if (i !== 0) {
      // 처음꺼 pop
      if (stackObj[discount[i-1]]) stackObj[discount[i-1]] -= 1
      // 새로운거 push
      if (stackObj[discount[i+9]]) stackObj[discount[i+9]] += 1
      else stackObj[discount[i+9]] = 1
    };
    
    let flag = true;
    for (let i=0; i<want.length; i++) {
      if (stackObj[want[i]] !== wantObj[want[i]]) {
        flag = false
        break
      }
    };
    

    if (flag) cnt++
  };

  return cnt;
}

// 15개 -> 0~9, 5~14 -> 6개 -> 15-10

console.log(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]));

console.log(solution(["apple"],[10],["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]));
