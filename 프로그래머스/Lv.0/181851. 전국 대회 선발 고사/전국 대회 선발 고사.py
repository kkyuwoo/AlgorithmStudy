def solution(rank, attendance):
    answer = 0
    dic = {}
    for i in range(len(rank)):
        dic[i] = [rank[i], attendance[i]]
    dic = dict(sorted(dic.items(), key=lambda x: x[1][0]))
    mem = 0
    result = []
    for key in dic:
        if mem == 3:
            break
        if dic[key][1] == True:
            mem += 1
            result.append(key)
    answer = 10000 * result[0] + 100 * result[1] + result[2]
    return answer