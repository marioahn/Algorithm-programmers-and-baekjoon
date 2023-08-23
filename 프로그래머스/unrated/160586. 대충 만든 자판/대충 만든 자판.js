//최종목표:targets(입력하려는 문자열)을 위해 클릭해야 하는 수를 순차적으로 돌아가며 answer배열에 저장해주기 
//targets를 for문 돌려줌
//targets[i]를 변수(1)에 저장해줌
//변수(1)에 들어간 값을 for문을 돌리면서 변수(1)의 j번째 해당하는 문자를 입력하기 위한 최소클릭수를 구함
//최솟값을 구하기 위해 min변수에 101로 초기화 시킴(키맵의 원소길이 100이니까 )
//이를 위해 keymap을 for문 돌리면서 변수(1)의 j번째 해당하는 문자의 인덱스의 최솟값을 순차적으로 구해줌
//min이 101이면 keymap에 변수(1)의 j번째 해당하는 문자가 없단거니까 answer배열에 -1 넣어주고 차례패스함
//min이 101이 아닐경우 최솟값 존재(문자가 키맵에존재)니까 answer i번째에 min+1(인덱스+1만큼 눌러야되니까)더함

function solution(keymap, targets) {
  // let answer = []; <- 이 상태로 하면 아래 answer[i] += ~~ 할때 빈 것에 숫자를 더하니까 NaN이 나오지 ㅅㅂ
  let answer = new Array(targets.length).fill(0)
  
  for (let i=0; i<targets.length; i++) {
    let tmp = targets[i]
    //tmp = ABCD
    for (let j=0; j<tmp.length; j++) {
      let minN = 101
      //tmp[j]=A
      //keymap = ["ABACD", "BCEFD"]
      for (let k=0; k<keymap.length; k++) {
        if (keymap[k].indexOf(tmp[j]) === -1) continue
        minN = Math.min(minN,keymap[k].indexOf(tmp[j]))
      }
      if (minN === 101) {
        answer[i] = -1
        break
      }

      else {answer[i] += (minN+1)}
    }
  }
  
  return answer;
}

console.log(solution(["ABACD", "BCEFD"], ["ABCD","AABB"]))
console.log(solution(["AA"], ["B"]))
console.log(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))