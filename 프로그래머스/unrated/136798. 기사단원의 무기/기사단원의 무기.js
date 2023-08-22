// 1. 반복문 돌려서, 각 기사의 약수의 개수 확인해서 빈 배열에 추가
// 2. limit초과하면 power로 바꾸고, 배열 합 return

function solution (number, limit, power) {
  const arr = Array.from({length: number}, (_,index) => (index+1))

  // 약수의 개수 구하는 함수
  function count(num) {
    let result = 0
    for(let i = 1 ; i <= Math.sqrt(num); i++) {
      if(num / i === i) {
        result += 1
      } else if( num % i === 0 ) {
        result += 2
      }
    }
    return result
  }


  for(let i = 0 ; i < arr.length ; i ++) {
    if(count(arr[i]) > limit) {
      arr[i] = power
    } else {
      arr[i] = count(arr[i])
    }
  }
  
  return arr.reduce((a,b) => a+b)
}