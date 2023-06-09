stack = []
for c in input():
    stack.append(c)
    
    while len(stack) >= 4:
        if stack[-4:] == list("PPAP"):
            for i in range(4):
                stack.pop()
            stack.append("P")
        else:
            break
if stack == ["P"]:
    print("PPAP")
else:
    print("NP")