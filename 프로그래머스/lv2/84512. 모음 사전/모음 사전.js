// 1트: DFS로 풀이 -> BUT, 다른 풀이에 비해 오래 걸림

function solution(word) {
  let answer = 0
  let alphabets = ['A','E','I','O','U']

  function dfs(sum) {
    answer += 1

    if (sum === word) { return true };
    if (sum.length === 5) { return false };

    for (let alphabet of alphabets) {
      if (dfs(sum+alphabet) === true) {
        return true
      }
    }
  };

  for (let alphabet of alphabets) {
    if (dfs(alphabet) === true) {
      return answer
    }
  };
};

console.log(solution('AAAAE'))