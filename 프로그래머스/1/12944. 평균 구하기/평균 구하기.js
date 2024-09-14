// function solution(arr) {
//     var answer = 0;
//     answer = arr.reduce((acc,val) => acc+val,0) / arr.length
//     return answer;
// }

function solution(arr) {
    let answer = 0;
    for (let i=0; i<arr.length; i++) {
        answer += arr[i]
    }
    return answer / arr.length
}