// 네비게이터
  // 0. 문자열 s를 upper(전부 대문자화 or 소문자화) -> 's = s.toUpperCase()'
  // 1. 문자열 s를 반복문을 통해 순회해서
    // 1-2. p의 개수와 y의 개수를 각각 센다(변수 pSum,nSum)
  // 2. pSum,nSum이 같으면 true, 아니면 false
    // 0되는 경우 자동으로 해결



// ----------

function solution(s){
    var answer = true;
    s = s.toUpperCase()
    let ysum = 0;
    let psum = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === "Y"){
            ysum++
        } else if(s[i] === "P"){
            psum++
        }
    }
    (ysum === psum) ? answer = true : answer = false;
    return answer;
}

console.log(solution("Pyy"))