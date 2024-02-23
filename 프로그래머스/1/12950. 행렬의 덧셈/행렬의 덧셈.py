import numpy as np # 이거 사용해서 가능?
# numpy array를 'list'로 바꿀 수 있음 -> np_array.tolist() 함수 사용
def solution(arr1, arr2):
    num_arr1 = np.array(arr1)
    num_arr2 = np.array(arr2)
    sum = num_arr1 + num_arr2
    return sum.tolist()