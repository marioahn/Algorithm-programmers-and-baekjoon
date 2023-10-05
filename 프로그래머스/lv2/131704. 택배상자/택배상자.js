// 2트 -> stack도 subContainer이런식으로 해서 보조컨테이너라는 것을 드러내주자
function solution(order) {
  let subContainer = []
  let [cnt, orderN] = [0,0] // order배열의 작은 수는 1임. 0이 아니라

  // (main)컨테이너 상자 꺼내기
  for (let i=1; i<=order.length; i++) {
    // step1: 메인 확인
    if (order[orderN] !== i) {
      subContainer.push(i)
    } else {
      orderN ++
      cnt ++
    }

    // step2: stack(보조)에 상자가 남아있고, 맨 뒤에 넣은 상자와 번호가 같으면 cnt
    while (subContainer.length && subContainer.at(-1) === order[orderN]) {
      subContainer.pop();
      orderN ++
      cnt ++
    }
  }

  return cnt
}