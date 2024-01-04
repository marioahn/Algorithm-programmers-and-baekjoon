group = []
groups = []
while True:
    num = int(input())
    if num == 0:
        break
    for i in range(num): # 그룹의 길이만큼 반복
        student = input().split()
        group.append(student)
    groups.append(group)
    group = []
for i in range(len(groups)): # 그룹의 길이만큼 반복
    if i!=0:
        print()
    print("Group",i+1)
    cnt = 0
    for j in range(len(groups[i])):
        bad = -1
        if 'N' in groups[i][j]:
            nasty = groups[i][j].count('N')
            for k in range(nasty):
                bad = groups[i][j].index('N',bad+1)
                badp = (len(groups[i])+j-bad)%len(groups[i])
                print(groups[i][badp][0],"was nasty about",groups[i][j][0])
            cnt += 1 # cnt가 0인 경우 Nobody was nasty를 출력해야하기 때문에 구별을 위해 사용
    if cnt == 0: # 나쁜 말을 한 사람이 아무도 없는 경우
        print("Nobody was nasty") 