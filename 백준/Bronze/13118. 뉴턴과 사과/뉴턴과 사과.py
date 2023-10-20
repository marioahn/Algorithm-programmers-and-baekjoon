numbers = list(map(int, input().split()))
x, y, r = map(int, input().split())
print(numbers.index(x)+1 if x in numbers else 0)  # python에서의 삼항연산자 느낌ㅇㅇ
