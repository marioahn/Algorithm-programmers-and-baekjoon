// 네비게이터
// 반복문을 사용하여 a[i]와 b[i] 값을 곱하여 더한 값을 answer 에 push 합니다.



// ----------
function solution(a, b) {
  var answer = 0;
  
  for (let i=0; i<a.length; i++) {
    answer += a[i]*b[i]
  }

  return answer;
}

console.log(solution([1,2,3,4],[-3,-1,0,2]))