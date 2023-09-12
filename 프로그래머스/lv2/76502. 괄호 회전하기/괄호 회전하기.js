// 4트: 아 근데, 3트는 너무 시간 오래걸리고 비효율적이야
  // stack으로 다시 풀어보자
function solution(s) {
  if (s.length % 2 === 1) return 0;

  let pair = { '}': '{', ')': '(', ']':'['};
  let cnt = 0;

  // step1: s.length-1번 왼쪽으로 회전
  for (let i=0; i<s.length-1; i++) {
    let stack = [];
    // step2: stack이용해서, 옳은 괄호형인지 체크
    for (let j=0; j<s.length; j++) {
      if (s[j] === '(' || s[j] === '[' || s[j] === '{') {
        stack.push(s[j])
      } 
      else {
        let recent = stack.pop()
        // 맞지 않으면, 해당 로테는 실패 -> cnt-1하고 break
        if (recent !== pair[s[j]]) {
          cnt -= 1
          break
        }
      };
      // break안 걸리고, 끝까지 왔다면? 성공
    };
    
    cnt ++ 
    s = s.slice(1) + s[0];
  };

  return cnt;
};

console.log(solution("[](){}"));
console.log(solution("}]()[{"));
console.log(solution("[)(]"));
console.log(solution("}}}"));