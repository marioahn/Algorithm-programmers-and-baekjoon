// 1. arr길이가 2의 거듭제곱인지 아닌지 판단
  // 거듭제곱이면 그대로 return
  // 아니라면 그 뒤의 거듭제곱 - arr길이 만큼 0 추가

function solution(arr) {
  // 1 2 4 8 16 32 64 128 256 512 1024(2**10)
  // i가 10인경우, 1024-arr길이가 아니라, 1000-arr
  let cnt = 0
  for (let i=0; i < 11; i++) {
    if (2**i >= arr.length) {
      cnt = i
      break
    }
  }


  let result = [...arr] // 깊은복사 - 원본arr변경x
  for (let j=1; j<=(2**cnt)-arr.length; j++) {
    result.push(0)
  }

  return result
}