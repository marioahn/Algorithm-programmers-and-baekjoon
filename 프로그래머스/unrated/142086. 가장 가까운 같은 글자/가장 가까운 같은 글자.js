/* 객체를 이용하면, 아래 두가지 정보를 한꺼번에 가져올 수 있다
- (1)해당하는 문자가 처음 등장하는지 아닌지,
- (2)그리고 만약 등장했다면, 가장 근처(가까운)idx는 몇번인지
*/

function solution(s) {
  let bucket = {}
  let answer = []
  
  for (let i =0; i<s.length; i++) { // 각 글자 순회

    // step1: 만약 처음 보는 단어면(=undefined)
    if (bucket[s[i]] === undefined) { 
      bucket[s[i]] = i // 객체에 키는 s[i], 밸류는 i(=인덱스 뜻함)로 담아주고
      answer.push(-1) // 처음 등장 => -1추가
    } 
    // step2: 이미 있던 단어라면, 가장 가까운 idx찾기
    else { 
      // bucket[s[i]]에는 가까운(과거의) idx정보가 담겨있다=> 현재idx-가까운idx
      answer.push(i-bucket[s[i]]) 
      bucket[s[i]] = i // 가장 최신(=현재)idx로 업.데이트
    }
  }
  return answer
}


/* (참고)

- 객체를 이용하면 2가지 정보를 한꺼번에 저장할 수 있다(키,밸류)
- "빈" 객체를 하나 선언하고, 키에는 '문자', 밸류에는 '최근의 인덱스'값을 저장
  - s = 'banana' <- 반복문으로 순회하면서 각 글자들을 왼쪽부터 읽음
  - obj = {'b':0} 의 뜻은
    -> 'b'문자의 가장 최근의 idx는 0번 인덱스
  

EX)
let obj = {}

obj[1] = 1 // <- 키는 1, 밸류는 1
obj['b'] = 2 // <- 키는 'b', 밸류는 2
obj['b'] = 3 // <- 'b'키는 이미 있으므로 키가 추가되진 않고, 대신 밸류가 3으로 변경

console.log(obj)// -> { 1:1, 'b': 3}
console.log(obj[2]) // <- 위에 2키값을 추가한 적이 없으므로 undefined 나옴

*/