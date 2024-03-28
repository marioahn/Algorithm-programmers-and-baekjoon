# book_time정렬하면 시작시간 기준으로 정렬됨. 단, 끝 시간은 뒤죽박죽
# room개수를 늘린다는 것을 어떻게 구현할 것인가?
    # stack에 [] << 빈 배열을 추가(=방)하는 식?
    # book_time순회하면서 하나 씩 체크하는데, 이때 stack도 같이 순회하면서 체크
    # 만약, 끝 타임+10이면 해당 룸 방 빼도 되는거지
        # 또한, 각 방에는 2개가 동시에 들어갈 수 없음. []를 아예 추가시켜야지
        # 단, 방 뺄 때 []를 삭제시키면 안됨. -> 그래야 방 수 유지시키지
    # * 근데 여기서 필요한 "최소 객실의 수"를 return해야 함
        # dfs같은 다른 기법도 적용시켜야 하나..
        # stack에 추가할 때 끝시간을 기준으로 정렬시킨 후에.
            # 근데 stack을 또 정렬한다는게 맞는건가? -> 물론 book_time정렬보단 낫긴 하지만..
            # 흠;; -> 다시 생각해보니 stack은 정렬할 필요 없을 듯
        # 앞에서부터 조건에 맞는 것 컷팅

def solution(book_time):
    room_stack = [] # stack의 길이: 필요한 최소 방 수 - 손님을 한 명도 놓치지 않기 위한
    book_time.sort()

    for book in book_time:
        if not room_stack:
            room_stack.append(book) # book자체가 리스트
        else:
            flag = False
            for booked in room_stack:
                hour_dif = (int(book[0][:2]) - int(booked[1][:2]))*60
                minute_dif = int(book[0][3:]) - int(booked[1][3:]) - 10 # 10은 청소시간
                
                if hour_dif+minute_dif >= 0: # 퇴실+10분(청소) <= 현재 예약예정시간
                # if booked[1]+10 <= book[0]: 
                    booked[0], booked[1] = book[0], book[1]
                    flag = True
                    break
            
            if not flag: # 빈방 없으면 추가
                room_stack.append(book)

    return len(room_stack)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))