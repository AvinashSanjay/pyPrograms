import time

odd = set([x*1+2 for x in range(1,5)])
primes = set(list())
for i in range(2,10):
    j = 2
    f = 0
    while j< i/2:
        if i %j == 0:
            f=1
        j+=1
    if f==0:
        primes.add(i)
print("Set of Odd Numbers(A) ",odd,"\n")
print("Set of Prime Numbers(B) ",primes,"\n")
print("union -> A U B ", odd.union(primes),"\n")
print("intersection -> A n B ", odd.intersection(primes),"\n")
print("difference -> A - B ", odd.difference(primes),"\n")
print("symmetric_difference -> A ^ B ", odd.symmetric_difference(primes),"\n")

time.sleep(510)
