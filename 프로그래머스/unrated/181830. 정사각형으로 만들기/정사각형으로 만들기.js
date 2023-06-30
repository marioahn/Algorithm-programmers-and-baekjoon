// arr의 전체길이 = 행, arr의 각 요소의 길이 = 열
//let a = Array(4).fill(0) -> a = [0,0,0,0]

function solution(arr) {
  let [row, column] = [arr.length, arr[0].length]

  // 1. 행>열인 경우 -> 각 요소에 (행-열)만큼 0추가
  if (row > column) {
    for (let i=0; i<arr.length; i++) {
      for (let j=0; j<row-column; j++) { // (행-열)번 시행
        arr[i].push(0)
      }
    }
  }

  // 2. 행<열인 경우 -> arr뒤에 [0]*열을 (열-행)번만큼 추가
  if (row < column) {
    for (let i=0; i<column-row; i++) {
      arr.push(Array(column).fill(0))
    }
  }

  return arr
}