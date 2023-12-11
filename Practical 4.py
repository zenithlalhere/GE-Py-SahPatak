charInput = input("Input your single character: ")

if len(charInput) > 1:
    print("Error")
elif charInput[0].islower() or charInput[0].isupper():
    print("Character")
    if charInput[0].islower():
        print("Character is Lower")
    else:
        print("Character is Upper")

elif charInput.isdigit():
    print("Numerical")
    numName = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    print(numName[int(charInput)])

else:
    print("Special Character")