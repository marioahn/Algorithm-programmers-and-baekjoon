# 2 - 레퍼런스 풀이 -> 1트 풀이보다 6배 이상 빠르다!
ans = 0
chkX = [False for i in range(25)] # 현.재.열에 퀸이 배치되어 있는지?
chkCross1 = [False for i in range(25)] # *오른대각 -> 왼쪽아래에서 오른쪽 위로 올라가는걸 말하는 것 - 주의!
chkCross2 = [False for i in range(25)] # *왼대각 -> 왼쪽위에서 오른쪽 아래로 내려가는걸 말하는 것 - 주의!
# 왜 25칸인가? - n이 최대 12일 수 있는 상황에서 대각선 인덱싱에 대한 충분한 범위를 제공하기 위함
    # -> 2n-1 -> +2(0인덱스는 사용x, 양수위한 +n고려)
# 왜 y+x가 오른대각? -> 왼쪽아래에서 오른쪽 위로 가는것: (2,2)기준으로, (3,1), (1,3)가 오른대각ㅇㅇ
# 왜 y-x가 왼대각? -> (2,2)기준으로 (1,1), (3,3)가 예시 -> 왼대각은 y-x가 다 같음ㅇㅇ
# *★따.라.서 이러한. 규.칙이 있으므로 굳.이 모-든 공격범위 지점에 True를 표시할 필요가 1도 없는 것;;★

def nq(y, n): # y는 행의미, x는 열의미
    global ans
    
    if y > n:
        ans+=1
    for x in range(1, n+1): # y행 "x열"에 퀸을 배.치한다는 의미
        if chkX[x] or chkCross1[y + x] or chkCross2[(y - x) + n]:
            continue
        chkX[x] = True
        chkCross1[y + x] = True
        chkCross2[(y - x) + n] = True

        nq(y + 1, n)
        # 전부 백트랙킹 ㄷㄷ; - 내가 처음 구상했던 거임 이게
        chkX[x] = False
        chkCross1[y + x] = False
        chkCross2[(y - x) + n] = False


def solution(n):
    nq(1, n)
    return ans
