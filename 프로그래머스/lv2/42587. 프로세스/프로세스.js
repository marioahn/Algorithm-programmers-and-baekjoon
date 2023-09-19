// 우선순위 젤 큰 값이 나오면 그 순서대로 출력한다고 이해했었는데
// 현재 우선순위 젤 큰 값이 출력되면 그 다음 젤 큰 값이 나올 때까지 배열 뒤로 보내야됨.
// 그러다 처음 location 위치에 있던 문서가 출력될 때 그 때 몇번째로 출력됐는지가 답

// obj선언해서, 키는 '몇번째 인덱스'인지, 값은 '우선순위'
  // obj이용해서 Max값 계속 구할거고, obj[location]이 0이되는 순간 return cnt할 것
function solution(priorities, location) {
  let obj = {}
  for (let i=0; i<priorities.length; i++) {
    obj[i] = priorities[i]
  }

  let arr = []
  for (let i=0; i<priorities.length; i++) {
    arr.push([i,priorities[i]])
  }

  let cnt = 0
  while (arr) {
    let Max = Math.max(...Object.values(obj))
    if (arr[0][1] < Max) {
      let tmp = arr[0]
      arr.shift()
      arr.push(tmp)
    } 
    else {
      obj[arr[0][0]] = 0
      arr.shift()
      cnt ++
    };

    if (obj[location] === 0 ) return cnt;
  };
  return arr
}

console.log(solution([2, 1, 3, 2],2));
console.log(solution([1, 1, 9, 1, 1, 1],0));