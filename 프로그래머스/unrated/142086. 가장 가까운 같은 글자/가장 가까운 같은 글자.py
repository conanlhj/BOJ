def solution(s):
    answer = []
    d = {}
    for i, c in enumerate(s):
        if c in d.keys():
            answer.append(i-d[c])
            d[c] = i
        else:
            d[c] = i
            answer.append(-1)
    return answer