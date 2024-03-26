# swea: 문자열 동화 D5
# 세 문자열에서 공통된 것 먼저 뽑아내고, 오름차순 -> 나머지 공통x or 쩌리를 change
# west, east, wait -> 끝에서부터 보자
    # t는 3개 -> 통과 / 그 다음 s는 2개 ok / a가 2개
        # 어. 근데 모두 west로 바꾸는게 best인데, 이러면 wast가 될수도 없고 안될텐데
# 단, 원형을 유지할 필요가 전혀 없음!
# 그냥 set으로 처리하기 -> set에 1개만 들어가면 3단어 모두 공통이니까 넘어가고
    # set에 2개만 들어가면 2단어는 공통이란 뜻이니까 1개단어만 바꾸면 됨
    # set에 3개 들어가면 3단어 모두 다르니까 나머지 2개
T = int(input())

for tc in range(1,T+1):
    n = int(input())
    a = input()
    b = input()
    c = input()

    switch_cnt = 0
    for i in range(len(a)):
        tmp_set = set()
        tmp_set.add(a[i])
        tmp_set.add(b[i])
        tmp_set.add(c[i])

        switch_cnt += len(tmp_set)-1


    print(f'#{tc} {switch_cnt}')
