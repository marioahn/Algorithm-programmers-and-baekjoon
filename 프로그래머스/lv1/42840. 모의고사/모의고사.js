// function solution(answers) {
//   let pattern1 = [1, 2, 3, 4, 5];
//   let pattern2 = [2, 1, 2, 3, 2, 4, 2, 5];
//   let pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
//   let answer = [];
//   let result = [0, 0, 0];

//   for (let i = 0; i < answers.length; i++) {
//     if (answers[i] === pattern1[i % 5]) {
//       result[0] += 1;
//     }
//     if (answers[i] === pattern2[i % 8]) {
//       result[1] += 1;
//     }
//     if (answers[i] === pattern3[i % 10]) {
//       result[2] += 1;
//     }
//   }
//   let win = Math.max(...result);

//   for (let i = 0; i < result.length; i++) {
//     if (result[i] === win) {
//       answer.push(i + 1);
//     }
//   }
//   return answer;
// }
// --------------------------
// 1번, 2번, 3번 수포자가 찍는 방식의 배열을 선언한다.
// 1번, 2번, 3번 수포자의 정답 수를 저장하는 변수를 선언한다.
// answers의 배열을 돌면서 1번, 2번, 3번 수포자가 찍는 방식의 index의 값과 answers의 index 값이 일치하면 count를 1씩 더해준다.
// 가장 큰 값을 가진 수포자를 출력한다.


function solution (answers) {
  let result = []

  let [patternOne, cnt1] = [[1,2,3,4,5], 0] // 길이 5
  let [patternTwo, cnt2] = [[2,1,2,3,2,4,2,5], 0] // 길이 8
  let [patternThree, cnt3] = [[3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 0] // 길이 10

  for (let i=0; i<answers.length; i++) {
    if (answers[i] === patternOne[i % 5]) cnt1 ++
    if (answers[i] === patternTwo[i % 8]) cnt2 ++
    if (answers[i] === patternThree[i % 10]) cnt3 ++
  }
  let maxAnswer = Math.max(cnt1,cnt2,cnt3)
  let tmp = [cnt1,cnt2,cnt3]
    
  for (let i=1; i<=3; i++) {
    if (maxAnswer === tmp[i-1]) result.push(i)
  }

  return result
}