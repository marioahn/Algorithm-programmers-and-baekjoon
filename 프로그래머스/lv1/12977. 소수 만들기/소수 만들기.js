function solution(nums) {

  let sum = []
  for (let i=0; i<nums.length-2; i++) {
    for (let j=i+1; j<nums.length-1; j++) {
      for (let k=j+1; k<nums.length; k++) {
        sum.push(nums[i]+nums[j]+nums[k])
      }
    }
  }

  // 각 요소 순회하면서, 각 요소가 소수인지를 체크
  let cnt = 0
  for (let i=0; i<sum.length; i++) {
    let isPrime = true

    for (let j=3; j<sum[i]; j++) {
      if (sum[i] % j === 0) {
        isPrime = false
        break
      }
    }
    if (isPrime===true) cnt++
  }

  return cnt
}