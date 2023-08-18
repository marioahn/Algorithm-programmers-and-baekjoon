function solution(a, b) {
  let [min, max] = [0, 0]
  if (a<=b) {[min, max] = [a, b]}
  else {[min, max] = [b, a]}

  let answer = 0
  for (let i = min; i <=max; i++) {
    answer += i
  }
  return answer
}