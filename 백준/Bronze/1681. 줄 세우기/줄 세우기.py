N,l = list(map(int,input().split(' ')))

num = 1 # 양의 정수이기 때문에 0이 아닌 1부터 시작합니다
cnt = 0	# 라벨을 붙인 개수
while True:
    if str(l) not in str(num): #해당 숫자를 사용할 수 있으면
        cnt+=1	#라벨을 붙입니다
        if cnt == N: #N개의 원소를 다 라벨링했다면
            print(num) #마지막 값을 출력하고
            break #반복문을 그만둡니다
        num+=1	#반복문이 끝나지 않았다면 다음 숫자로 넘어갑니다

    else:	#l이 포함되어 해당 숫자를 사용할 수 없다면
        num+=1	#다음 숫자로 넘어갑니다