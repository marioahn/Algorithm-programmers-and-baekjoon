// arr.push 라는 메서드가
  // 1. 단독으로 사용될 때
  // 2. return 과 함께 쓰일 때의
// 2가지의 차이점을 주의할 것
function solution(n) {
  let collatzArr = [n];

  while (n !== 1) {
    if (n%2) { // 홀수라면
      n = n*3+1
      collatzArr.push(n)
    } else {
      n = n/2
      collatzArr.push(n)
    }
  }

  return collatzArr;
}