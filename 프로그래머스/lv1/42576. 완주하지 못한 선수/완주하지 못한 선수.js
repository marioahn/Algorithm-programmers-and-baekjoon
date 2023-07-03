function solution(participant, completion) {
	participant.sort();
	completion.sort();

  for (let i = 0; i < participant.length; i++) {
    if (participant[i] !== completion[i]) {
      return participant[i]; // break쓸 필요도 없이, return하면 바로 함수 끝
    }
  }
}