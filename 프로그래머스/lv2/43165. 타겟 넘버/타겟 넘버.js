// DFS이용
function solution(numbers, target) {
  let cnt = 0
  let signs = ['+', '-']

  function dfs(level, sum, target) {
    if (level === numbers.length) {
      if (sum === target) cnt ++
      return
    }

    for (let sign of signs) {
      dfs(level+1, sum+Number(sign+numbers[level]),target)
    }
  }

  dfs(0,0,target)

  return cnt
}

console.log(solution([1, 1, 1, 1, 1],3))