// 핵심 로직: 각각의 종류의 개수+1들을 모두 곱하고, 마지막에 -1
  // 상의3개, 모자2개인 경우는 4*3-1이다. why?
  // 상의가 3개이지만, 상의에서 나올 수 있는 선택지는 4개이다. 바로, '상의선택x'경우도 +!
  // 단, 모-든 옷종류가 선택x를 택할 수는 없으므로 이 경우를 마지막에 -1해서 빼주는 것

function solution(clothes) {
  let obj = {}
  for (let cloth of clothes) {
    if (!obj[cloth[1]]) obj[cloth[1]] = 1
    else obj[cloth[1]] += 1
  };

  let values = Object.values(obj);
  let answer = 1;

  for (let value of values) {
    answer *= (value+1)
  };

  return answer-1
};


console.log(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]));
console.log(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]));
