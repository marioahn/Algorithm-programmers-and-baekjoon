// 걍 함수 따로 만들어서, 약수의 개수

function divisor(n) {
  let cnt = 0
  for (let i=1; i<=n; i++) {
    if (n%i===0) cnt ++
  }
  return cnt
}

function solution(left, right) {
  let answer = 0;

  for (let i=left; i<=right; i++) {
    if (divisor(i)%2===0) { answer += i }
    else { answer -= i }
  }
  return answer;
}


// 제곱근이 정수면, 약수의 갯수가 홀수.....생각해보면..당...연한..건..데...
// function solution(left, right) {
//     var answer = 0;
//     for (let i = left; i <= right; i++) {
//         if (Number.isInteger(Math.sqrt(i))) {
//             answer -= i;
//         } else {
//             answer += i;
//         }
//     }
//     return answer;
// }