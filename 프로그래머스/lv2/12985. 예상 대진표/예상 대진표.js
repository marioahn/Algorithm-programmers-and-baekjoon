
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
function solution(n,a,b)
{
    if (a > b) {
        var t = b;
        b = a;
        a = t;
    }
    var times = 1;

    while(a%2!==1 || b-a > 1) {
        if (a % 2 === 1) a++;
        if (b % 2 === 1) b++;
        a = a/2;
        b = b/2;
        times++;
    }


    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    //console.log('Hello Javascript')

    return times;
}