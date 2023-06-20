function solution(n) {
  let answer = '';

  let arr = String(n).split("")
  arr.sort((a,b) => b-a) // 그냥 arr.sort() 이렇게 쓰는거 절대xx
  
  for (let i=0; i<arr.length; i++) {
    answer += String(arr[i])
  }
  

  return parseInt(answer);
}