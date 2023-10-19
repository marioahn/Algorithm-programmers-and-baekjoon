# 흠..입력받는 변수가 string,int,int타입인데? 입력 어떻게 하지
while True:
    name, age, weight = input().split()  # 걍 이렇게 하고, 아래에서 int함수 씌우기
    if name == '#':
        break
    if int(age) > 17 or int(weight) >= 80:
        print(f'{name} Senior')
    else:
        print(f'{name} Junior')
