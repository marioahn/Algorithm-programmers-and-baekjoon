function solution(answers) {
  let pattern1 = [1, 2, 3, 4, 5];
  let pattern2 = [2, 1, 2, 3, 2, 4, 2, 5];
  let pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  var answer = [];
  let result = [0, 0, 0];

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === pattern1[i % 5]) {
      result[0] += 1;
    }
    if (answers[i] === pattern2[i % 8]) {
      result[1] += 1;
    }
    if (answers[i] === pattern3[i % 10]) {
      result[2] += 1;
    }
  }
  let win = Math.max(...result);

  for (let i = 0; i < result.length; i++) {
    if (result[i] === win) {
      answer.push(i + 1);
    }
  }
  return answer;
}