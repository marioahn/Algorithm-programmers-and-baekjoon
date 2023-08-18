function solution(x) {
  let haNum = 0
  for (let i=0; i<String(x).length; i++) {
    haNum += Number(String(x)[i])
  }

  return !(x % haNum) ? true : false
}