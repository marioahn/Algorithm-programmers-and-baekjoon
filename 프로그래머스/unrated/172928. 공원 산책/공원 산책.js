// 2트: 
function solution(park, routes) {

  let [height, width] = [park.length, park[0].length]

  function canMove(sx,sy,direct,amount) {
    ways = [] // 초기화

    for (let i=1; i<=amount; i++) {
      if (direct === 'S') { sx += 1 }
      if (direct === 'N') { sx -= 1 }
      if (direct === 'W') { sy -= 1 }
      if (direct === 'E') { sy += 1 }
      ways.push([sx,sy]) // [0,1]
    }
  
    for (let way of ways) {
      if (way[0] >= height || way[0] < 0 ) return false;
      if (way[1] >= width || way[1] < 0 ) return false;
      if (park[way[0]][way[1]] === 'X') return false;
    }
    return true;
  }

  // step1: 시작 좌표 찾기
  let now = [0,0]
  for (let i=0; i<height; i++) {
    if (park[i].indexOf('S')>=0) now[0] = i
    for (let j=0; j<width; j++) {
      if (park[i][j] === 'S') now[1] = j
    }
  }

  // step2: routes 순회
  let ways = []
  for (let route of routes) {
    let [dir, num] = route.split(" ")
    if (canMove(now[0],now[1],dir,num)) {
      now[0] = ways[ways.length-1][0]
      now[1] = ways[ways.length-1][1]
    }
  }

  return now
}

console.log(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
console.log(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))
console.log(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))