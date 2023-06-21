function solution(arr, k) {
  let answer = [];
  let set = new Set(arr);
  let arr2 = [];
  arr2.push(...set);
  
  if (arr2.length > k) {
      for (let i = 0; i < k; i++) {
          answer.push(arr2[i])
      }
  } else {
    answer = [...arr2]
    for (let i = 0; i < k-arr2.length; i++) { // -1을 추가할 방법은??
      answer.push(-1) // answer.push(-1)
      
    }
  }
  return answer;
}