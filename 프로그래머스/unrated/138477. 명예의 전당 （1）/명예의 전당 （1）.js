function solution(k, score) {
  let answer = []; 
  let minArr = []

  for (let i=0; i<score.length; i++) {
    minArr.push(score[i])
    minArr.sort((a,b)=>b-a)
    if (k<minArr.length) {minArr.pop()}
    answer.push(Math.min(...minArr)) 
  }

  return answer;
}