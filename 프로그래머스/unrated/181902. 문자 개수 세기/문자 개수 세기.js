// 26개짜리 두개 만들고, 대문자면 위 배열, 소문자면 아래 배열 채우기
// 아스키 코드 사용: [A~Z, 65~90] / [a~z, 97~122]

function solution(str) {
  let [upperArr, lowerArr] = [[],[]]
  for (let i=0; i<26; i++) {
    upperArr.push(0)
    lowerArr.push(0)
  }

  for (let i=0; i<str.length; i++) {
    if (str[i].charCodeAt() >= 65 && str[i].charCodeAt() <= 90) { // 대문자면
      upperArr[str[i].charCodeAt()-65] ++
    }
    if (str[i].charCodeAt() >= 97 && str[i].charCodeAt() <= 122) { // 대문자면
      lowerArr[str[i].charCodeAt()-97] ++
    }
  }

  return [...upperArr,...lowerArr] // js의합치기 (=python의 upperArr+lowerArr)
}

console.log(solution('AA'))