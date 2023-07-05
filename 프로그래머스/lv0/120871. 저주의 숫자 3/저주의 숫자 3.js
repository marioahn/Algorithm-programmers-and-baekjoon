// 첫 코드 -> n=40인경우 76이 나와야하는데, 내 코드는 71이 나옴. 흠;; 어디서 잘못된거지
  // 아. '3'이 들어있는 경우 -> while돌려야 할거 같은데? 
  // 그리고 로직 잘못 이해했음 -> '33'이면 (.length-1)해서 +2 하는게 아니라, 그냥 계속 넘겨야 함
  // '3'자가 그 수에 없을 때 까지
function solution(n) {
  let num = 0;

  for (let i=1; i<=n; i++) {
    num ++ // logic0: 기본으로 1 추가

    // logic1
    if (num % 3 === 0) {
      num ++
      while (`${num}`.indexOf('3') >= 0) {
        num ++
      }
    }
    
    // logic2
    while (`${num}`.indexOf('3') >= 0) {
      num ++
      if (num % 3 === 0) {
        num ++
      }
    }
  }
  return num;
}
