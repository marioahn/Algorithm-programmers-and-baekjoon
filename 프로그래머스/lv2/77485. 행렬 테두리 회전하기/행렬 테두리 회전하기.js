function solution(rows, columns, queries) {
  let answer = [];
  let arr = Array.from({ length: rows+1 }, () => Array(columns+1).fill(0));
  // 0. 빈 arr에 -> 1~rows*columns 숫자 채우기
  for (let i=1; i<=rows; i++) {
    for (let j=1; j<=columns; j++) {
      // 위에서 rows,columns+1 각 안해주면 여기하고 아래 회전부분에서도 i-1,j-1고려해야함
      arr[i][j] = (i-1)*columns + j 
    }
  };

  // 1. 회전 - stack이용
  for (let query of queries) {
    // let [x1,y1, x2,y2] = [query[0],query[1], query[2],query[3]]
    let [x1,y1, x2,y2] = query; // 이렇게만 해도 됨
    let stack = [];
    // 1-1)위테두리
    for (let i=y1; i<y2; i++) stack.push(arr[x1][i]);
    // 1-2)오른테두리
    for (let i=x1; i<x2; i++) stack.push(arr[i][y2]);
    // 1-3)아래테두리
    for (let i=y2; i>y1; i--) stack.push(arr[x2][i]);
    // 1-4)왼테두리
    for (let i=x2; i>x1; i--) stack.push(arr[i][y1]);

    // 2)최솟값 찾고, stack 조절
    answer.push(Math.min(...stack));
    stack.unshift(stack.pop()); // 맨 뒤를 맨 앞으로, 나머지도 오른쪽으로 한칸씩 옮기기

    // 3)회전한 값 다시 arr에 배치하기
    for (let i=y1; i<y2; i++) arr[x1][i] = stack.shift()
    for (let i=x1; i<x2; i++) arr[i][y2] = stack.shift()
    for (let i=y2; i>y1; i--) arr[x2][i] = stack.shift()
    for (let i=x2; i>x1; i--) arr[i][y1] = stack.shift()
  };

  return answer
}

console.log(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))

