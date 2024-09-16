// function solution(n) {
//     for (let i=2; i<n; i++) {
//         if (n%i==1) return i
//     };
// }

// while: 조건식 안에서도 증감이 가능하네?
function solution(n, x = 1) {    
    while (x++) {
        if (n % x === 1) {
            return x;
        }
    }    
}