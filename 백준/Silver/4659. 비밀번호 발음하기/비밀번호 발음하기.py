while True:
    pas = input()
    if pas == "end":
        break
    arr = [False] * len(pas)
    flag = True
    for i in range(len(pas)):
        if pas[i] in "aeiou":
            arr[i] = True
    if not any(arr):
        flag = False
    
    for i in range(len(pas)-1):
        if pas[i] == pas[i+1] and pas[i] not in 'eo':
            flag = False
            break
    
    for i in range(len(pas)-2):
        if all(arr[i:i+3]) or not any(arr[i:i+3]):
            flag = False
            break
    
    if flag:
        print(f"<{pas}> is acceptable.")
    else:
        print(f"<{pas}> is not acceptable.")