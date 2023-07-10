// 문제 제한사항 -> 회원들의 비밀번호는 같을 수 있지만 아이디는 같을 수 없다!!!
// 순서: 먼.저 아이디부터 검사 -> 그 후 비번 검사
// 1. 아디x -> fail
// 1-2. 아디o -> 2. 비번o -> login
              //2-2.비번x -> wrong pw

function solution(user, db) {
  
  let status = "fail"

  for (let i=0; i<db.length; i++) {
    // step1: 아디일치? -> 비번 검색 (login or wrong pw 둘 중 한개)
    if (user[0]===db[i][0]) {
      if (user[1]===db[i][1]) { // 비번까지 같다면
        return "login"
      } 
      else return "wrong pw" // 아디는 맞지만, 비번은 틀리다 - 아디는 한개밖에 없으니, 바로 return해도 ㄱㅊ
    }
  }
  // step2: 아디일치x -> fail뿐
  return status
}