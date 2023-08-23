//answer를 최솟값을 초기화 , 최솟값 n-lost.length
//obj(객체)에 체육복의 여분 정보를 저장 키가 학생의 번호, 벨류가 여분1개만
//lost를 돌아가면서 reserve에 값이 있을경우 우선시해서 여분의 갯수를 - 해줌, 그리고 answer를 ++해줌
//다시 lost를 돌아가면서 번호가 -1일경우, 번호가 +1일경우 obj에 있는지 체크하고 있으면 answer++해줌
//그리고 obj의 벨류는 -해줌
//


// lost = [6,4,9]
// 가져온애가 = 5,7 
// sort를 해주면 4는 5를 가져가고 6은 7을 가져감
// 근데 안해주면 6이 5를 체가버림, 4는 원래는 5를 가져갈수 있는데 뺏김, 그래서 최종적으로 6만 얻음

function solution(n, lost, reserve) {
  let answer = n-lost.length // 최소
  let obj = {}
  lost.sort((a,b)=>a-b)
  
  // 1
  for (let i=0; i<reserve.length; i++) {
    obj[reserve[i]] = 1
  }

  // 2
  for (let j=0; j<lost.length; j++) {
    if (obj[lost[j]] === 1) {
      obj[lost[j]] = 0
      answer ++
    }
  }
  
  // 3
  for (let k=0; k<lost.length; k++) {
    if(obj[lost[k]] === 0) continue
    else if (obj[lost[k]-1]) { 
      obj[lost[k]-1] = 0
      answer ++
    }
    else if (obj[lost[k]+1]) { 
      obj[lost[k]+1] = 0
      answer ++
    }
  }
  
  return answer;
}


console.log(solution(5,[2, 4],[1, 3, 5])) // 5
console.log(solution(5,[2, 4],[3])) // 4
console.log(solution(3,[3],[1])) // 2