str = input()
result = ''
for i in str:
    if i <= 'Z':
        result += i.lower()
    else:
        result += i.upper()
print(result)
