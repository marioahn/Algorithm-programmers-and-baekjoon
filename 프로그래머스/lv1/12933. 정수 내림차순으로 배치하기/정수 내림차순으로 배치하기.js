function solution(n) {
  let answer = '';

  let arr = String(n).split("")
  arr.sort((a,b) => b-a) // 그냥 arr.sort() 이렇게 쓰는거 절대xx
  
  for (let i=0; i<arr.length; i++) {
    answer += String(arr[i])
  }
  

  return parseInt(answer);
}

//https://celltong.tistory.com/entry/JavaScript-sort-%EB%A9%94%EC%86%8C%EB%93%9C%EB%A1%9C-%EB%B0%B0%EC%97%B4-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0
//이거 읽고 정리 절.대 arr.sort()이런식으로쓰면 안되고, 제대로 정렬할 수 있는 함수를 같이 넣어줘야함

// function solution(n) {
//   const newN = n + "";
//   const newArr = newN
//     .split("")
//     .sort()
//     .reverse()
//     .join("");

//   return +newArr; // <- 와 이거 +는 그럼 또 숫자화시켜주는건가??
// }
// console.log(typeof +("123")) <-- 시바 number네;

// re풀이!!
// function solution(n) {
//   let arr = String(n).split("").sort((a,b) => b-a)
//   let reStr = arr.join("")

//   return Number(reStr)
// }