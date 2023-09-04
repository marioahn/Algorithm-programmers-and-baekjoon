// score를 sort(내림차순으로) -> score에서 계속 m개씩 제거하고, 마지막 'm개째 요소'*m*1를 answer에 더해가기
// 언제까지? -> m개를 채울 수 없을때까지

// function solution (k, m, score) {
//   let answer = 0
//   const sortedScore = score.sort((a,b) => b - a)

//   while(sortedScore.length >= m) {
//     answer += (sortedScore.slice(0,m)[m-1]) * m
//     sortedScore.splice(0,m)  
//   }
//   return answer
// } //-> 실패
function solution (k, m, score) {
  let answer = 0
  const sortedScore = score.sort((a,b) => b - a)
  const boxArr = []

  for(let i = 0 ; i < score.length ; i += m) {
    if( sortedScore.slice(i, i+m).length >= m ) {
      boxArr.push(sortedScore.slice(i, i+m))
    }
  }
  boxArr.map(v => {
    answer += v[m-1] * m
  })
  return answer
}