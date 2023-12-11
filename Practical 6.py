str1 = input("Enter Desired String1: ")
str2 = input("Enter Desired String2: ")

n = int(input("First n Number of Characters to be Replaced: "))

if n>len(str1) or n> len(str2):
    Print("Error")
else:
    newStr1 = str1[:n] + str2[n:]
    newStr2 = str2[:n] + str1[n:]
    print(newStr1, newStr2)
