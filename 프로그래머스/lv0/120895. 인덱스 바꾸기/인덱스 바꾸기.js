// 상한님 힌트: 구조분해할당??
  // let a = '123'

  // let b = [...a]

  // tmp = a[1]

  // b[0] = tmp
  // b[1] = a[0]
  // console.log(b)

function solution(str, num1, num2) {
  let arr = [...str];
  [arr[num1], arr[num2]] = [arr[num2], arr[num1]]
  return arr.join("")
  

}