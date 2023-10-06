// 레퍼런스 참조 - https://daesiker.tistory.com/43 
// 아;; 너무 삼각형 모양에 매달렸네;; - 0으로 채워진 graph모습봐바
  // 저렇게만 하고 채우면 되잖아
  // 와. 와. 이 풀이. 와;;;;;;;;;;;;;;;;;;;;;;
function solution(n) {
  let graph = [];
  let result = [];

  let [y,x] = [-1,0]; //초기값을 위해서 -1로 변수 지정
  let number = 1;

  // 요소가 모두 0인 배열 생성
  for (let i=1; i<n+1; i++) {
    let line = Array(i).fill(0)
    graph.push(line)
  }
  console.log(graph) // 삼각모형에 몰입되지 마라. 후;;

  for (let i=0; i<n; i++) { // 돌리는건 n번이지 -> n=4면 빙빙돌리기 4번임
    for (let j=i; j<n; j++) { // 4->3->2->1
      // 1. 밑으로
      if (i%3 === 0) {
        y += 1
      }
      // 2. 오른쪽으로
      else if (i%3 === 1) {
        x += 1
      }
      // 3. 위로
      else {
        y -= 1
        x -= 1
      }
      // final: graph채우기
      graph[y][x] = number
      number += 1
    }
  }
  // 이중 배열 풀어서 result에 1차원 배열로 담기
  for (let i=0; i<n; i++) {
    result = result.concat(graph[i])
  }

  return result
}

/*
n=6일때 graph의 모습
[
  [ 0 ],
  [ 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0 ],
  [ 0, 0, 0, 0, 0, 0 ]
]
*/