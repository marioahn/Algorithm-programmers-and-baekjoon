// console.log(solution('a234'))
// console.log(solution('1234'))
// test
// let a = parseInt('2a34')
// let b = parseInt('1342')
// console.log(typeof a, a) // number NaN
// console.log(typeof b, b) // number 2

// // mdn parseInt

// console.log(NaN === parseInt('a'))
// console.log(parseInt('a'))
// console.log(NaN === NaN) // false ?????
// console.log(false === false) // true
// console.log((typeof 'a') !== number) -> 이렇게 되는게 아니고,
// console.log((typeof '2') === 'string') string이 아니라 'string'...
// console.log((typeof 'a') === (typeof 'c')) -> 이게 되는거지


function solution(s) {
  var answer = true;
  
  for (let i=0; i<s.length; i++) {
    if (Number(s[i]) >= 0) { // '0123'도 true이므로 0이상
      answer = true;
    } else {
      answer = false;
      break
    }
  }

  if (s.length !== 4 && s.length !==6) {
    answer = false
  }

  return answer;
}

// console.log(solution())

// '1e22' -> parseInt들어가면 .. ㅜㅜ(지수형식)
// parseInt('문자열', 진법)
  // 원래 이 형태 -> 따라서 문자열 이상하게 넣으면 진법이 다르게 나올수도있음