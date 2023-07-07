function solution(n) { // n = 123
    let answer = 0;
    let tmp = String(n) // tmp = '123'

    for (let i=0; i<tmp.length; i++) {
        answer += Number(tmp[i])
    }

    return answer;
}

// 다른 코드 
    //쉬운방법 -> let b = 123 + "" // ㅅㅂ.. 자동 형변환경우.. (=String(n)과 동일)
// function solution(n){
//     return (n+"").split("").reduce((acc, curr) => acc + parseInt(curr), 0)
// }