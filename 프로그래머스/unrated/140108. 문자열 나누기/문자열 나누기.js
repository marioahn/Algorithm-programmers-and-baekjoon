/* 문제이해(me)
- x와 x가 아닌 다른 글자들이 나온 횟수를 각각 세나간다
- 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리
- s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복 -> 남은 부분이 없다면 종료
- 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, answer +1 하고 종료!
- 3번째 예시 이해: 'aaabbacccccabba'
  - 첫 글자 x = a -> aaa cnt1은 3개네 -> cnt2이제 세보자 -> bb.. a? 엇?
    -> cnt1은 4개가 됨 -> 즉, 2개를 더 세봐야함(a등장하면 또 더 세고)
    -> (aaa)bbacc 까지! -> aaabbacc 떼어냄~

- 페어 내비 내용
  - key point: for ~ in / for ~ of 의 차이점을 이해하고 2개의 문법 중 하나를 사용해서 코드를 작성한다.
  1)https://developerntraveler.tistory.com/122
  2)https://velog.io/@onea/JS-for-...of%EC%99%80-for-...in%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90
  -> for in은 키밸류로 이루어진 객체 순회할 때 유용하겠네
    -> 심지어 키,밸류 둘다 뽑아낼 수 있음 ㅇㅇㅇwow
    -> 정리하자
*/

// -> 그럼 이 경우에서는 for of 쓰는게 좋겠네!

function solution(str) {
  let answer = 0;
  let [x, rest, tmpIdx, okIdx] = [0, 0, 0, 0];

  for (let s of str) {
    if (s === str[okIdx]) x ++
    if (s !== str[okIdx]) rest ++
    tmpIdx ++ // 첨엔 이거 설정안하고, 위에 str[0]로 써놨음.. 분리되면 x가 바뀔수도 있잖아.
    if (x === rest) {
      answer ++
      [x, rest, okIdx] = [0, 0, tmpIdx] // 초기화 작업 꼭 필요
    }
    // if (s === str[str.length-1] && x === 1 && rest === 0) answer ++ // (1)마지막 1개만 남은 경우
      // 또한, s가 마지막 문자여야 한다는 조건이 있어야 하는 이유는 맨 처음 for문 시작할 때 1,0 상태니까.
      // 아 근데 이렇게 하면 안되지.. str마지막 문자가 중복일 수도 있잖아.. 아래는 정확x
      // + str.length로 해야지..
    // if (tmpIdx === str.length && x === 1 && rest === 0) answer ++ // (2)이것도 tc 몇개 실패
      // 아. str = 'bbaaaaa' 인경우 -> 위 코드대로라면 결과는 1이 나와버린다
      // bbaa, aaa 총 2개 나와야하잖아
    // if (tmpIdx === str.length && x !== 0 && rest === 0) answer ++ // (3)아 ㅅㅂ 이것도 실패네
      // 아. str = 'baaab' 인 경우 -> x는 2, rest는 1이잖아 시밬;;
    if (tmpIdx === str.length && x !== rest) answer ++
  }

  return answer;
}

console.log(solution("baaab"))