// bfs & visited
function solution(maps) {
  let result =[];
  let [H, W] = [maps.length, maps[0].length]; // height, width
  let visited = Array.from({ length: H }, () => Array(W).fill(0));
  let move = [[0,1], [0,-1], [1,0], [-1,0]]; // 우 좌 하 상

  // bfs함수
  function bfs(x,y) {
    let sum = 0; // 식량합
    let dq = [[x,y]]; // deque, 초기값 넣기
    sum += parseInt(maps[x][y]);
    visited[x][y] = 1; // 재방문 금지

    while (dq.length) {
      let [x, y] = dq.shift();
      for (let i=0; i<4; i++) { // 현 좌표에서 4방향 이동
        nowx = x + move[i][0], nowy = y + move[i][1]

        if (nowx>=0 && nowx<H && nowy>=0 && nowy<W) { // 1.범위 확인(맵 밖x)
          if (!visited[nowx][nowy] && maps[nowx][nowy] !== 'X') { // 2.갈수 있는가?
            visited[nowx][nowy] = 1; // 방문check
            sum += parseInt(maps[nowx][nowy]);
            dq.push([nowx,nowy]);
          }
        }
      };
    };
    // 총 식량 더하기
    result.push(sum);
  }

  for (let i=0; i<H; i++) {
    for (let j=0; j<W; j++) {
      if (!visited[i][j] && maps[i][j] !== 'X') { // bfs조건
        bfs(i,j)
      }
    }
  }

  return result.length === 0 ? [-1] : result.sort((a,b) => a-b)
}

console.log(solution(["X591X","X1X5X","X231X", "1XXX1"]))
console.log(solution(["XXX","XXX","XXX"]))