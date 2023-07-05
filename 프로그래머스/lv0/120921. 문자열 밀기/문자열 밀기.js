function solution(A, B) {
  if (A===B) return 0

  let cnt = 0
  let tmp = A // 초기값 담아주고
  for (let i=0; i<A.length-1; i++) {
    let moveA = tmp.slice(-1)+tmp.slice(0,A.length-1)
    tmp = moveA // 재할당
    cnt ++
    if (moveA === B) return cnt // break
  }

  if (cnt === A.length-1) return -1
}

// console.log(solution("hello","ohell"))