while True:
    com = input()
    if com == "# 0 0":
        break
    
    name, age, kg = com.split()
    if int(age) > 17 or int(kg) >= 80:
        print(name, "Senior")
    else:
        print(name, "Junior")