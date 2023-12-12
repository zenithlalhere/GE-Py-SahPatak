str1 = input("Enter Desired String1: ")
str2 = input("Enter Desired String2: ")



list1 = []
ind = 0
while ind < len(str1):
    adder = str1.find(str2, ind)
    print(adder)
    if adder == -1:
        print(adder)
        break
    else:
        list1.append(adder)
        ind = adder
    ind += 1
