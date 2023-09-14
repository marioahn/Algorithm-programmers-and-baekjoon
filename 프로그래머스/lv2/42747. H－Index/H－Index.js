function solution(citations) {
  let Max = Math.max(...citations);

  let answer = 0
  for (let i=1; i<=Max; i++) {
    let [up, down] = [0,0];

    for (let j=0; j<citations.length; j++) {
      if (citations[j] >= i) {
        up ++
      }
      if (citations[j] <= i) {
        down ++
      }
    };

    if (up>=i && down<=i) answer = i
  }

  return answer
}

console.log(solution([3, 0, 6, 1, 5]))