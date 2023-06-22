function solution(strings, n) {
  let answer = [];
  //1
  for (let i = 0; i < strings.length; i++) {
    strings[i] = strings[i][n] + strings[i]
  }
  //2
  strings.sort() // 근데, 이건 정렬할 요소들의 길이가 각 1이어서 가능한 거임
  //3
  for (let j = 0; j < strings.length; j++) {
    strings[j] = strings[j].replace(strings[j][0],"")
    answer.push(strings[j])
  }
  return answer;
}