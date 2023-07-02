// 네비게이터
  // 1. indexOf 함수 이용해서 kim이 있는지 확인 (or 반복문으로 순회해서 존재하는지 찾기)
  // 2. 있다면 김서방은 (인덱스)에 있다
// ----------
function solution(seoul) {
    var answer = '';
    let a = seoul.indexOf("Kim");
    answer = "김서방은 "+ a + "에 있다"
    return answer;
}
