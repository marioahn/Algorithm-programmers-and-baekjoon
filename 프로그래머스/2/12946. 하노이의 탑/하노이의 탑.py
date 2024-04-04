# 이번 문제가 전형적으로, 손코딩으로 시작해야 하는 것
# 노트에 적어두면서 하지 않았다면 진짜 절대 못했을듯;;
# 과정
    # 1)n개의 원판을 옮기기 위해서는 n-1개의 원판을 중간 기둥까지 옮겨야 하고,
    # 2)1번 기둥에서 3번 기둥으로 n번째 원판을 옮긴다
    # 3)다시 중간 기둥에 위치한 n-1개의 원판을 3번 기둥으로 옮기면 끝!
# 다시 정리하면,
    # n-1개의 원판을 출발 기둥에서 중간 기둥으로 이동(재귀)
    # -> n번째 원판을 출발 기둥에서 도착 기둥으로 이동
    # -> n-1개의 원판을 중간 기둥에서 도착 기둥으로 이동(재귀)
def hanoi(start, target, mid, n):
    if n==1:
        routes.append([start,target])
    else:
        hanoi(start, mid, target, n-1)
        hanoi(start, target, mid, 1)
        hanoi(mid, target, start, n-1)

routes = []
def solution(n):
    hanoi(1,3,2,n)

    return routes