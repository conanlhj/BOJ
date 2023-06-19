for p in range(int(input())):
    t, *arr = map(int, input().split())
    srt = [arr[0]]
    cnt = 0
    for kid in arr[1:]:
        flag = True
        for i in range(len(srt)):
            if srt[i] > kid:
                srt.insert(i, kid)
                flag = False
                cnt += len(srt) - i - 1
                break
        if flag:
            srt.append(kid)
    print(t, cnt)