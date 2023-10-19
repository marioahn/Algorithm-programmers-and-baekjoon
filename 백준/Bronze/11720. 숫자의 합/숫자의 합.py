# 문자가 아닌, 숫자의 각 요소를 순회하는 법??
# way1 : sum함수 + 입력값받는 족족 더하기(split안씀 ㅇㅇ)
n = int(input())
print(sum(map(int, input())))