# 제한조건
    # 1 ≤ report의 길이 ≤ 200,000
    # 정확성 테스트 : 10초
# dict2개 사용
# report먼저 중복 제거 -> (1)set->list? (2)아니면 그냥 메서드 찾아보기?

# * value가 모두 0인 dict생성하기: dict.fromkeys(list, 0)
    # -> or 딕셔너리 컴프리헨션 ㄱㄱ

# --------------------------------------------------
def solution(id_list, report, k):
    # dict = dict.fromkeys(id_list,0)
    report_dict = {id:[] for id in id_list}
    reported_cnt = {id:0 for id in id_list}
    
    # 1. report중복 제거
    report = list(set(report))
    # 2. dict채우기 + 3. 신고당한 횟수 채우기
    for rp in report:
        reporting, reported = rp.split(' ')
        report_dict[reporting].append(reported)
        reported_cnt[reported] += 1

    # 3. 신고한 사람이, 자기 신고가 먹혔는지 확인하는 것
    result = []
    for id in id_list:
        cnt = 0
        for id2 in report_dict[id]:
            if reported_cnt[id2] >= k:
                cnt +=1
        result.append(cnt)
    

    return result


print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)) # [2,1,1,0]
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)) # [0,0]