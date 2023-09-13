// 1,2,3,1을 계속 없앰
// [1,2,3,1] === [1,2,3,1] -> false이므로 문자화시켜서 비교해줘야함

// 1트 -> 당연히 실패.. -> 1 <= ingredient <= 1,000,000이기에 slice/splice + 이중포문은 xx
// function solution(ingredient) {
//   let [cnt, canMake] = [0, '1231']
  
//   while (1) {
//     let flag = 'end'
//     for (let i=0; i<ingredient.length-3; i++) {
//       if (ingredient.slice(i,i+4).join('') === canMake) {
//         ingredient.splice(i,4) // 4는 index가 아니라, 몇개를 지울지에 대한 것
//         cnt ++
//         flag = 'notEnd'
//         break
//       }
//     }
//     if (flag === 'end') return cnt // while문 빠져나오기
//   }
// }

// 2트: 여전히 시간초과 -> 통과안되는건 8개에서 3개로 줄었으나, 통과되는 것도 시간 겁나 걸미
  // replace도 오래걸리네
  // 이유: 문자열의 replace을 사용하려면 앞에서 부터 순차적으로 진행하여야 한다. replace('1231', '', 치환횟수)를 이용하여 치환횟수를 1로 두어 순차적으로 코드를 작성하여 해결할 수 있으나 시간복잡도를 고려하면 O((문자열의 길이X (교체하려는 문자열의 길이+교체되는 문자열의 길이) * while문의 반복 횟수) 가 소요되고 입력이 크므로 시간초과가 발생
// function solution(ingredient) {
//   let cnt = 0;
//   let strIngredient = ingredient.join('')
//   while (1) {
//     let tmp = strIngredient // tmp: 211231231
//     strIngredient = strIngredient.replace('1231','') // strIngredient: 21231

//     if (tmp === strIngredient) return cnt
//     cnt ++
//   }
// }

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


console.log(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
console.log(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))