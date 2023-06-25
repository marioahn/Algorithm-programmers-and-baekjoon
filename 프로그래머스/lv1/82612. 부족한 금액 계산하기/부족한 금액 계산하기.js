//네비게이터
  // 1. 현재 가지고 있는 잔고: money
  // 2. 반복문을 돌려서 놀이기구를 count번 타게됐을 때 소모되는 비용 합산 = answer
    // 2-1. answer = answer + price*i  -> i=1 ~ count
  // if money > answer: return 0  or return (answer-money)


// ----------

function solution(price, money, count) {
    var answer = 0;
    for (let i = 1; i <= count; i++) {
        answer = answer + price*i;
    }
        
    (money > answer) ? answer = 0 : answer = (answer - money);

    return answer;
}

console.log(solution(3, 20, 4));