# 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다
# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에,
# 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다

# ->제한사항: 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다!!
import sys

N = int(input())
for i in range(N):
    # map(int, input().split())대신에, sys.stdin.readline()
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
