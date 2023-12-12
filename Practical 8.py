listInput = input("Enter your List by commas").split(",")
listCubes = []
for i in listInput:
    if i.strip().isdigit():
        if int(i)%2 ==0:
            x = int(i)**3
            listCubes.append(x)
print(listCubes)
