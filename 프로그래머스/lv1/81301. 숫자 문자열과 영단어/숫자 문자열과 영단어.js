function solution(s) {
  let arr = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  for (let i = 0; i < arr.length; i++) {
    let spl = s.split(arr[i]);
    s = spl.join(i);
  }

  return parseInt(s);
}