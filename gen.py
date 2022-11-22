num1 = []
for i in range (1,11):
    num1.append(i)
print ("Numbers ",num1)

for j,i in enumerate(num1):
    if (i%2 != 0):
        del num1[j]
print("the value after :", num1)        