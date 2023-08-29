function solution(phone_book) {
  let hashPhone = {}

  for (let ele of phone_book) {
    hashPhone[ele] = 1
  }

  for (let i=0; i<phone_book.length; i++) {
    let tmp = ''
    for (let j=0; j<phone_book[i].length; j++) {
      tmp += phone_book[i][j]
      if (hashPhone[tmp] && tmp !== phone_book[i]) return false
    }
  }
  return true
}

console.log(solution(["119", "97674223", "1195524421"]	))
console.log(solution(["123","456","789"]))
console.log(solution(["12","123","1235","567","88"]))