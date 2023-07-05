// 하나 이.상의 공백문자로 구분 (공백 두번도 있을 수 있는건가?) -> 아 그게아니라, 여러 단어있단뜻
  // split으로 각 단어가 요소로 들어간 배열 새로 만들고,
  // 거기서 각 요소들의 인덱스를 또 들어가서(이중포문) 대/소문자화 하는거 밖에 생각이 안나..

function solution(s) {
  var answer = '';
  let sArr = s.split(" ")

  for (let i=0; i<sArr.length; i++) {
    for (let j=0; j<sArr[i].length; j++) {
      if (j%2 === 0) { answer += sArr[i][j].toUpperCase() }
      else { answer += sArr[i][j].toLowerCase() }
    }
    if (i !== sArr.length-1) { answer += " "  } // 단어 구분, 마지막은 추가하면 안되지
  }

  return answer;
}

console.log(solution("try hello world"))
