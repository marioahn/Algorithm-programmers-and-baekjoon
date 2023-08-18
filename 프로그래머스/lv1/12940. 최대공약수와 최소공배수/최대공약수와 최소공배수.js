function solution(n, m) {
   let ans = [n, m] // [5, 12]

   let sorted_ans = ans.sort((a, b) => { b - a }) // [12, 5]


   for (let i = 0; i < 100; i++) {
      if (!sorted_ans[i] % sorted_ans[i + 1] !== 0) {
         continue
      } else {
         ans.push(sorted_ans[i] % sorted_ans[i + 1])
      }
   }
   console.log(ans)

   let GCD = ans.at(-2) // 21
   let LCM = (m * n) / GCD // 52479

   return [GCD, LCM]
}