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
