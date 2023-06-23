function solution(n, m) {
    // 최대공약수를 구하는 함수
    function gcd(a, b) {
        while (b !== 0) { // b가 0이 아닐 때 까지 돌아라 이하는 swap 한 것!! 
            let c;
            c = b;
            b = a % b;
            a = c;
        }
        return a;
    }

    // 최소공배수를 구하는 함수
    function lcm(a, b) {
        return (a * b) / gcd(a, b);
    }

    // 최대공약수와 최소공배수를 배열로 반환
    return [gcd(n, m), lcm(n, m)];
}