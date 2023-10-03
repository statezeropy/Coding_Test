def solution(arr1, arr2):
    answer = []
    row = len(arr1)
    col = len(arr2)
    arr2_tm = [[arr2[j][i] for j in range(len(arr2))] for i in range(len(arr2[0]))]

    for r in range(row):
        tmp = []
        for ar2 in arr2_tm:
            tmp.append(sum([(arr1[r][c] * ar2[c]) for c in range(col)]))
        answer.append(tmp)

    return answer