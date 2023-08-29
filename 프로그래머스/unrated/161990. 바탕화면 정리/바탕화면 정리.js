// 한 줄에 '#'이 2개인 경우도 세야 함
function solution(wallpaper) {
  let [row, column] = [wallpaper.length, wallpaper[0].length]
  
  let arrR = []
  for (let i=0; i<row; i++) {
    if (wallpaper[i].indexOf('#')>=0) arrR.push(i)
  }

  let arrC = []
  for (let i=0; i<row; i++) {
    for (let j=0; j<column; j++) {
      if (wallpaper[i][j] === '#') arrC.push(j)
    }
  }

  let rowD = [Math.min(...arrR), Math.max(...arrR) + 1]
  let colD = [Math.min(...arrC), Math.max(...arrC) + 1]
  
  return [rowD[0],colD[0],rowD[1],colD[1]]
}