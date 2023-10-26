N, M = map(int, input().split())

if M in [1, 2]:
    print('NEWBIE!')
elif N >= M:
    print('OLDBIE!')
else:
    print('TLE!')
