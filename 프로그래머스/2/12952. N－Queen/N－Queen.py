# 1
# 기본적으로 dfs풀이를 생각하였는데, 다른 풀이보니까 굳이 그럴 필요가 없는 듯
    # https://school.programmers.co.kr/questions/41738 - dfs이외의 풀이

# n*n -> n개의 퀸을 배치해야 함 -> 어찌되었든 한.줄(한 행)에 퀸이 1개씩만 들어가야 함
# 한 행에 q배치하면, 바로 다음행으로 이동ㄱㄱ -> 끝행까지 도달해서 놓으면 cnt+1
# dfs만들고, 한행의 각 열에 퀸 미리 1개 놓고 dfs진입(for문으로 dfs진입)
# queen을 놓으면 사정거리블록은 모두 x표시해서, 다음 퀸 배치할 때 참고하기 - 이게 편할듯!
# visited 초기화 및 원상복구 조심
    # 흠.. 2개까지 되었는데 3개에서 빠꾸먹으면 2개째 폭탄범위를 back시켜야 하는데,
    # how..?
# -> 위 방법 폐기 -> 그냥, 대각/가로/세로에 다른 queen이 존재하느냐로 판별

# 레퍼런스풀이 - https://geunuk.tistory.com/178
    # *한 행에 하나의 퀸만 있을 수 있다 -> 1차원 배열로 표현 가능 WOW.
    # 이렇게 하면, 무작정 했을 때보다 훨씬 효율적 & 시간초과 문제도 해결 가능!
    # DFS탐색: 세로에 있을 경우, 대각선에 있을 경우를 배제하며 진행

# 와. 아래처럼 하면, count를 전역변수처럼 관리할 수가 있구나;; 스킬과 짬이 진짜 장난 아니네;
# 또한, n이 12이하여서 얕봤지만, 사실 돌아가는 dfs수로만 보면 매.우 빡빡하다
# 시간초과도 겨우겨우 통과한다. -> 대각체크에서 abs(row-x)로 하면 마지막 tc는 통과 못한다..;;
def dfs(queen, n, row):
    count = 0
    
    if n == row: # 마지막행에 도달하면? -> 모-든행에 queen배치 완료했다는 뜻이니 return 1!
        return 1
    
    # *for-else문: 반복문이 break될 경우에는 else 블록이 실행되지 않는다. 오!
    # 가로로 한번만 진행
    for col in range(n):
        queen[row] = col # 퀸 배치 -> queen[2] = 2면, 2행 2열에 배치되었다는 뜻
        # *행검사 -> 현재 3행까지 배치했으면, 1,2,3행의 세로/대각 퀸 검사하고, break x면. 3행 배치컨펌o -> 다음 dfs로 ㄱㄱ
        for x in range(row): 
            # 세로로 겹치면 안됨
            if queen[x] == queen[row]:  # 열이 같으면 = 세로 -> x
                break
                
            # 대각선으로 겹치면 안됨
                # 두 퀸: (2, 3), (4, 5) -> 4-2 = 5-3 -> 대각선!
                # 즉, 두 위치 (x1, y1)과 (x2, y2)가 대각선상에 있을 조건은 |x2-x1| == |y2-y1|
                # queen[x]는 x행에 위치한 퀸의 열 위치를, queen[row]는 현재 row에 자리잡은 퀸의 열 위치
                # row-x는 두 퀸 사이의 행 차이
            if abs(queen[x]-queen[row]) == (row-x): # abs(row-x)로 했으면, 시간초과에서 걸림
                break
        else:
            count += dfs(queen, n, row+1)
            
    return count
 
def solution(n):
    queen = [0]*n 
    return dfs(queen, n, 0)
