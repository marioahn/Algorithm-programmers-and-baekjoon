// a~z: 97~122 / A~Z: 65~90 
  // console.log(solution('A a',25)) // @ ` 아.
  // if (toAscii >= 91) <- 90에서 91로
  // if (toAscii >= 123) <- 122에서 123으로해서 A,a경우 아스키코드 범위 벗어나지 않게해줌!
    // 이렇게 하면 65+25 = 90이니까, -26작업이 없어져서 정상으로 나옴

function solution(s, n) {
  let sArr = s.split('') // 배열(공백도 요소를 가진)
  
  for (let i=0; i<sArr.length; i++) {
    if (sArr[i]===' ') continue // 공백 패스

    let toAscii = sArr[i].charCodeAt()+n
    // (1)대문자인 경우
    if (sArr[i].charCodeAt() <= 90) {
      if (toAscii >= 91) { toAscii -= 26 }
      sArr[i] = String.fromCharCode(toAscii)
    } else { // (2)소문자 경우
      if (toAscii >= 123) { toAscii -= 26 }
      sArr[i] = String.fromCharCode(toAscii)
    }
  }

  let answer = sArr.join('')

  return answer;
}

console.log(solution('A a',25)) // @ ` 아.