def solution(n):
    return '수박'*(n//2) if (n%2) == 0 else '수박'*(n//2) + '수'
    # 레퍼런스 아래 방법이 오히려 더 깔끔한듯
    # str = "수박"*n
    # return str[:n]