// 일단, 제일 큰 S(arr 그 자체)부터 검사하고 계속 정사각형으로 나눠서 검사
  // 언제까지? S가 2*2일때까지. 더 작은 S는 X


function solution(arr) {
  let [zeroCnt, oneCnt] = [0, 0];

  // 시작행, 열, 검색할 길이(+4분할)
  function quadCompression(row,col,n) {
    let flag = true;

    for (let x=row; x<row+n; x++) {
      for (let y=col; y<col+n; y++) {
        if (arr[row][col] !== arr[x][y]) flag = false
        // false면 divide into!
      }
    };

    if (!flag) {
      let half = parseInt(n/2);
      quadCompression(row, col, half)
      quadCompression(row, col+half, half)
      quadCompression(row+half, col, half)
      quadCompression(row+half, col+half, half)
    } else {
      if (arr[row][col] === 1) oneCnt ++
      else zeroCnt ++
    }
  };

  quadCompression(0,0,arr.length)
  return [zeroCnt, oneCnt]
}