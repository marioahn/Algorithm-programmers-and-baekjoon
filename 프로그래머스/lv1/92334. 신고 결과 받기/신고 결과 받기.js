// 제한 사항
  //정확성 테스트 : 10초
  // 1 ≤ report의 길이 ≤ 200,000
// "ryan"이 "con"을 4번 신고했으나, 주어진 조건에 따라 한 유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리


// 먼저, report set화시켜서 중복 제거?? 하면 바로..될거같은데..?
function solution(id_list, report, k) {
  let setReport = [...new Set(report)]
  let wasReported = {}
  let whoReported = {}

  for (let i=0; i<setReport.length; i++) {
    let [reportP, reportedP] = setReport[i].split(" ")
    // wasReported: 신고당한 사람(key)은 몇번 신고당했는가(value)?
    if (wasReported[reportedP] === undefined) wasReported[reportedP] = 1
    else wasReported[reportedP] += 1

    // whoReported: 신고한 사람(key)은 각 누구누구를 신고했는가(value)?
    if (whoReported[reportP] === undefined) whoReported[reportP] = reportedP
    else whoReported[reportP] += `,${reportedP}`
  }

  let answer = []
  for (let id of id_list) {
    let cnt = 0

    // 신고 안했거나, 신고했지만 k번이상이 아닌 경우
    if (whoReported[id] === undefined) {
      answer.push(0)
      continue
    }

    // 신고한 사람이 k번이상 신고당한 상태면 cnt++
    let checks = whoReported[id].split(',')
    for (let check of checks) {
      if (wasReported[check]>=k) cnt ++
    }
    answer.push(cnt)
  };

  return answer
}

console.log(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
console.log(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))
