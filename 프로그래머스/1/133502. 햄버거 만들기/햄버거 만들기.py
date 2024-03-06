# ingredient자체를 검사하면서, remove하거나 pattern을 'in'문법을 사용해서 푸는게 x
# 앞에서부터 ingredient순회하면서 새 배열에 요소를 추가함
# 그리고, 새 배열의 [-4:-1]가 pattern과 맞는지? 를 체크하면 훨씬 효율적임ㅇㅇ.
def solution(ingredient):
    cnt = 0
    bucket = []
    for ele in ingredient:
        bucket.append(ele)
        if bucket[-4::] == [1,2,3,1]:
            cnt += 1
            # bucket = bucket[:-4]
            del bucket[-4::]

    return cnt
