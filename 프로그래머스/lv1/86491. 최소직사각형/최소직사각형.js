function solution(sizes) {
  let arr1 = []
  let arr2 = []
  for (let i=0; i<sizes.length; i++) {
      if (sizes[i][0] >= sizes[i][1]) { 
        arr1.push(sizes[i][0])
        arr2.push(sizes[i][1])
      }
      else {
        arr2.push(sizes[i][0])
        arr1.push(sizes[i][1])
      }
    }
  // return console.log(arr1,arr2)
  return (Math.max(...arr1))*(Math.max(...arr2)) // Math.max([1,2,3]) -> NaN값
}