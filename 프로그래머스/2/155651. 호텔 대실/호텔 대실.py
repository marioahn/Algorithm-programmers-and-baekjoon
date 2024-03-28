# 레퍼런스 코드 - 누적합 -> 훨---씬 빠름.
    # 마지막 tc: 내 코드는 490ms인데, 이건 8ms (메모리는 비슷)
def solution(book_time):
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    
    print(time_table)
    return max(time_table)