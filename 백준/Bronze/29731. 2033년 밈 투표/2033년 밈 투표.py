# js의 includes => python은 "in"!!
n = int(input())
bucket = ["Never gonna give you up",
          "Never gonna let you down",
          "Never gonna run around and desert you",
          "Never gonna make you cry",
          "Never gonna say goodbye",
          "Never gonna tell a lie and hurt you",
          "Never gonna stop"]
flag = ''
for _ in range(n):
    a = input()
    if a not in bucket:
        print('Yes')
        flag = 'True'
        break
if flag == '':
    print('No')
