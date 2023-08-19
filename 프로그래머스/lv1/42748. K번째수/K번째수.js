function solution(array, commands) {
  let answer = [];

  for (let i=0; i<commands.length; i++) {
    // let tmp = array.slice(commands[i][0]-1,commands[i][1]).sort()
    let tmp = array.slice(commands[i][0]-1,commands[i][1]).sort((a,b)=> a-b) // <- 이렇게 써야 통과!
    answer.push(tmp[commands[i][2]-1])
  }
  return answer;
}

// let tmp = array.slice(commands[i][0]-1,commands[i][1]).sort()
// 이거 tc 한개 통과 못함 ..? array의 각원소는 100까지임 ㅇㅇ. 100도 들어올 수 있음
// let a = [20, 100,10,15,51,15]
// a.sort()

// console.log(a) // [ 10, 100, 15, 15, 20, 51 ] -> 이렇게 됨!
// 와 진짜;; 명심하자 걍 sort는 항.상 원래 표현까지 전.부 써주자 숫자라고 방심해버렸네
// 문자열 sort할때는 뒤에꺼까지 제대로 써줬는데
// let tmp = array.slice(commands[i][0]-1,commands[i][1]).sort((a,b)=> a-b)