// 1. 길이가 n이고, 1로 채워진 배열을 만든다. section에 있는 번호들의 숫자는 0을 push.
// 2. 0이 있는 index부터 m개만큼 1로 만든다. 근데, 룰러가 벽을 넘어가면 안됨.
// 3. 배열에 0이 없어질때까지 반복한다.

// 수정
// 1. 길이가 n이고, 1로 채워진 배열을 만든다. section에 있는 번호들의 숫자는 0을 push.
// 2. 위에서 만든 배열을 돌면서 0을 만나면 / 칠하는 횟수 +1 / index를 m만큼 건너뜀
// 3. arrN이 0이 아니면 index를 1만 추가

function solution (n, m, section){
  let arrN = []
  let sectionSet = new Set(section);
  for (let i=1; i<=n; i++) {
    if (sectionSet.has(i) > 0) arrN.push(0)
    else arrN.push(1)
  }
  // for (let i=1; i<=n; i++) {
  //   if (section.includes(i) > 0) arrN.push(0)
  //   else arrN.push(1)
  // } -> includes는 O(n)
  // [1, 0, 0, 1, 1, 0, 1, 1] 
  // [0, 1, 0, 1, 1]
  // [0, 0, 0, 0]
  let cnt = 0
  for (let i = 0; i < n; i++) {
    if (arrN[i] === 0) {
      cnt ++
      i += m - 1
    }
  }
  return cnt
}