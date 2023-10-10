// bfs로 가능한(=이어진) 경로 모두 탐색
// 레퍼런스 참조 - https://velog.io/@sean2337/Programmers-%EC%A0%84%EB%A0%A5%EB%A7%9D%EC%9D%84-%EB%91%98%EB%A1%9C-%EB%82%98%EB%88%84%EA%B8%B0-JavaScript
function solution(n, wires) {
  let answer = Infinity
  
  // 0. 트리 뼈대 만들고, 채우기 - n+1 -> 1번인덱스에는 1번이 들어가도록 하기 위해
  let tree = Array.from({length: n+1}, () => [])
  for (let wire of wires) {
    let [from, to] = wire
    tree[from].push(to);
    tree[to].push(from);
  }

  // 1. bfs함수 만들기 - 인자: start, 제외할 번호
  function bfs(start, exceptNum) {
    let cnt = 0;
    let visit = []; // n만큼 0 안채워도 됨 ㅇㅇ.
    let queue = [start];
    visit[start] = true;

    while (queue.length) {
      let idx = queue.pop()
      // 반복문 말고, forEach써보자 - 안 익숙해서 일부러 안썼는데 연습ㄱㄱ
      tree[idx].forEach((ele) => {
        if (ele !== exceptNum && visit[ele] !== true) {
          visit[ele] = true;
          queue.push(ele);
        }
      })
      cnt ++
    }

    return cnt
  }

  wires.forEach(ele => {
    let[a,b] = ele
    // 아래 부분이 제일 이해x였음 - 왜 bfs(a,b)-bfs(b,a)인가?
    // 문제 홈페이지에서 입출력예시1 그림 보면 바로 이해가 됨
    // bfs(start,except)에서 start는 root노드임 -> 여기서 쭉 뻗어나가는 거고,
    // except는 root에서 해당 번호쪽으로는 안 가겠다는 것
    // 따라서, bfs(a,b) - bfs(b,a)는 a와b의 연결이 끊어진 상태에서 각각의 전력망 개수의 차이를 구한것과 같다
    answer = Math.min(answer, Math.abs(bfs(a,b)-bfs(b,a))) 
  })

  return answer
}

console.log(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
