T = int(input())

for tc in range(1,T+1):
    numbers = list(map(int,input().split()))

    numbers = [number for number in numbers if number % 2 ==1]
    print(f"#{tc} {sum(numbers)}")