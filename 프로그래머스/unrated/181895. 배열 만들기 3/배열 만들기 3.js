// slice?
function solution(arr, indexs) {
  return [...arr.slice(indexs[0][0],indexs[0][1]+1), ... arr.slice(indexs[1][0],indexs[1][1]+1)]
}

