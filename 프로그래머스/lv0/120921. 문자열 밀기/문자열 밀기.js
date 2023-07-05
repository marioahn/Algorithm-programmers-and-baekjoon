function solution(A, B) {
  // step1
  if (A===B) return 0

  // step2
  let cnt = 0
  let tmp = A // 초기값 담아주고
  for (let i=0; i<A.length-1; i++) {
    let moveA = tmp.slice(-1)+tmp.slice(0,A.length-1)
    tmp = moveA // 재할당
    cnt ++
    if (moveA === B) return cnt // break
  }

  // step3 -> step2에서 return이 안 나온다 => A는 B가 될 수 없다
  return -1
}
