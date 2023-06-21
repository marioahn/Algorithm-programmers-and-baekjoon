// 등수 매기는 것도 일인데, 공동 등수 매기는게 골치아프네..
function solution(score) {
  var answer = [];
  let average = []

  for (let k=0; k<score.length; k++) {
    average.push((score[k][0]+score[k][1])/2)
  }

  let rankArr = []

  for (let i=0; i<average.length; i++) {
    let rank = average.length
    for (let j=0; j<average.length; j++) {
      if (i===j) continue // 자기자신의 점수와 비교할 필요없음
      if (average[i] >= average[j]) { rank -= 1}
      // else if (average[i] < average[j]) { rank += 1}
    }
    rankArr.push(rank)
  }
  return rankArr
}