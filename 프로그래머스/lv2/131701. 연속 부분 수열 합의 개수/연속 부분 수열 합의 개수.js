function solution(elements) {
  let arr = [...elements] // 초기값 넣기 (길이가 1인)

  // i => 길이가 i인 부분연속 수열의 합 구하기
  for (let i=2; i<=elements.length; i++) {
    let elements2 = elements.concat(elements.slice(0,i-1))

    for (let j=0; j<elements2.length-i+1; j++) {
      let sum = 0
      for (let k=0; k<i; k++) {
        sum += elements2[j+k]
      }
      arr.push(sum)
      
    }
  }

  // return 
  return [...new Set(arr)].length // 중복제거한 배열의 길이
}

console.log(solution([7,9,1,1,4]))