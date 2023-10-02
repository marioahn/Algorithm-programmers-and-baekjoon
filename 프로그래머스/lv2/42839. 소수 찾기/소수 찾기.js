// 핵심은 중.복.순.열을 완전탐색으로 어떻게 구현할 것인가?
// 아 진짜 알고리즘 손 너무 오래놨더니 이런 기본적인 거 구현하는것도 힘드네;;
// 앞으론 아무리 힘들어도 절대 놓지말고 꾸준히 하자..
function isPirme(num) {
  if (num === 0 || num === 1) return false;
  if (num === 2) return true;
  if (num % 2 === 0) return false
  for (let i=3; i<=Math.sqrt(num); i+=2) {
    if (num%i === 0) {
      return false
    }
  };
  return true // .. 이거 안 붙여서 계속 0나옴..
};

function solution(numbers) {
  let numSet = new Set();
  let nLength = numbers.length; // 이 습관 들이자ㅇㅇ.

  function dfs(level,endLevel,visited,sum) {
    if (level === endLevel) {
      if (isPirme(Number(sum))) {
        numSet.add(Number(sum))
      }
      return // 필수;; 안하면 endLevel은 1인데, level이 2이상 올라가는 경우 생김
    };

    for (let i=0; i<nLength; i++) {
      if (!visited[i]) {
        visited[i] = 1
        let tmpSum = sum // 백트랙킹 용도
        sum += numbers[i]
        dfs(level+1,endLevel,visited,sum)
        visited[i] = 0 // 백트랙킹
        sum = tmpSum // 얘도 돌려줘야지
      }
    };
  };

  for (let i=1; i<=nLength; i++) { // 1~nLength 자릿수의 순열 구하기
    let visited = Array.from({length:nLength}, ()=>0)
    dfs(0,i,visited,'')
  };

  return numSet.size
};

console.log(solution("011"))