// "첫"글자부터 순차적으로 발음해나가야 함..
// 조건을 추가하고, while문으로 해야할 듯..
  // 조건: 첫글자가 babyWords의 첫글자랑 같으면 그제서야 replace
// splice사용

function solution(babbling) {

  let cnt = 0
  for (let i=0; i<babbling.length; i++) {
    let babyWords = ["aya", "ye", "woo", "ma"]
    let tmp = babbling[i]

    for (let j=0; j<4; j++) {
      for (let k=0; k<4; k++) {
        if (tmp[0] === babyWords[k][0]) {
          tmp = tmp.replace(babyWords[k],"")
        }
      }
    }

    if (!tmp) cnt ++
  }

  return cnt
}