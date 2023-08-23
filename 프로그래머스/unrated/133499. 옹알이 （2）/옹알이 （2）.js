// 발음을 할 수 있는 단어 배열에 먼저 저장
//babbling을 for문 돌리면서 차례대로 발음할 수 있는지를 count변수에 체크
//조건 !! 반복해서 발음 불가 !!! 

function solution(babbling) {
  let babyWords = ["aya", "ye", "woo", "ma"]
  
  let cnt = 0
  for (let i=0; i<babbling.length; i++) {
    let tmpChk = babbling[i]
    //tmpchk = yeye 
    for (let j=0; j<4; j++) {
      // update - 4가지 발음에 따라 체크
      if (tmpChk.includes(babyWords[j].repeat(2))) break // 연속이면 나오기
      tmpChk = tmpChk.split(babyWords[j]).join(' ') // 'yeaya' = ['','aya'].join('')='aya' <- 순서상관없이 가능
    }
    tmpChk = tmpChk.split(' ').join('')
    if (tmpChk.length === 0) cnt ++
  }

  return cnt
}
// ['a','b','a','d'].join('%')= 'a%b%a%d'
// .join('')='abad'
// .join(' ') = 'a b a d'

//'yayae' -> split(babyWords[j]) 후 그냥 빈문자열로 join하면 안되는 이유 
// 'y', 'e' - > 'y e'

// 'yeaya' -> 'ye',''


console.log(solution(["aya", "yee", "u", "maa"]));//1
console.log(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))//2

