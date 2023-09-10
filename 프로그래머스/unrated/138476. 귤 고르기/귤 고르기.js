// 2트
  // 어라.. 근데, 굳이 indexOf로 최댓값과 최댓값의 인덱스 찾을 필요 없잖아
  // 그냥 내림차순sort하고 앞에서 부터 걸러내면 될거같은데?
function solution(k, tangerine) {
  let obj = {};

  for (let i=0; i<tangerine.length; i++) {
    if (!obj[tangerine[i]]) obj[tangerine[i]] = 1
    else obj[tangerine[i]] += 1
  };

  let values = Object.values(obj); // obj에서 value값만 떼와서 모음
  values.sort((a,b) => b-a)
  
  for (let i=0; i<values.length; i++) {
    k -= values[i]
    if (k <= 0) return i+1
  }
}

console.log(solution(6,[1, 3, 2, 5, 4, 5, 2, 3,7]));
console.log(solution(4,[1, 3, 2, 5, 4, 5, 2, 3]));
console.log(solution(2,[1, 1, 1, 1, 2, 2, 2, 3]));