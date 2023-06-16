N,G=input().split()
a=set([input()for _ in range(int(N))])
print(len(a)//{"Y":1,"F":2,"O":3}[G])