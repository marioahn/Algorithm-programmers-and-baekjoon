function solution(arr) {
    let answer = [arr[0]];
    
    let dupli = arr[0]
    for (let i=1; i<arr.length; i++) {
      if (arr[i] !== dupli) {
        answer.push(arr[i])
        dupli = arr[i]
      }
    }

    return answer;
}

console.log(solution([1,1,3,3,0,1,1]))