// 제한사항: 5 ≤ sequence의 길이 ≤ 1,000,000
// 고려1: 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾는다
// 고려2: 길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾는다

// 누적합 + 투포인터 사용해서 풀이 (나 생각해보니. 누적합 거의 안 써봤구나.. 중요중요! - til쓰자)
// 비내림차순 !== 오름차순이다. 문제 설명 이상하다고 욕하지않긔..^^..
  // 비내림차순은 오름차순이되, 중복값이 있을 수 있음을 전제한다 - [1,1,1,2,3,5]

function solution(sequence, k) {
  let answer = [];
  let accSum = [0] // 초기값ㅇㅇ - 이거 안 넣으면 피똥쌈

  // step1: 누적합 구하기
  for (let ele of sequence) {
    accSum.push(accSum.at(-1)+ele)
  };

  // step2: 투포인터로, answer구하기
  let [start, end] = [0,1];
  let Min = Infinity;
  while (start < end) {
    // step2-1
    if (accSum[end] - accSum[start] < k) {
      if (end<accSum.length-1) end ++ // 한계 초월ㄴㄴ
      else if (end===accSum.length-1) start++ // 종료조건
    }
    // step2-2
    else if (accSum[end] - accSum[start] > k) {
      start ++
    }
    // step2-3
    else { // = k
      if (end-1-start < Min) {
        answer = [start,end-1]
        Min = end-1-start
      }
      start ++ // 이제 다른거 찾아가(진행시켜)
    }
  };

  // answer중에서 최종값 골라내기 - 제일 작으면서도, 앞에 있는 것

  return answer
}

console.log(solution([1, 2, 3, 4, 5],7))
console.log(solution([1, 1, 1, 2, 3, 4, 5],5))
console.log(solution([2, 2, 2, 2, 2],6))