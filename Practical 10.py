def dicGen():
    dictGenerated={}

    for i in range(1,6):
        
        dictGenerated[i] = i**3
    return dictGenerated
    
print(dicGen())