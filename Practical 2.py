n = int(input("Give n: "))
x = int(input("Give x till prime to be generated"))
def checkPrime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n%i == 0:
            return False
        else:
            return True


def tillPrime(n):
    listOfPrime = []
    for i in range(2, n):
        if checkPrime(i) == True:
            listOfPrime.append(i)
    print(listOfPrime)

    j = 2
    while len(listOfPrime) != x:
        if checkPrime(j) == True:
            listOfPrime.append(j)
        j+=1
    print(listOfPrime)



print(checkPrime(n))
tillPrime()
