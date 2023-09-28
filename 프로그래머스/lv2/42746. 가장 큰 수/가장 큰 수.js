// 먼저, number의 첫자리수(number[0])가 가장 큰것들을 먼저 뽑아서 더해야함
  // 만약 같다면? ex -> 30 vs 34 -> 그 다음 숫자가 큰것이 필요함
  // 아 근데. 34 vs 3은 34가 우선, 3 vs 30은 3이 우선이어야 함;;
  // stack 써야할 것 같은데? ㄴㄴ 일단 정렬알고리즘 세부사항 짜서 해보자 strA,strB로

function solution(numbers) {
    if (Math.max(...numbers) === 0) return "0"
  numbers.sort(function(a,b) {
    let strA = a.toString();
    let strB = b.toString();

    if (strA+strB < strB+strA) {
      return -1
    } else if (strA+strB < strB+strA) {
      return 1
    } else {
      return 0
    }
  })

  numbers = numbers.map((ele) => String(ele))
  let answer = ''

  for (let i=numbers.length-1; i>=0; i--) {
    answer += numbers[i]
  }

  return answer;
}

console.log(solution([6, 10, 2]))
console.log(solution([3, 30, 34, 5, 9]))