// 음.. 그냥 합이 더 큰 큐에서 작은 큐로만 옮기면 될..것 같..은데..?
    // 맞나? 그렇게 단순할 것 같진 않은데
  // 또한, 같아질 수 없는 경우는 어떻게 체크하지?
    // 예제3에서는 위 논리대로 하면, (2,6) -> (3,5) -> (8,0)이 되고 끝남
    // 흠.. 한쪽 큐가 0이 되면 끝나도록?

// 1트 -> 실패(25/30) - 시간초과
  // 음.. 아래에서 queue1,2에 각 shift하는게 개에바인듯.. - shift자체가 O(N)
  // +음.. 일단 sum1,2합이 홀수인거는 -1 바로 return 추가할까
    // 시간간은 줄어들지언정, tc통과갯수는 여전함(25/30)
// function solution(queue1, queue2) {
    // let [sum1, sum2] = [0, 0]
    

    // for (let ele of queue1) {
    //   sum1 += ele
    // }
    // for (let ele of queue2) {
    //   sum2 += ele
    // }
    
//     if ((sum1+sum2)%2) return -1 // 홀수면 컷

//     let cnt = 0
//     while (sum1 !== sum2) {
//       if (sum1>sum2) {
//         sum1 -= queue1[0]
//         sum2 += queue1[0]
//         if (sum1 === 0) return -1
//         queue2.push(queue1.shift())
//         cnt ++ 
//       } else if (sum1<sum2) {
//         sum2 -= queue2[0]
//         sum1 += queue2[0]
//         if (sum2 === 0) return -1
//         queue1.push(queue2.shift())
//         cnt ++
//       }
//     }

//     return cnt
// }


// 2트: js에서 queue를 직접 구현하느냐(js는 queue구조 지원x) or shift말고 다른 방법
  // 참조: https://school.programmers.co.kr/questions/41370
function solution(queue1, queue2) {
  let cnt = 0
  let maxTry = queue1.length * 3

  // reduce로 queue1,2차이 한 방에 정리
    // acc, cur뿐만 아니라, idx이용해서 queue2[idx] ㄷㄷ;
  let difference = queue1.reduce((acc, cur, idx) => acc + cur - queue2[idx], 0) / 2;
  let [idx1, idx2] = [0, 0]

  while (difference !== 0 && cnt < maxTry) {
    if (difference > 0) {
      let queueNumber = queue1[idx1]
      idx1 ++, difference -= queueNumber, queue2.push(queueNumber)
    } else {
      let queueNumber = queue2[idx2]
      idx2 ++, difference += queueNumber, queue1.push(queueNumber)
    }

    cnt ++
  }
  
  return difference !== 0 ? -1 : cnt; // 0이 되지 않는다면 실패
}

console.log(solution([3, 2, 7, 2],[4, 6, 5, 1]))