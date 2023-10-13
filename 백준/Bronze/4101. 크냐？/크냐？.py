# python while문 ㅇㅇ.
# 호.. 저렇게 종료조건 찾네 -> 입력: 여러 개의 tc라고 했지, 몇개라고는 말안했으니까!!
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        print("Yes")
    else:
        print("No")
