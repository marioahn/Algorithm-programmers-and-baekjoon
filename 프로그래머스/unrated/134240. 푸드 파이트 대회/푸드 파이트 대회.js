function solution(food) {

  let leftFood = ''
  for (let i=1; i<food.length; i++) {
    leftFood += String(i).repeat(Math.floor(food[i]/2))
  }
  let rightFood = ''
  for (let i=food.length-1; i>0; i--) {
    rightFood += String(i).repeat(Math.floor(food[i]/2))
  }
  
  return leftFood + '0' + rightFood
}