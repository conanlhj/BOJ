prime = [True]*(123456*2)
prime[0] = False
for i in range(1, int((123456*2)**.5)):
    if prime[i]:
        for j in range(i+1, 123456*2-1, i):
            prime[j+1] = False
