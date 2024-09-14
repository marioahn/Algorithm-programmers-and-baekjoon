function solution(n) {
    let answer = 0;
    
    for (let i=0; i<String(n).length; i++) {
        answer += parseInt(String(n)[i])
    };
    
    return answer;
}