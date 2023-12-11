str = input("Enter Your String: ")
char1 = input("Character to Find Frequency: ")
rep1 = input("Character to Find : ")
rep2 = input("Character to Replace : ")
occu = input("Character to be removed on First Occurance: ")
global freq
freq = 0

for i in str.lower():
    if i == char1.lower():
        freq +=1
print(f"Frequency is {freq}")


replacedStr = str.replace(rep1, rep2)
print(replacedStr)

removedStr = str.replace(occu, "", 1)
print(removedStr)

removedStr = str.replace(occu, "")
print(removedStr)

