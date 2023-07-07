// 풀이2
/* .flat() 을 통해 intervals 평탄화 작업
Why? intervals 의 형태는 항상 [[a1, b1], [a2, b2]] 로 주어지기 때문
intervals 의 idx 를 2개의 set 로 생각하면 방향성이 잡힐 것으로 생각
set_1 : intervals[0] ~ [1]
set_2 : intervals[2] ~ [3]
arr 배열을 나누는 것은 slice 를 통해 진행 */

// let arr2 = arr.flat(n) <- 중첩배열을 n번 벗겨낸다 (중첩배열이 아닌 애는 pass)
  // flat은 원본 배열 변경x
// let arr3 = arr.flat(Infinity) <- 모~든 중첩 배열을 벗겨낸다
function solution(arr, intervals) {
  let flatArr = intervals.flat(Infinity)
  return [...arr.slice(flatArr[0],flatArr[1]+1),...arr.slice(flatArr[2],flatArr[3]+1)]
}