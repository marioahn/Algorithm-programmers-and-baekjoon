// 서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다.
// 흠.. 이건 중복제거 하는게 나을것 같은데?
// 어차피 이건 어떻게 해도 못 해 ㅇㅇ. -> 이중배열도 set으로 되나?
  // 근데 또 1~3개 메서드 써야 함. 어차피 중복은 바로 다음에서 통과x니까 패스
// 완전탐색으로 푸는게 나을듯 -> 어떻게 하더라;;;;

function solution(k, dungeons) {
  let cnt = 0
  let visited = Array.from({length: dungeons.length}, () => 0)

  function DFS(remainHp, level) {
    for (let i=0; i<dungeons.length; i++) {
      // 방문x & hp가 남아있으면 다음레벨 진입
      if (!visited[i] && remainHp >= dungeons[i][0]) {
        visited[i] = 1 // 방문표시
        DFS(remainHp - dungeons[i][1], level+1)

        visited[i] = 0 // 원상복구
      }
    }

    cnt = Math.max(cnt, level)
  }

  DFS(k,0)
  return cnt
}