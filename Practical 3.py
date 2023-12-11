def patternDraw(n):
    for i in range(1, n+1):
        print(" " * (n-i), end = "")
        print("*" * (i-1), end = "")
        print("*" * i)

    for i in range(1, n):
        print(" " * (i), end = "")
        print("*" * (n-i-1), end = "")
        print("*" * (n-i))

patternDraw(5)