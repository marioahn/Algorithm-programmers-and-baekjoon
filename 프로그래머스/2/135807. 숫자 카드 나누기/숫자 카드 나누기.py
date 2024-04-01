# 제한사항
    # 1 ≤ arrayA의 길이 = arrayB의 길이 ≤ 500,000
    # 1 ≤ arrayA의 원소, arrayB의 원소 ≤ 100,000,000
    # arrayA와 arrayB에는 중복된 원소가 있을 수 있습니다.
# -> 유클리드 이용하면 시간제한 해결 가능
# arrayA,B 정렬할 필요 없음
def solution(arrayA, arrayB):
    answer = 0
    # array의 첫 번째 값이 최대공약수로 가정 해 모든 요소와 비교하기 위해 아래처럼 초기화
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    
    for n in arrayA[1:]:
        gcdA = gcd(n, gcdA) # 2,4,6,8,3,7이면 1이 나와야 하는..
        
    for n in arrayB[1:]:
        gcdB = gcd(n, gcdB)
        
    # 두 조건 중 하나를 만족하는 가장 큰 양의 정수 a의 값을 구해야 하므로 각각 max!
    # 첫 번째 조건
    if notDiv(arrayA, gcdB): # True면 그게 바로 정답
        answer = max(answer, gcdB)
    
    # or 두 번째 조건
    if notDiv(arrayB, gcdA):
        answer = max(answer, gcdA)
        
    return answer
 
# 최대공약수
def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)
 
# 처음부터 끝까지 순회해서 떨어지는지 아닌지 확인
    # 안 떨어지면 true반환 = notDiv
def notDiv(array, gcd):
    for n in array:
        if n % gcd == 0:
            return False
    return True


print(solution([10, 17],[5, 20]))
print(solution([10, 20],[5, 17]))
print(solution([14, 35, 119],[18, 30, 102]))