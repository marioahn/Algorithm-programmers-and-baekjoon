function solution(answers) {
  // step1: 1~3번수포자들의 답 리스트 쭉 만들기
  let arr1 = [1,2,3,4,5]
  let arr2 = [1,2,3,2,4,2,5,2] // 얘 초기값 2 어케 처리하지 -> 걍 bigArr2에 초기값 넣으면 됨 
  let arr3 = [3,3,1,1,2,2,4,4,5,5]

  let bigArr1 = [] // 1번 수포자 리스트 만들기
  for (let i=0; i<=parseInt(answers.length/5); i++) {
    bigArr1.push(...arr1)
  }
  let bigArr2 = [2]
  for (let i=0; i<=parseInt(answers.length/8); i++) {
    bigArr2.push(...arr2)
  }
  let bigArr3 = []
  for (let i=0; i<=parseInt(answers.length/10); i++) {
    bigArr3.push(...arr3)
  }

  // step2: 정답 맞는지 각각 채점해서 count에 작성
  count = [0,0,0] // 0번인덱스: 1번이 맞춘 횟수, 2번인덱스: 3번이 맞춘 횟수
  for (let k=0; k<answers.length; k++) {
    if (answers[k] === bigArr1[k]) { count[0] ++ }
    if (answers[k] === bigArr2[k]) { count[1] ++ }
    if (answers[k] === bigArr3[k]) { count[2] ++ }
  }
  
  // 아 이제 정답횟수가 같은 애들도 처리해야하네..
  let answer = []
  for (let i = 0; i<3; i++) {
    if (count[i] === Math.max(...count)) { answer.push(i+1) }
  }

  return answer;
}