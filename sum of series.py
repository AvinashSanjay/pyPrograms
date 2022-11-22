n = int(input("enter a value of n: "))
s = 0.0
for i in range (1,n+1):
    a = float(i**i)/i 
    s = s+a
print("Sum of series is ",s)