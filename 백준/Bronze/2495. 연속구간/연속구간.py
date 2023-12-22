for _ in range(3):
    s = input()
    len_max = 0 #가장 긴 길이
    cnt = 1 #같은 숫자가 나온 횟수
    for i in range(1, len(s)):
        #전과 같으면 +1, 다르면 1로 초기화
        if s[i-1] == s[i]:
            cnt += 1
        else:
            cnt = 1

        #cnt가 더 크면 max값 교체
        if cnt > len_max:
            len_max = cnt
    print(len_max)