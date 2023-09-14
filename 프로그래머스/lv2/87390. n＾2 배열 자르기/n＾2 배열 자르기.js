// 2트: 
function solution(n, left, right) {
  let answer = []
  
  for (let i=left; i<=right; i++) {
    let divide = parseInt(i/n)
    let rest = i%n

    if (divide>=rest) {
      answer.push(divide+1)
    } else {
      answer.push(rest+1)
    }
  }

  return answer
};

console.log(solution(3,2,5));
console.log(solution(4,7,14));