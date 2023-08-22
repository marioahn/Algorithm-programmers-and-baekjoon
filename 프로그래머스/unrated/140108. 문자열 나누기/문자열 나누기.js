function solution(s) {
  var answer = 0;

  while (s.length > 0) {
      let x = s[0];
      let cntX = 0;
      let cntO = 0;

      for (let i of s) {
          if (i === x) {
              cntX++;
          } else {
              cntO++;
          } ``

          if (cntX === cntO) {
              answer++;
              s = s.slice(cntX + cntO);
              break;
          }
      }

      if (cntX !== cntO) {
          answer++;
          s = '';
      }
  }

  return answer;
}