file1 = open("C:/Users/pjzen/OneDrive/Desktop/Programming with Python/unittled.txt", 'r')
lines = 0
characters = 0
words = 0
evenLines = ''
count = 0
x = input("Character to check frequency")
reverse = []
for line in file1:
    lines +=1
    if lines%2 ==0:
        evenLines = evenLines + "\n" + line
    words += len(line.strip().split())
    characters += len(line)

    word = line.strip().split()
    reverse = word[::-1] + reverse



    for x in line:
        count+=1

print(reverse)


file2 = open("C:/Users/pjzen/OneDrive/Desktop/Programming with Python/unittled1.txt", 'w')
file2.write(evenLines)
print(lines, words, characters)
print(count)