// 자르기 전 부분을 left, 자르는 부분을 mid, 자르는부분 직후부터 마지막까지를 right
// answer = left+mid+right

function solution(my_string, overwrite_string, s) {

  // str.substr(a,b) -> a인덱스부터 b-1인덱스를 자르겟다
  let left = my_string.substr(0,s)
  let mid = overwrite_string
  let right = my_string.substr(s+overwrite_string.length)

  return left+mid+right
}