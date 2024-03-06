# 모든 달은 28일까지 있다고 가정
# today가 지.나.야 유효기간이 지난 것, today와 = 만료기간? ok
# 결과값 오름차순 return
# 파기해야 할 개인정보가 하나 이상 존재하는 입력만 주어진다
# 날짜 모듈 쓰면, 한 방에 편하게 되긴 할듯 -> 일단 연습할 셈 치고 일일이 구현

# 날짜 비교는 -> 년,월,일을 -> 일로 치환해서 숫자비교(int화)
    # 년은  2000년도부터니까, -2000해서

# pre)날짜 바꾸는 함수
def to_int(str_days):
    return (int(str_days[0:4])-2001)*12*28 + int(str_days[5:7])*28 + int(str_days[8:])

def solution(today, terms, privacies):
    result = []
    # 0. terms는 dict화 시켜서 쉽게 찾을 수 있도록
    dict = {}
    for k in range(len(terms)):
        dict[terms[k][0]] = int(terms[k][2:])
    
    today_int = to_int(today)
    for k in range(len(privacies)):
        day, rank = privacies[k].split(" ")
        day_rank_int = to_int(day) + dict[rank]*28 - 1

        if today_int > day_rank_int:
            result.append(k+1)

    return result


print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])) # [1, 3]
print(solution("2020.01.01",["Z 3", "D 5"],["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])) # [1, 4, 5]


# 레퍼런스 - 축약인데도, 가독성이 좋음. 진짜 두고두고 봐서 익힐 코드인듯 이건
# def to_days(date):
#     year, month, day = map(int, date.split("."))
#     return year * 28 * 12 + month * 28 + day

# def solution(today, terms, privacies):
#     months = {v[0]: int(v[2:]) * 28 for v in terms}
#     today = to_days(today)
#     expire = [
#         i + 1 for i, privacy in enumerate(privacies)
#         if to_days(privacy[:-2]) + months[privacy[-1]] <= today
#     ]
#     return expire