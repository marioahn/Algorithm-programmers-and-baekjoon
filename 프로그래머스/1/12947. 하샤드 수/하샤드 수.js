function solution(x) {

  divNum = 0
  for (let i=0; i<(x+"").length; i++) {
    divNum += (+(x+"")[i])
  }

  return x % divNum === 0 ? true : false
  
}
