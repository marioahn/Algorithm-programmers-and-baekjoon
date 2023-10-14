# tc가 몇개인지 안 알려줌 -> 이 부분에 대한 처리를 해줘야함!!
# 어떻게? -> try-except(breaK)로!
# try: 변수 A,B에 int형이 들어간다면, A+B의 값을 출력한다.
# except: try에 대한 에러가 발생한 경우(ex. a 1, 3, 2 ㄱ 입력)
# break: while문을 멈춘다.
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
