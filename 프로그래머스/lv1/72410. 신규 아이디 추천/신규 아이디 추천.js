function solution(new_id) {
  
  // step1: 1+2
  new_id = new_id.toLowerCase()
  ban = '~!@#$%^&*()=+[{]}:?,<>/</>' // 처음 -,_,.는 제거
  ban = ban.split('')
  let new_id1 = ''
  for (let i=0; i<new_id.length; i++) {
    if (ban.indexOf(new_id[i])<0) { new_id1 += new_id[i] }
  }

  // step2. 3+4
  let new_id2 = ''
  for (let i=0; i<new_id1.length; i++) {
    if (new_id1[i] === '.' && new_id1[i+1] === '.') {
      continue
    } else { new_id2 += new_id1[i]}
  }
  // 아래처럼 하면 처음과 마지막에 '.'둘다 있으면 둘다 차례대로 제거됨? yes.
  if (new_id2[0]==='.') { new_id2 = new_id2.replace('.','') } // 처음 '.'제거
  if (new_id2[new_id2.length-1]==='.') { new_id2 = new_id2.slice(0,-1) } // 이렇게 해도 재할당되냐? ㅇㅇ

  // step3. 5+6
  if (new_id2.length===0) { new_id2 += 'a'}
  if (new_id2.length>=16) { new_id2 = new_id2.slice(0,15) } // new_id4 새로 선언안하고, 걍 바로 때려박아도 ㄱㅊ?
  if (new_id2[14]==='.') { new_id2 = new_id2.slice(0,14)}
  if (new_id2.length===2) { new_id2 += new_id2[1] }
  if (new_id2.length===1) { new_id2 += new_id2+new_id2 }

  return new_id2
}