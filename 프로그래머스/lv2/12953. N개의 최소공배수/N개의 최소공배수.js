// 2트: arr을 오름차순으로 sort하고,
// 순차적으로 최소공배수를 각각 구해나간다
  // 즉, 1,2번째 숫자의 최소공배수 -> & 3번째 숫자와의 최소 공배수 ..
// 최대공약수 재귀: const gcd = (a, b) => a % b === 0 ? b : gcd(b, a % b);
// 최소공배수 재귀: const lcm = (a, b) => a * b / gcd(a, b);
function solution(arr) {
  arr.sort((a,b) => a-b) // 먼저 정렬

  const gcd = (a,b) => a%b === 0 ? b : gcd(b,a%b);

  let start = (arr[0]*arr[1]) / gcd(arr[0],arr[1])
  for (let i=2; i<arr.length; i++) {
    // 만약을 위해, 크기 한 번더 정렬
    if (start < arr[i]) { [start, arr[i]] = [arr[i], start] };
    
    let tmpGcd = gcd(arr[i],start)
    start = start*arr[i] / tmpGcd
  }

  return start;
}


console.log(solution([2,6,8,14]))
