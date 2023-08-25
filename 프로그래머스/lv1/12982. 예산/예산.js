// 흠.. 그냥 정렬한 다음,budget넘기게 되면 스탑하면 될거같은데

// 1트: 실패
  // 어라 tc몇개 통과 못하는데?
  // console.log(solution([2,2,3,3,4],15)) <- 아 이 경우 undefined가 뜨는구나;;
  // '이하' 경우 제대로 산정 안했음..
// function solution(d, budget) {
//   let answer = 0;
  
//   d.sort((a,b)=>a-b)
//   for (let i=0; i<d.length; i++) {
//     answer += d[i]
//     if (answer > budget) { return i }
//     if (answer === budget) { return i+1 }
//   }
// }

function solution(d, budget) {
  let answer = 0;
  
  d.sort((a,b)=>a-b)
  for (let i=0; i<d.length; i++) {
    answer += d[i]
    if (answer > budget) { return i }
    if (answer === budget) { return i+1 }
    // 아래 코드로, '[2,2,3,3,4],15' <- 이 경우 완벽하게 해결
    if (i===d.length-1) { return d.length} 
    
  }
}