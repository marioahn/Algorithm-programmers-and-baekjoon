// 이것도 시간복잡도 따져야겠네.. 잘 따져보자 이쿠요잇!

// 1트: 이중포문 (for문안에, slice2번 -> 2n**2)
  // 허허허.. -> (2/20). 심지어 통과된 2개도 3000ms,7000ms..
// function solution(topping) {
//   let cnt = 0

//   for (let i=1; i<topping.length; i++) {
//     let left = new Set(topping.slice(0,i))
//     let right = new Set(topping.slice(i))
//     if (left.size === right.size) {
//       cnt ++
//     }
//   }

//   return cnt
// }

// 2트 set과 스택을 이용해보자
  // (2/20) -> 통과된 2개: 1300, 3110ms로 절반 줄어들긴 했음..
  // 여전히 어림도 없다 - 이유가 무엇인가? 여전히 시간복잡도는 O(N**2)이기 때문이다
  // 배열을 Set으로 변환하는 과정은 일반적으로 선형 시간 복잡도(O(n))를 가진다. 이것은 배열의 각 요소를 Set에 하나씩 추가하는 작업을 수행하기 때문이다
  // Set은 중복된 요소를 허용하지 않으므로 배열의 중복된 요소가 Set으로 복사될 때 중복이 제거된다. 이 과정도 배열의 모든 요소를 한 번 씩 훑어야 하므로 선형 시간이 걸린다..

// function solution(topping) {
//   let cnt = 0;
//   let stack = new Set(); // set으로 하면, 중복값은 추가해도 안 들어감

//   while (topping.length>0) {
//     stack.add(topping[0]);
//     topping.shift();
//     if (stack.size === new Set(topping).size) {
//       cnt ++
//     };
//   };

//   return cnt;
// }

// 3트 - 잠깐만. 생각해보니, 왜 자꾸 좌/우를 항상 비교하면서 해?
  // 좌를 먼저 쭉 구하고, 우측에서 한개씩 뺏는다고 생각하면 되지 않을까?
  // 이 과정을 모-두 해쉬로 처리하면 될것 같다
	// 성공!!!!!
function solution(topping) {
  let left = {}
  let right = {}
  let answer = 0

  for (let i=0; i<topping.length; i++) {
    if (!left[topping[i]]) left[topping[i]] = 1
    else left[topping[i]] += 1
  }

  let leftCnt = Object.keys(left).length
  let rightCnt = 0

  for (let i=topping.length-1; i>=0; i--) {
    // 동생 객체 만들기
    if (!right[topping[i]]) {
      right[topping[i]] = 1
      rightCnt += 1 // 없던 종류가 새로 들어오는 경우므로 cnt!
    }
    else right[topping[i]] += 1

    // 형 객체 조정하고, leftCnt도 조정
    left[topping[i]] -= 1
    if (left[topping[i]] === 0) leftCnt -= 1

    if (leftCnt === rightCnt) answer ++
  }

  return answer;
}

// 4트 - 레퍼런스
https://school.programmers.co.kr/questions/49346