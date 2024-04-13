# 2 - 레퍼런스 풀이 -> 1트 풀이보다 6배 이상 빠르다!
ans = 0
chkX = [False for i in range(32)]
chkCross1 = [False for i in range(32)] # 오른대각
chkCross2 = [False for i in range(32)] # 왼대각

def nq(y, n):
    global ans
    x = 0
    if y > n:
        ans+=1
    for x in range(1, n+1): # 한 줄 배치하면, 가로전부, 대각쪽 전부 O표시하기
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

