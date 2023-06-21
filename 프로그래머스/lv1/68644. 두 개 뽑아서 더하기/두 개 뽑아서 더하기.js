function solution(numbers) {
  let answer = [];

  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      tmpSum = numbers[i] + numbers[j];
      if (answer.indexOf(tmpSum) === -1) {
        answer.push(tmpSum);
      }
    }
  }
  answer.sort((a, b) => a - b);

  return answer;
}