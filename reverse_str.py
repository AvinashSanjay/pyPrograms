def rev(str1):
    str2 = ""
    i = len(str1)-1
    while i >= 0:
        str2 += str1[i]
        i -= 1
    return str2
    
word = input("Enter a String: ")
print("\n The Mirror Image of the given String is ",rev(word))
 