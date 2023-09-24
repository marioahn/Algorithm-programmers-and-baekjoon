function solution(fees, records) {
  let sumParking = {} // 총 주차시간이 몇분인지 Sum.
  let tmpLog = {}

  // step1: 채우기
  for (let record of records) {
    let [ time, car, order ] = record.split(' ')
    let [hour, minutes] = time.split(':')
    let sumMinutes = Number(hour)*60 + Number(minutes) 
    
    if (tmpLog[car] === undefined) {
      tmpLog[car] = sumMinutes
    } else { // 이미 차있다면?
      sumMinutes -= tmpLog[car] // 차감시간 구하고,
      tmpLog[car] = undefined // 초기화 -> 0으로 하면, 마지막 예시에서 꼬임
      if (!sumParking[car]) sumParking[car] = sumMinutes
      else sumParking[car] += sumMinutes // 여기에 업데이트
    }
  }

  // step2: In만 있는 경우 -> 23:59에 자동 out시키기
  let keys = Object.keys(tmpLog).sort((a,b) => a-b) // return은 차량 번호 적은 순으로
  for (let key of keys) {
    if (!sumParking[key]) sumParking[key] = 0 // 마지막 예시 경우 대비(NaN나오는거 방지)
    if (tmpLog[key] >= 0) {
      sumParking[key] += 24*60 - 1 - tmpLog[key]
    }
  }

  let result = []
  for (let key of keys) {
    totalFee = fees[1] + Math.ceil((sumParking[key] - fees[0])/fees[2]) * fees[3]
    if (totalFee < fees[1]) result.push(fees[1])
    else result.push(totalFee)
  }


  return result
}

console.log(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
console.log(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
console.log(solution([1, 461, 1, 10],["00:00 1234 IN"]))