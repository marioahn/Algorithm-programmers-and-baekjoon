# 아래처럼 바로 1~30을 가진 list 만들기 - 한 줄로 가능
students = [i for i in range(1, 31)]
for _ in range(28):
    submit = int(input())
    students.remove(submit)  # 아. 바로 이게 되는구나.. 까먹었네;; 굿굿

print(students[0])  # print(min(students)) 해도 오케이. 아래는 max로
print(students[1])
