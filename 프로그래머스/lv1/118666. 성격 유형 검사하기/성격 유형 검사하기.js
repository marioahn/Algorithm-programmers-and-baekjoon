// 단, 하나의 지표에서 각 성격 유형 점수가 같으면, 
  // 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단
// 1~3 -> survey[i]의 첫 요소, 5~7 -> survey[i]의 두번째 요소, 4는 continue

// 반복문 돌면서 1~4지표의 각 점수 합산
// 최종적으로 1지표부터 성격유형 하나씩 찍어주기   [[R,T], [C,F], [J,M], [A,N]]

function solution(survey, choices) {
  let answer = '';
  let obj = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

  for (let i=0; i<survey.length; i++) {
    if (choices[i] >= 5) obj[survey[i][1]] += (choices[i]-4)
    else if (choices[i] <= 3) obj[survey[i][0]] += (4-choices[i])
    else continue
  }

  if (obj['R'] >= obj['T']) answer += 'R' // 같은 경우 사전순까지 걍 러프하게 해줌
  else answer += 'T'

  if (obj['C'] >= obj['F']) answer += 'C'
  else answer += 'F'

  if (obj['J'] >= obj['M']) answer += 'J'
  else answer += 'M'

  if (obj['A'] >= obj['N']) answer += 'A'
  else answer += 'N'
  
  return answer;
}


console.log(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])) // TCMA
console.log(solution(["TR", "RT", "TR"],[7, 1, 3])) // RCJA