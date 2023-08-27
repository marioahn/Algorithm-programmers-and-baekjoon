// 풀이3: stack이용 - 와 이 문제 풀면서 stack이 진짜 얼마나 유용한지 깨달았음
  // for문 한.개.로 해결한 셈 - 풀이1,2와 비교
  // 풀이1,2에서는 전-부 ingredient를 대상으로 slice,splice,replace를 진행했지만,
  // 여기서는 상대적으로 짧을 수 밖에 없는 stack배열을 이용했기에 통과!
function solution(ingredient) {
  let stack = []
  let cnt = 0

  for (i of ingredient) { // 배열이니 for-of good
    stack.push(i)

    if (stack.slice(-4).join('') === '1231') {
      stack.splice(-4)
      cnt ++
    }
  }

  return cnt;
}