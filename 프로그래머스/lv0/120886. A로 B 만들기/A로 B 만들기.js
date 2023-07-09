// 순서를 바꾼다는게.. 무슨 말이지? 무슨 의미일까
  // 아. 그냥 sort해서 다른게 나오면 false일듯?
// let a = "olleh"
// let b = a.split("")

// console.log(b)
// console.log(b.sort())
// console.log(b.sort((a,b)=>a-b)) <- 이건 안되네. 어찌보면 당연하지 문자인데..숫자처럼 비교가안되잖아

function solution(before, after) {
  let beforeArr = before.split("").sort()
  let afterArr = after.split("").sort()
  
  for (let i=0; i<before.length; i++) {
    if (beforeArr[i] !== afterArr[i]) return 0
  }
  
  return 1
}