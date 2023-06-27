// 네비게이터
  // 0.빈배열(answer) 생성
  // 1.반복문으로 배열(arr) 순회 -> 배열의 각 요소가 divisor로 나눠떨어지면 push -> 반복문끝
  // 2. answer정렬
  // 3. answer크기가 0이면 -> -1 push

// ---------

function solution(arr, divisor) {
    var answer = [];
    
    // arr = [7, 10, 9, 5] ,나누기5
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] % divisor === 0){
                answer.push(arr[i])
        } 
    }
    
    if(answer.length === 0) {
        answer.push(-1)
    }
    
    answer.sort((a,b) => a-b);
    
    return answer;
}

console.log(solution([7,10,9,5],5));


//answer.sort -> 이렇게 하면 안됨: 딱 앞자리만 보고 비교하게됨
      // 1 12 2 25 3 36 << 이거때문 -> 따라서 a-b, 혹은 b-a로 앞뒤자리 비교하면서 정렬
// answer.sort(function(a,b){
    //     return;
    // })
