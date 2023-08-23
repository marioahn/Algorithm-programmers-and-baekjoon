// 0. 빈 배열을 하나 선언
// 1. X만큼 반복문을 돌리고, 각 요소가 Y에 포함되는지 확인 
  // 포함된다면, X = X.split(X[i]).join('')으로 줄여주고, -> replace
  // 빈배열에 해당 문자 추가(공통 정수)
// 2. 완성된 배열을 sort하고 하나의 (문자화된)정수로 join
  // 완성된 배열이 여전히 빈 배열이면 -1 return

function solution(X, Y) {
    var answer = '';
    let arr =[];
    let obj ={};
    //{'1': 2, '0':3, '3':2}

    for(let i=0; i<X.length;i++){
      obj[X[i]] ? obj[X[i]]++ : obj[X[i]] = 1;    
    }
    for(let i=0; i<Y.length;i++){
      if(obj[Y[i]]>0){
        arr.push(Y[i]);
        obj[Y[i]]--;
      }
    }

    arr = arr.map(Number);
    answer = arr.sort((a,b)=>b-a).join('');
    if(answer[0]==='0') return '0';
    
    return arr.length ===0 ? '-1' : answer;
}