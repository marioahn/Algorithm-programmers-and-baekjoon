// function solution(numbers) {
//   let answer = [];

//   for (let i = 0; i < numbers.length - 1; i++) {
//     for (let j = i + 1; j < numbers.length; j++) {
//       tmpSum = numbers[i] + numbers[j];
//       if (answer.indexOf(tmpSum) === -1) {
//         answer.push(tmpSum);
//       }
//     }
//   }
//   answer.sort((a, b) => a - b);

//   return answer;
// }
function solution(numbers) {
  let answer = new Set() // add로 +

  // 반복문
  for (let i=0; i<numbers.length-1; i++) {
    for (let j=i+1; j<numbers.length; j++) {
      let tmpSum = numbers[i] + numbers[j]
      answer.add(tmpSum)
    }
  }


  return [...answer].sort((a,b)=>a-b)
}