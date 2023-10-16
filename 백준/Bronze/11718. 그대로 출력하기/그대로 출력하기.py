# try문으로 안 들어게 되면 컷
# how? -> EOF에러로!
while True:
    try:
        print(input())
    except EOFError:  # 이게 핵심
        break
