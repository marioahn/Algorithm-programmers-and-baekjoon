function solution(before, after) {
  let answer = (before.split("").sort().join("")===after.split("").sort().join(""))
  return (answer) ? 1 : 0
}