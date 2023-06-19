import math as m
a,b=sorted(map(int,input().split()))
x,y=map(int,input().split())
x,f=abs(x),True
if not 0<=y<x:f=False
p,q=m.ceil((a-y)/x),m.floor((b-y)/x)
print(p*x+y if q-p==0 and f else "Unknwon Number")