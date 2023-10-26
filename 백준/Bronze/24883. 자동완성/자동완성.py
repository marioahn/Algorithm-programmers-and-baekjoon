# import sys
# input = sys.stdin.readline
# sys붙이면 안됨 why?
# 제시한 코드에서 a는 sys.stdin.readline을 통해 사용자 입력을 받는 변수입니다. sys.stdin.readline 함수는 한 줄을 읽어서 문자열로 반환하는 함수이며, 읽은 줄 끝에 줄 바꿈 문자 ('\n')도 포함됩니다.
# 따라서 사용자가 'N'을 입력하면 실제로 'N\n'로 읽히게 됩니다. 따라서 a는 'N\n'이 되고, 이는 ['N', 'n'] 리스트에는 포함되지 않으므로 if 조건문에서 a는 'N' 또는 'n'과 일치하지 않으므로 else 블록이 실행되어 'Naver Whale'을 출력합니다.
# 해결 방법으로는 a에서 줄 바꿈 문자를 제거한 후 조건문을 검사하면 원하는 동작을 얻을 수 있습니다. 다음은 수정된 코드의 예시입니다:

a = input()
if a in ['N', 'n']:
    print('Naver D2')
else:
    print('Naver Whale')
