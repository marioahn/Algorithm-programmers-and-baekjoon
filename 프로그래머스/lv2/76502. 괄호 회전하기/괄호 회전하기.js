// 3트 - 성공
  function solution(s) {
    if (s.length % 2 === 1) return 0
  
    let cnt = 0
    for (let i=0; i<s.length-1; i++) {
      let tmp = s
      // tmp값이 하나도 안 걸러질때까지, while문으로 반복
      while (1) {
        let tmp2 = tmp
        tmp = tmp.replaceAll('()','')
        tmp = tmp.replaceAll('{}','')
        tmp = tmp.replaceAll('[]','')
        if (tmp2 === tmp) break // replace로 걸러지는게 없다면? 그만해
      }
  
      // 비로소, 모든 (),{},[]가 없어짐 - ('({})'같은포함형도 마찬가지)
      if (tmp.length === 0) cnt ++
      s = s.slice(1) + s[0]
    }
    
    return cnt
  }

console.log(solution("[](){}"));
console.log(solution("}]()[{"));
console.log(solution("[)(]"));
console.log(solution("}}}"));