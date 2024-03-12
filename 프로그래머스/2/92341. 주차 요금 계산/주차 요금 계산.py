# 생각해보면, IN & OUT요소는 안 써도 될듯
# 어차피, 홀수면 아웃없고, 짝수면 인앤아웃 짝
import math


# ? 근데 먼가 비효율적인것 같음 -> 더 좋은 방법 없나?
def solution(fees, records):
    dict = {}

    for record in records:
        hour, minute, car_number = record[0:2], record[3:5], record[6:10]
        times = int(hour) * 60 + int(minute)
        if car_number in dict.keys():
            dict[car_number].append(times)
        else:
            dict[car_number] = [times]

    key_list = sorted(list(dict.keys()))  # ['0000', '0148', '5961']

    result = []
    for key in key_list:
        time_info = dict[key]
        if len(time_info) % 2:  # ==1 즉, 홀수
            time_info.append(23 * 60 + 59)

        time_info = [
            time_info[k] if k % 2 != 0 else -time_info[k] for k in range(len(time_info))
        ]
        total_time = sum(time_info)
        print(total_time)
        if fees[0] >= total_time:
            result.append(fees[1])
        else:
            result.append(
                math.ceil((total_time - fees[0]) / fees[2]) * fees[3] + fees[1]
            )

    return result


# print(
#     solution(
#         [180, 5000, 10, 600],
#         [
#             "05:34 5961 IN",
#             "06:00 0000 IN",
#             "06:34 0000 OUT",
#             "07:59 5961 OUT",
#             "07:59 0148 IN",
#             "18:59 0000 IN",
#             "19:09 0148 OUT",
#             "22:59 5961 IN",
#             "23:00 5961 OUT",
#         ],
#     )
# )
print(
    solution(
        [120, 0, 60, 591],
        [
            "16:00 3961 IN",
            "16:00 0202 IN",
            "18:00 3961 OUT",
            "18:00 0202 OUT",
            "23:58 3961 IN",
        ],
    )
)
# print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
