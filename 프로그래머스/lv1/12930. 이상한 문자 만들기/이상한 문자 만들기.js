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