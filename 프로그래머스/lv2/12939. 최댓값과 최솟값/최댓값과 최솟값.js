function solution(s) {
  let arr = s.split(' ').map(e => parseInt(e))
  let [max, min] = [Math.max(...arr), Math.min(...arr)]

  return `${min} ${max}`
}

console.log(solution("1 2 3 4"))
console.log(solution("-1 -2 -3 -4"))
console.log(solution("-1 -1"))