function solution(n) {
    var answer = [];
    for (let i=String(n).length-1; i>=0; i--) {
        answer.push(parseInt(String(n)[i]))
    }
    return answer;
}