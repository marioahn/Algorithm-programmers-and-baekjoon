# def solution(sizes):
#     max_list, min_list = [], []
#     for ele in sizes:
#         max_list.append(max(ele))
#         min_list.append(min(ele))
    
#     return max(max_list) * max(min_list)

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)