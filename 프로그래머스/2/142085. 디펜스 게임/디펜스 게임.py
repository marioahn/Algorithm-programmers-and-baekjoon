# 주어진 순서대로 데이터를 누적으로 계산하는 중에 조건에 부합하지 않은 상황이 발생했을 경우,
# 현재 누적되어 있는 데이터 중 가장 큰 값, 혹은 작은 값의 제거가 필요한 경우!!!
# -> 사용할 수 있는 자료구조는 힙(heap) 자료구조이다
    # 아래에서 heappop으로 heap리스트에서 가장 작은 것 추출하는데, min보다 훨씬 효율적임
    # min으로 찾았으면 바로 시간초과임

# 풀이
# (1)적의 수(e)를 최대힙 자료구조(heap)에 음수형식으로 저장
# (2)적의 전체 수(sumEnemy)에 적의 수(e)를 누적으로 더한다
# (3)만약 적의 전체 수(sumEnemy)가 보유한 병사(n)보다 많을 경우
    # 무적권(k)도 존재하지 않는다면 더 이상 라운드를 진행할 수 없다(break)
    # 최대힙 자료구조(heap)에서 지금까지 진행해온 라운드 중 적이 가장 많은 라운드를 찾아서(heappop),
        # -> 적의 전체 수(sumEnemy)의 값을 차감하고, 무적권(k)의 수도 1 만큼 차감한다.

from heapq import heappop, heappush

def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e)
        sumEnemy += e
        if sumEnemy > n:
            # 무적권도 없으면 라운드 종료
            if k == 0:
                break
            # 무적권 있는 경우
            sumEnemy += heappop(heap) # heap에서 가장 작은 원소를 pop 
            k -= 1
        answer += 1
    return answer