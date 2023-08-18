function solution(t, p) {
    let arr = [];
    let t_arr = [...t.split('')];

    for (let i = 0; i <= t.length - p.length; i++) {
        arr.push(t_arr.slice(i, p.length + i).join(''))
    };

    return arr.filter(x => x <= (+p)).length;  

}