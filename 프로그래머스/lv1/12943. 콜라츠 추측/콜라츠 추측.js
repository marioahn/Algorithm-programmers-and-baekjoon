function solution(num) {

  if (num === 1) { return 0 }

  let n = 0
  while (num !== 1) {
    if (num % 2 === 0) { num = num/2 }
    else { num = num*3+1 }
    n ++ 
  }

  return n < 500 ? n : -1
}