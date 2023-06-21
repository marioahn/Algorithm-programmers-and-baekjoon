function solution(arr, k) {
  let answer = [];
  let setArr = new Set(arr) // sort안해도 될듯?
  let arr2 = [...setArr]
  
  answer = arr2.slice(0,k)
  
  console.log(answer)
  if (answer.length < k) {
    for (let i=0; i<k-arr2.length; i++) {
      answer.push(-1)
    }
  }
  
  return answer;
}