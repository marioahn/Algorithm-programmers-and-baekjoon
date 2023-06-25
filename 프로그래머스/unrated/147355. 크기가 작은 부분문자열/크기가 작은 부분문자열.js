// '02' -> Number('02') 하면 어떤가?
// '3141592', '271' -> t의 길이는 7, p의 길이는 3
// (012) (123) (234) (345) (456) 

function solution(t, p) {
  let cnt = 0;

  for (let i=0; i<=t.length-p.length; i++) {
    let sliceNum = +(t.slice(i,i+p.length)) // +로 숫자화
    if (sliceNum <= (+p)) cnt ++
  }
  
  return cnt
}