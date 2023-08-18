function solution(price, money, count) {
    var answer = 0;
    for (let i = 1; i <= count; i++) {
        answer = answer + price*i;
    }
        
    (money > answer) ? answer = 0 : answer = (answer - money);

    return answer;
}

console.log(solution(3, 20, 4));