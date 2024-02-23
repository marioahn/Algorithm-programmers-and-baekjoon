# 앞/뒷자린 나눈 후에, 앞자리 전부 replace로 * 바꾼 후에, 두개 합치기?
# ㄴㄴ 번거로움. 그냥 문자->리스트로 바꾼 후에, len(range)로 뒷번호4개 전까지만 바꾸고, join
# 꼭 순회를 해야하는가? 반복문으로. 아 ㄴㄴ
    # -> phone_number의 길이-4 * '*' + 뒷자리4를 단순히 하면 끝나네
    # 이렇게 하면 문자 전체가 아닌, 4개만 고정적으로 순회하면 됨

def solution(phone_number):
    return (len(phone_number)-4)*'*' + phone_number[len(phone_number)-4:len(phone_number)]

