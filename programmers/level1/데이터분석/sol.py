def solution(data, ext, val_ext, sort_by):
    answer = []
    answer_dict = {}
    for i in data:
        mdict = {
            'code' : i[0],
            'date' : i[1],
            'maximum' : i[2],
            'remain' : i[3],
        }

        if mdict[ext] <= val_ext:
            answer_dict[mdict[sort_by]] = i
    for i in sorted(answer_dict):
        answer.append(answer_dict[i])
    
    return answer


print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], 'date', 20300501, "remain"))



# 다른 풀이
# def solution(data, ext, v_ext, srt):
#     answer = []
#     mdict = {"code":0, "date":1, "maximum":2, "remain":3}
    
#     for d in data:
#         if d[mdict[ext]] < v_ext:
#             answer.append(d)

#     return sorted(answer, key = lambda x: x[mdict[srt]])