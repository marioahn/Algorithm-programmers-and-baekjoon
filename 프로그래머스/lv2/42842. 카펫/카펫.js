// 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 길다
// 제한사항: yellow는 1 이상 2,000,000 이하인 자연수입니다.


// 전체의 가로길이는? 노랑의 가로길이 + 2
// 전체의 세로 길이? 노랑의 세로길이 + 2
// 노랑 가로길이를 x, 세로 길이를 y라고 하자
// xy = yellow, (x+2)(y+2) = brown
  // 2x+2y+4 = brown
  // y = (brown-2x-4)/2
  // x*y = yellow
  // x(brown-2x-4)/2 = yellow 이 식 풀면, x,y나옴 -> 근의공식!

function solution(brown, yellow) {
  let [x,y] = [0,0]
  let b = (4-brown)/2 //근의 공식에서 'b'담당

  x = (-b+Math.sqrt(Math.pow(b,2)-4*yellow))/2
  y = yellow/x

  console.log(x,y)

  return [Math.max(x,y)+2,Math.min(x,y)+2]

}

console.log(solution(24,24))