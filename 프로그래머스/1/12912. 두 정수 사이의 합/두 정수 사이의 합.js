function solution(a, b) {
  var answer = 0;

  if (a <= b) {
    for (let i = a; i <= b; i++) {
      answer = answer + i;
    }
  } else {  // a = 5, b = 3
    for (let i = b; i <= a; i++) {  
      answer = answer + i;
    }
  }
  return answer;
}
