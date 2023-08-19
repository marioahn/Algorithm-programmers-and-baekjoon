// function solution(s) {
//   let arr = [
//     "zero",
//     "one",
//     "two",
//     "three",
//     "four",
//     "five",
//     "six",
//     "seven",
//     "eight",
//     "nine",
//   ];
//   for (let i = 0; i < arr.length; i++) {
//     let spl = s.split(arr[i]);
//     s = spl.join(i);
//   }

//   return parseInt(s);
// }
function solution(s) {
  let bucket = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

  // include, replace활용
  for (let i=0; i<10; i++) {
    if (s.includes(bucket[i])) { // true이면,
      s = s.replaceAll(bucket[i],i) // s.replace만 하면x 새로운걸 반환하는 메서드
    }
  }

  return Number(s)
}