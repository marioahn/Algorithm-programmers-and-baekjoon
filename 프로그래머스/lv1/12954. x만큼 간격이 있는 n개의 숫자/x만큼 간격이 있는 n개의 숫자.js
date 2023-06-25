// 반복문을 사용하여 x의 i를 n 번 만큼 곱해줍니다.
// 곱해줄 때 마다 answer에 값을 저장하여 n 번이 끝나면 그 배열을 현출합니다.


function solution(x, n) {
    var answer = [];
    
    for (let i=1; i<n+1; i++) {
      answer.push(x*i)
    }

    return answer;
}

console.log(solution(-4, 2));

// test

// let a = [1]
// a.push[2]
// console.log(a)