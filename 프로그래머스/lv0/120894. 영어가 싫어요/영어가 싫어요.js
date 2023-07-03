// 2트
  // zero~nine: 글자 길이는 3~5사이
  // while문 돌리고 - 조건(numbers.length>0)
  // numbers[0~3] or [0~4] or [0~5]가 bucket.indexOf했을 때 >=0이면 그 인덱스 빈배열에 계속 추가
  // numbers는 [3~끝] or [4~끝] or [5~끝]으로 재할당해서 계속 줄여가기
function solution(numbers) {
  let bucket = ["zero","one","two","three","four","five","six","seven","eight","nine"]
  let result = ""

  while (numbers.length > 2) {
    for (let i=0; i<10; i++) {
      if (numbers.slice(0,3).indexOf(bucket[i]) >= 0) {
        result += i // 문자를 숫자로 바꿔서 result에 추가
        numbers = numbers.slice(3) // 방금 확인한 문자 빼고, 그 이후를 재할당
        break // 했으면, 다시 0부터 ㄱㄱ
      }

      if (numbers.slice(0,4).indexOf(bucket[i]) >= 0) {
        result += i // 문자를 숫자로 바꿔서 result에 추가
        numbers = numbers.slice(4) // 방금 확인한 문자 빼고, 그 이후를 재할당
        break
      }

      if (numbers.slice(0,5).indexOf(bucket[i]) >= 0) {
        result += i // 문자를 숫자로 바꿔서 result에 추가
        numbers = numbers.slice(5) // 방금 확인한 문자 빼고, 그 이후를 재할당
        break
      }
    }
  }

  return Number(result)
}