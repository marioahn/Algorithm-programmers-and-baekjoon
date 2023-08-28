// return값: 최대의 종.류

function solution(nums) {
  let cnt = 0;
  let setNums = [...new Set(nums)] // 중복제거
  let half = nums.length / 2

  if (setNums.length < half) return setNums.length
  return half

}

console.log(solution([3,1,2,3]))
console.log(solution([3,3,3,2,2,4]))
console.log(solution([3,3,3,2,2,2]))