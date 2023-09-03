// function solution(s) {
//     return s.split(" ").map(v => v.charAt(0).toUpperCase() + v.substring(1).toLowerCase()).join(" ");
// }
function solution(s) {
    return s.split(" ").map(e => e.charAt(0).toUpperCase() + e.substring(1).toLowerCase()).join(" ")
}