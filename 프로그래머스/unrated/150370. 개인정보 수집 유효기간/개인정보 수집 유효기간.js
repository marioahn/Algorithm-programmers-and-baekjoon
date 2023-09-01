function solution(today, terms, privacies) {
  let answer = [];

  // step1: obj에 약관종류와 기한을 담음
  let obj = {}
  for (let term of terms) {
    let [type, plus] = term.split(' ')
    obj[type] = plus
  }

  // step2: privacies를 순회하면서, 기한을 넘긴 것을 answer에 push
  let idx = 1
  let todayNum = (+today.split('.').join(''))

  for (let privacy of privacies) {
    let [pastDay, type] = privacy.split(' ')
    // 1. 날짜 추가: 달 먼저 + -> 달이 12초과면 연+1
    let [year, month, day] = pastDay.split('.')
    year = +year
    month = +month
    day = +day
    month += (+obj[type])
    if (month > 12) {
      year += parseInt(month/12)
      month = month%12
    }

    // 2. 또한, '일'도 -1해야함 -> '일' 0 되면 달 -1하고, 이때 달이 또 0이 되면 연 -1
    day -= 1
    if (day === 0) {
      month -= 1
      day = 28
    }
    if (month === 0) {
      year -= 1
      month = 12
    }
    // 3. 마지막으로 비교해서 기한 넘겼는지 아닌지 check
    year = String(year)
    month = String(month)
    if (month.length === 1) month = '0' + month // 5면 -> 05로
    day = String(day)
    if (day.length === 1) day = '0' + day

    let expireNum = +(year+month+day)
    console.log(expireNum)
    if ((todayNum > expireNum)) answer.push(idx)
    idx ++ 
  }

  return answer;
};

// console.log(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]));
// console.log(solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]));
// console.log(solution("2020.10.15", ["A 100"], ["2018.06.16 A", "2008.02.15 A"])) // [2]
