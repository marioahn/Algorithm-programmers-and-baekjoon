// cards1 또는 cards2의 0번째 index를 goal의 0번째 index와 비교해서 같다면 제거 
// goal의 length가 0이 될 경우 Yes를 return
// cards1 또는 cards2의 0번째 index를 goal의 0번째 index와 비교해서 둘 다 같지 않다면 No를 return

function solution(cards1, cards2, goal) {
  
  while (goal.length > 0) {
    if (cards1[0] === goal[0]) {
      cards1.shift()
      goal.shift()
    } else if (cards2[0] === goal[0]) {
      cards2.shift()
      goal.shift()
    } else return "No"
  }
  return "Yes"
}